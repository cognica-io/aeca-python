#
# Aeca
#
# Copyright (c) 2024 Aeca, Inc.
#

# pylint: disable=no-member,missing-module-docstring,missing-class-docstring,missing-function-docstring
# pylint: disable=invalid-name

from __future__ import annotations

import time
import typing as t

import grpc

from aeca.channel import Channel
from aeca.protobuf import (
    system_metrics_pb2,
    system_metrics_pb2_grpc,
)


messages: t.TypeAlias = system_metrics_pb2  # type: ignore

SystemMetricsServiceStub = system_metrics_pb2_grpc.SystemMetricsServiceStub

GetSystemMetricsRequest: t.TypeAlias = (
    messages.GetSystemMetricsRequest  # type: ignore
)
GetSystemMetricsResponse: t.TypeAlias = (
    messages.GetSystemMetricsResponse  # type: ignore
)


def _create_stub(
    stub: t.Callable, channel: Channel
) -> SystemMetricsServiceStub:
    return stub(channel.channel)


class SystemMetrics:
    def __init__(self, channel: Channel, timeout: int | None = None):
        self._max_retry_count = 5
        self._stub = _create_stub(SystemMetricsServiceStub, channel)
        self._timeout = timeout

    def get_snapshot(
        self,
        client_name: str | None = None,
        version: str | None = None,
    ) -> str:
        req = GetSystemMetricsRequest(
            client_name=client_name,
            version=version,
        )
        resp: GetSystemMetricsResponse = self._invoke(
            self._stub.get_snapshot, req, wait_for_ready=True
        )

        return resp.snapshot

    def _invoke(self, func: t.Callable, *args, **kwargs) -> t.Any:
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
