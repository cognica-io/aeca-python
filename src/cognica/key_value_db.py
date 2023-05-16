#
# Cognica
#
# Copyright (c) 2023 Cognica, Inc.
#

# pylint: disable=no-member,broad-exception-caught
# pylint: disable=missing-class-docstring,missing-function-docstring

import time
import typing as t

import grpc

from cognica.channel import Channel
from cognica.protobuf import key_value_db_pb2, key_value_db_pb2_grpc


messages: t.TypeAlias = key_value_db_pb2  # type: ignore

KeyValueDBServiceStub = key_value_db_pb2_grpc.KeyValueDBServiceStub
KeyspaceManagerServiceStub = key_value_db_pb2_grpc.KeyspaceManagerServiceStub

StatusType: t.TypeAlias = messages.StatusType  # type: ignore
Response: t.TypeAlias = messages.Response  # type: ignore
PutRequest: t.TypeAlias = messages.PutRequest  # type: ignore
PutResponse: t.TypeAlias = messages.PutResponse  # type: ignore
RemoveRequest: t.TypeAlias = messages.RemoveRequest  # type: ignore
RemoveResponse: t.TypeAlias = messages.RemoveResponse  # type: ignore
GetRequest: t.TypeAlias = messages.GetRequest  # type: ignore
GetResponse: t.TypeAlias = messages.GetResponse  # type: ignore
MultiGetRequest: t.TypeAlias = messages.MultiGetRequest  # type: ignore
MultiGetResponse: t.TypeAlias = messages.MultiGetResponse  # type: ignore
BatchedPutRequest: t.TypeAlias = messages.BatchedPutRequest  # type: ignore
BatchedPutResponse: t.TypeAlias = messages.BatchedPutResponse  # type: ignore
BatchedRemoveRequest: t.TypeAlias = messages.BatchedRemoveRequest  # type: ignore
BatchedRemoveResponse: t.TypeAlias = (
    messages.BatchedRemoveResponse  # type: ignore
)
BatchedGetRequest: t.TypeAlias = messages.BatchedGetRequest  # type: ignore
BatchedGetResponse: t.TypeAlias = messages.BatchedGetResponse  # type: ignore

CreateKeyspaceRequest: t.TypeAlias = (
    messages.CreateKeyspaceRequest  # type: ignore
)
CreateKeyspaceResponse: t.TypeAlias = (
    messages.CreateKeyspaceResponse  # type: ignore
)
DropKeyspaceRequest: t.TypeAlias = messages.DropKeyspaceRequest  # type: ignore
DropKeyspaceResponse: t.TypeAlias = (
    messages.DropKeyspaceResponse  # type: ignore
)
TruncateKeyspaceRequest: t.TypeAlias = (
    messages.TruncateKeyspaceRequest  # type: ignore
)
TruncateKeyspaceResponse: t.TypeAlias = (
    messages.TruncateKeyspaceResponse  # type: ignore
)
ListKeyspacesRequest: t.TypeAlias = (
    messages.ListKeyspacesRequest  # type: ignore
)
ListKeyspacesResponse: t.TypeAlias = (
    messages.ListKeyspacesResponse  # type: ignore
)


def _create_stub(stub: t.Callable, channel: Channel):
    stub = stub(channel.channel)

    return stub


class KeyValueDB:
    def __init__(self, channel: Channel, timeout: int | None = None):
        """
        parameter 'timeout' is in seconds
        """

        self._max_retry_count = 5
        self._stub = _create_stub(KeyValueDBServiceStub, channel)
        self._timeout = timeout

    def put(
        self,
        keyspace_name: str,
        key: t.Union[bytes, str],
        value: t.Union[bytes, str],
        ttl: int = 0,
        create_if_missing: bool = True,
    ) -> bool:
        if isinstance(key, str):
            key = key.encode("utf-8")
        if isinstance(value, str):
            value = value.encode("utf-8")

        req = PutRequest(
            keyspace_name=keyspace_name,
            key=key,
            value=value,
            ttl=ttl,
            create_if_missing=create_if_missing,
        )
        try:
            resp: PutResponse = self._invoke(
                self._stub.put, req, wait_for_ready=True
            )
        except Exception:
            return False

        return resp.response.status == StatusType.kOK

    def remove(self, keyspace_name: str, key: t.Union[bytes, str]) -> bool:
        if isinstance(key, str):
            key = key.encode("utf-8")

        req = RemoveRequest(keyspace_name=keyspace_name, key=key)
        try:
            resp: RemoveResponse = self._invoke(
                self._stub.remove, req, wait_for_ready=True
            )
        except Exception:
            return False

        return resp.response.status == StatusType.kOK

    def get(
        self, keyspace_name: str, key: t.Union[bytes, str]
    ) -> t.Optional[bytes]:
        if isinstance(key, str):
            key = key.encode("utf-8")

        req = GetRequest(keyspace_name=keyspace_name, key=key)
        try:
            resp: GetResponse = self._invoke(
                self._stub.get, req, wait_for_ready=True
            )
        except Exception:
            return None

        if resp.response.status != StatusType.kOK:
            return None

        return resp.value

    def mget(
        self, keyspace_name: str, keys: t.List[t.Union[bytes, str]]
    ) -> t.List[t.Optional[bytes]]:
        keys_encoded = []
        for key in keys:
            if isinstance(key, str):
                keys_encoded.append(key.encode("utf-8"))
            elif isinstance(key, bytes):
                keys_encoded.append(key)
            else:
                raise TypeError("key must be either string or bytes type.")

        req = MultiGetRequest(keyspace_name=keyspace_name, keys=keys_encoded)
        try:
            resp: MultiGetResponse = self._invoke(
                self._stub.mget, req, wait_for_ready=True
            )
        except Exception:
            return [None] * len(keys)

        values = []
        for response, value in zip(resp.responses, resp.values):
            if response.status == StatusType.kOK:
                values.append(value)
            else:
                values.append(None)

        return values

    def put_batch(
        self,
        keyspace_name: str,
        keys: t.List[t.Union[bytes, str]],
        values: t.List[t.Union[bytes, str]],
        ttls: t.List[int],
        create_if_missing: bool = True,
    ) -> t.List[bool]:
        keys_encoded = []
        values_encoded = []
        for key, value in zip(keys, values):
            if isinstance(key, str):
                key = key.encode("utf-8")
            if isinstance(key, str):
                value = value.encode("utf-8")  # type: ignore
            keys_encoded.append(key)
            values_encoded.append(value)

        req = BatchedPutRequest(
            keyspace_name=keyspace_name,
            keys=keys_encoded,
            values=values_encoded,
            ttls=ttls,
            create_if_missing=create_if_missing,
        )
        try:
            resp: BatchedPutResponse = self._invoke(
                self._stub.put_batch, req, wait_for_ready=True
            )
        except Exception:
            return [False] * len(keys)

        statuses = []
        for resp in resp.responses:
            if resp.status == StatusType.kOK:
                statuses.append(True)
            else:
                statuses.append(False)

        return statuses

    def remove_batch(
        self, keyspace_name: str, keys: t.List[t.Union[bytes, str]]
    ) -> t.List[bool]:
        keys_encoded = []
        for key in keys:
            if isinstance(key, str):
                key = key.encode("utf-8")
            keys_encoded.append(key)

        req = BatchedRemoveRequest(
            keyspace_name=keyspace_name, keys=keys_encoded
        )
        try:
            resp: BatchedRemoveResponse = self._invoke(
                self._stub.remove_batch, req, wait_for_ready=True
            )
        except Exception:
            return [False] * len(keys)

        statuses = []
        for resp in resp.responses:
            if resp.status == StatusType.kOK:
                statuses.append(True)
            else:
                statuses.append(False)

        return statuses

    def get_batch(
        self, keyspace_name: str, keys: t.List[t.Union[bytes, str]]
    ) -> t.List[t.Optional[bytes]]:
        keys_encoded = []
        for key in keys:
            if isinstance(key, str):
                key = key.encode("utf-8")
            keys_encoded.append(key)

        req = BatchedGetRequest(keyspace_name=keyspace_name, keys=keys_encoded)
        try:
            resp: BatchedGetResponse = self._invoke(
                self._stub.get_batch, req, wait_for_ready=True
            )
        except Exception:
            return [None] * len(keys)

        values = []
        for resp, value in zip(resp.responses, resp.values):
            if resp.response.status == StatusType.kOK:
                values.append(value)
            else:
                values.append(None)

        return values

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


class KeyspaceManager:
    def __init__(self, channel: Channel, timeout: int | None = None):
        self._max_retry_count = 5
        self._stub = _create_stub(KeyspaceManagerServiceStub, channel)
        self._timeout = timeout

    def create_keyspace(self, keyspace_name: str) -> bool:
        req = CreateKeyspaceRequest(keyspace_name=keyspace_name)
        resp: CreateKeyspaceResponse = self._invoke(
            self._stub.create_keyspace, req, wait_for_ready=True
        )

        return resp.response.status == StatusType.kOK

    def drop_keyspace(self, keyspace_name: str) -> bool:
        req = DropKeyspaceRequest(keyspace_name=keyspace_name)
        resp: DropKeyspaceResponse = self._invoke(
            self._stub.drop_keyspace, req, wait_for_ready=True
        )

        return resp.response.status == StatusType.kOK

    def truncate_keyspace(self, keyspace_name: str) -> bool:
        req = TruncateKeyspaceRequest(keyspace_name=keyspace_name)
        resp: TruncateKeyspaceResponse = self._invoke(
            self._stub.truncate_keyspace, req, wait_for_ready=True
        )

        return resp.response.status == StatusType.kOK

    def list_keyspaces(self) -> t.List[str]:
        req = ListKeyspacesRequest()
        resp: ListKeyspacesResponse = self._invoke(
            self._stub.list_keyspaces, req, wait_for_ready=True
        )

        if resp.response.status != StatusType.kOK:
            return []

        return resp.keyspace_names

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
