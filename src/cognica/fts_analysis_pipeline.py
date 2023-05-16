#
# Cognica
#
# Copyright (c) 2023 Cognica, Inc.
#

# pylint: disable=no-member,missing-class-docstring,missing-function-docstring

import time
import typing as t

import grpc

from cognica.channel import Channel
from cognica.protobuf import (
    fts_analysis_pipeline_pb2,
    fts_analysis_pipeline_pb2_grpc,
)


messages: t.TypeAlias = fts_analysis_pipeline_pb2  # type: ignore

FTSAnalysisPipelineServiceStub = (
    fts_analysis_pipeline_pb2_grpc.FTSAnalysisPipelineServiceStub
)

PipelineExecutionRequest: t.TypeAlias = (
    messages.PipelineExecutionRequest  # type: ignore
)
PipelineExecutionResponse: t.TypeAlias = (
    messages.PipelineExecutionResponse  # type: ignore
)
AdhocPipelineExecutionRequest: t.TypeAlias = (
    messages.AdhocPipelineExecutionRequest  # type: ignore
)
AdhocPipelineExecutionResponse: t.TypeAlias = (
    messages.AdhocPipelineExecutionResponse  # type: ignore
)


def _create_stub(stub: t.Callable, channel: Channel):
    stub = stub(channel.channel)

    return stub


class FTSAnalysisPipeline:
    def __init__(self, channel: Channel, timeout: int | None = None):
        self._max_retry_count = 5
        self._stub = _create_stub(FTSAnalysisPipelineServiceStub, channel)
        self._timeout = timeout

    def execute(
        self,
        collection_name: str,
        index_name: str,
        query: str,
        field_names: t.Optional[t.List[str]] = None,
    ) -> str:
        req = PipelineExecutionRequest(
            collection_name=collection_name,
            index_name=index_name,
            field_names=field_names,
            query=query,
        )
        resp: PipelineExecutionResponse = self._invoke(
            self._stub.execute, req, wait_for_ready=True
        )

        return resp.result

    def execute_adhoc(
        self,
        pipeline_def: str,
        query: str,
        field_names: t.Optional[t.List[str]] = None,
    ) -> str:
        req = AdhocPipelineExecutionRequest(
            pipeline_def=pipeline_def, field_names=field_names, query=query
        )
        resp: AdhocPipelineExecutionResponse = self._invoke(
            self._stub.execute_adhoc, req, wait_for_ready=True
        )

        return resp.result

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
