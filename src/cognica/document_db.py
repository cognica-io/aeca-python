#
# Cognica
#
# Copyright (c) 2023 Cognica, Inc.
#

# pylint: disable=no-member,missing-class-docstring,missing-function-docstring
# pylint: disable=invalid-name,no-else-return

import io
import json
import time
import typing as t

import grpc

import pandas as pd
import polars as pl
import pyarrow as pa
import pyarrow.parquet as pq

from cognica.channel import Channel
from cognica.protobuf import document_pb2, document_db_pb2, document_db_pb2_grpc


messages: t.TypeAlias = document_db_pb2  # type: ignore

DocumentDBServiceStub = document_db_pb2_grpc.DocumentDBServiceStub

IndexType: t.TypeAlias = messages.IndexType  # type: ignore
IndexStatus: t.TypeAlias = messages.IndexStatus  # type: ignore
IndexDesc: t.TypeAlias = messages.IndexDesc  # type: ignore
CreateIndexRequest: t.TypeAlias = messages.CreateIndexRequest  # type: ignore
CreateIndexResponse: t.TypeAlias = messages.CreateIndexResponse  # type: ignore
DropIndexRequest: t.TypeAlias = messages.DropIndexRequest  # type: ignore
DropIndexResponse: t.TypeAlias = messages.DropIndexResponse  # type: ignore
GetIndexRequest: t.TypeAlias = messages.GetIndexRequest  # type: ignore
GetIndexResponse: t.TypeAlias = messages.GetIndexResponse  # type: ignore

Query: t.TypeAlias = messages.Query  # type: ignore

FindRequest: t.TypeAlias = messages.FindRequest  # type: ignore
FindResponse: t.TypeAlias = messages.FindResponse  # type: ignore
FindBatchRequest: t.TypeAlias = messages.FindBatchRequest  # type: ignore
FindBatchResponse: t.TypeAlias = messages.FindBatchResponse  # type: ignore

CountRequest: t.TypeAlias = messages.CountRequest  # type: ignore
CountResponse: t.TypeAlias = messages.CountResponse  # type: ignore
ContainsRequest: t.TypeAlias = messages.ContainsRequest  # type: ignore
ContainsResponse: t.TypeAlias = messages.ContainsResponse  # type: ignore

InsertRequest: t.TypeAlias = messages.InsertRequest  # type: ignore
InsertResponse: t.TypeAlias = messages.InsertResponse  # type: ignore
UpdateRequest: t.TypeAlias = messages.UpdateRequest  # type: ignore
UpdateResponse: t.TypeAlias = messages.UpdateResponse  # type: ignore
RemoveRequest: t.TypeAlias = messages.RemoveRequest  # type: ignore
RemoveResponse: t.TypeAlias = messages.RemoveResponse  # type: ignore
GetCollectionRequest: t.TypeAlias = (
    messages.GetCollectionRequest  # type: ignore
)
GetCollectionResponse: t.TypeAlias = (
    messages.GetCollectionResponse  # type: ignore
)
TruncateCollectionRequest: t.TypeAlias = (
    messages.TruncateCollectionRequest  # type: ignore
)
TruncateCollectionResponse: t.TypeAlias = (
    messages.TruncateCollectionResponse  # type: ignore
)
ListCollectionsRequest: t.TypeAlias = (
    messages.ListCollectionsRequest  # type: ignore
)
ListCollectionsResponse: t.TypeAlias = (
    messages.ListCollectionsResponse  # type: ignore
)


def _to_json(doc):
    if isinstance(doc, document_pb2.Document):  # type: ignore
        return doc
    elif isinstance(doc, (dict, list)):
        return document_pb2.Document(  # type: ignore
            json=json.dumps(doc, ensure_ascii=False)
        )

    return document_pb2.Document(json=doc)  # type: ignore


class Request:
    def __init__(
        self,
        collection,
        query,
        index_columns=None,
        columns=None,
        dtypes=None,
        skip=None,
        limit=None,
    ):
        query = _to_json(query)

        self.collection = collection
        self.query = query
        self.index_columns = index_columns
        self.columns = columns
        self.dtypes = dtypes
        self.skip = skip
        self.limit = limit


def _create_stub(stub: t.Callable, channel: Channel):
    stub = stub(channel.channel)

    return stub


class DocumentDB:
    Request = Request

    def __init__(self, channel: Channel, timeout: int | None = None):
        self._max_retry_count = 5
        self._stub = _create_stub(DocumentDBServiceStub, channel)
        self._timeout = timeout

    def find(
        self,
        collection,
        query,
        limit=None,
        index_columns=None,
        columns=None,
        dtypes=None,
        to_pandas=True,
        to_polars=False,
        to_arrow=False,
        enable_profile=False,
    ) -> (
        pd.DataFrame
        | pl.DataFrame
        | pa.Table
        | tuple[pd.DataFrame | pl.DataFrame | pa.Table, dict]
    ):
        if to_polars or to_arrow:
            to_pandas = False

        query = _to_json(query)
        req = FindRequest(
            query=Query(collection_name=collection, query=query),
            limit=limit,
            index_columns=index_columns,
            columns=columns,
            dtypes=dtypes,
        )

        resp: FindResponse = self._invoke(
            self._stub.find, req, wait_for_ready=True
        )
        if to_pandas:
            df = self._to_pd_dataframe(
                buffer=resp.buffer,
                index_columns=index_columns,
                columns=columns,
                dtypes=dtypes,
            )
        elif to_polars:
            df = self._to_pl_dataframe(buffer=resp.buffer, columns=columns)
        elif to_arrow:
            df = self._to_arrow_table(buffer=resp.buffer, columns=columns)
        else:
            df = self._to_arrow_table(buffer=resp.buffer, columns=columns)

        if enable_profile:
            profile = {
                "duration": {
                    "query": resp.profile.query_duration_us,
                    "serialization": resp.profile.serialization_duration_us,
                    "unit": "us",
                }
            }
            del resp
            return df, profile
        else:
            del resp
            return df

    def find_batch(
        self,
        requests,
        to_pandas=True,
        to_polars=False,
        to_arrow=False,
        enable_profile=False,
    ) -> (
        list[pd.DataFrame]
        | list[pa.Table]
        | tuple[list[pd.DataFrame] | list[pa.Table], list[dict]]
    ):
        if not requests:
            return []

        if to_polars or to_arrow:
            to_pandas = False

        batch_items = []
        for req in requests:
            query = _to_json(req.query)
            item = FindRequest(
                query=Query(collection_name=req.collection, query=query),
                limit=req.limit,
                index_columns=req.index_columns,
                columns=req.columns,
                dtypes=req.dtypes,
            )
            batch_items.append(item)
        batch_req = FindBatchRequest(requests=batch_items)

        dfs = []
        profiles = []
        resp: FindBatchResponse = self._invoke(
            self._stub.find_batch, batch_req, wait_for_ready=True
        )
        for req, response in zip(requests, resp.responses):  # type: ignore
            if to_pandas:
                df = self._to_pd_dataframe(
                    buffer=response.buffer,
                    index_columns=req.index_columns,
                    columns=req.columns,
                    dtypes=req.dtypes,
                )
            elif to_polars:
                df = self._to_pl_dataframe(
                    buffer=response.buffer, columns=req.columns
                )
            elif to_arrow:
                df = self._to_arrow_table(
                    buffer=response.buffer, columns=req.columns
                )
            else:
                df = self._to_arrow_table(
                    buffer=response.buffer, columns=req.columns
                )
            dfs.append(df)
            if enable_profile:
                profile = {
                    "duration": {
                        "query": response.profile.query_duration_us,
                        "serialization": (
                            response.profile.serialization_duration_us
                        ),
                        "unit": "us",
                    }
                }
                profiles.append(profile)
        del resp

        if enable_profile:
            return dfs, profiles
        else:
            return dfs

    def insert(self, collection, docs) -> None:
        if not isinstance(docs, list):
            docs = [docs]

        items = []
        for doc in docs:
            doc = _to_json(doc)
            item = Query(collection_name=collection, query=doc)
            items.append(item)

        req = InsertRequest(requests=items)
        self._invoke(self._stub.insert, req, wait_for_ready=True)

    def update(self, collection, filter_, updates) -> None:
        filter_ = _to_json(filter_)
        updates = _to_json(updates)
        req = UpdateRequest(
            collection_name=collection, filter=filter_, updates=updates
        )

        self._invoke(self._stub.update, req, wait_for_ready=True)

    def remove(self, collection, docs) -> None:
        if not isinstance(docs, list):
            docs = [docs]

        items = []
        for doc in docs:
            doc = _to_json(doc)
            item = Query(collection_name=collection, query=doc)
            items.append(item)

        req = RemoveRequest(requests=items)

        self._invoke(self._stub.remove, req, wait_for_ready=True)

    def get_collection(self, collection) -> t.Dict[str, t.Any]:
        req = GetCollectionRequest(collection_name=collection)
        resp: GetCollectionResponse = self._invoke(
            self._stub.get_collection, req, wait_for_ready=True
        )

        return {
            "success": resp.status == 0,
            "message": resp.message,
            "data": [
                {
                    "collection_name": resp.collection.collection_name,
                    "primary_key": {
                        "index_id": resp.collection.primary_key.index_id,
                        "index_name": resp.collection.primary_key.index_name,
                        "fields": list(resp.collection.primary_key.fields),
                        "unique": resp.collection.primary_key.unique,
                        "index_type": IndexType.Name(
                            resp.collection.primary_key.index_type
                        ),
                        "status": IndexStatus.Name(
                            resp.collection.primary_key.status
                        ),
                        "options": json.loads(
                            resp.collection.primary_key.options.json or "{}"
                        ),
                    },
                    "secondary_keys": [
                        {
                            "index_id": secondary_key.index_id,
                            "index_name": secondary_key.index_name,
                            "fields": list(secondary_key.fields),
                            "unique": secondary_key.unique,
                            "index_type": IndexType.Name(
                                secondary_key.index_type
                            ),
                            "status": IndexStatus.Name(secondary_key.status),
                            "options": json.loads(
                                secondary_key.options.json or "{}"
                            ),
                        }
                        for secondary_key in resp.collection.secondary_keys
                    ],
                }
            ],
        }

    def list_collections(self) -> t.List[str]:
        req = ListCollectionsRequest()

        collection_names = []
        resp: ListCollectionsResponse = self._invoke(
            self._stub.list_collections, req, wait_for_ready=True
        )
        for name in resp.collection_names:
            collection_names.append(name)

        return collection_names

    def truncate_collection(self, collection) -> None:
        req = TruncateCollectionRequest(collection_name=collection)
        self._invoke(self._stub.truncate_collection, req, wait_for_ready=True)

    def create_index(
        self, collection, index_name, fields, unique, index_type, options
    ) -> None:
        if options is not None:
            options = _to_json(options)

        index_desc = IndexDesc(
            index_id=0,
            index_name=index_name,
            fields=fields,
            unique=unique,
            index_type=index_type,
            status=IndexStatus.kEnabled,
            options=options,
        )
        req = CreateIndexRequest(
            collection_name=collection, index_desc=index_desc
        )
        self._invoke(self._stub.create_index, req, wait_for_ready=True)

    def drop_index(self, collection, index_name) -> None:
        req = DropIndexRequest(
            collection_name=collection, index_name=index_name
        )
        self._invoke(self._stub.drop_index, req, wait_for_ready=True)

    def get_index(
        self, collection, index_name
    ) -> t.List[t.Dict[str, t.Union[int, str]]]:
        req = GetIndexRequest(collection_name=collection, index_name=index_name)

        index_infos = []
        resp: IndexDesc = self._invoke(
            self._stub.get_index, req, wait_for_ready=True
        )
        index_desc = resp.index_desc
        index_infos.append(
            {
                "index_id": index_desc.index_id,
                "index_name": index_desc.index_name,
                "fields": list(index_desc.fields),
                "unique": index_desc.unique,
                "index_type": index_desc.index_type,
                "status": index_desc.status,
                "options": str(index_desc.options),
            }
        )

        return index_infos

    def empty(self, collection, query, dtypes=None) -> bool:
        df = self.find(collection, query, dtypes=dtypes, limit=1)

        return len(df) == 0

    def _invoke(self, func, *args, **kwargs):
        retry = 0
        backoff = 0.1
        resp = None
        if self._timeout:
            kwargs["timeout"] = self._timeout
        while retry < self._max_retry_count:
            try:
                resp = func(*args, **kwargs)
            except grpc.RpcError as rpc_error:
                if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:  # type: ignore
                    retry += 1
                    time.sleep(backoff)
                    backoff *= 2
                else:
                    raise
            else:
                break

        return resp

    def _to_pd_dataframe(
        self, buffer, index_columns=None, columns=None, dtypes=None
    ) -> pd.DataFrame:
        if len(buffer) > 0:
            table = self._to_arrow_table(buffer)
            df = table.to_pandas(split_blocks=True, self_destruct=True)
            del table
        else:
            df = pd.DataFrame(columns=columns)
            if index_columns:
                try:
                    df = df.set_index(index_columns)
                except KeyError:
                    pass

        if dtypes:
            for column, type_ in dtypes.items():
                if type_ == "json" and column in df:
                    df[column] = df[column].apply(json.loads)

        return df

    def _to_pl_dataframe(
        self, buffer, columns=None, dtypes=None
    ) -> pl.DataFrame:
        if len(buffer) > 0:
            df = pl.read_parquet(io.BytesIO(buffer), columns=columns)
        else:
            df = pl.DataFrame(schema=columns)

        if dtypes:
            for column, type_ in dtypes.items():
                if type_ == "json" and column in df:
                    df[column] = df[column].apply(json.loads)

        return df

    def _to_arrow_table(self, buffer, columns=None) -> pa.Table:
        buffer_arrow = pa.py_buffer(buffer)
        table = pq.read_table(buffer_arrow, columns=columns)

        return table
