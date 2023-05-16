#
# Cognica
#
# Copyright (c) 2023 Cognica, Inc.
#

# pylint: disable=invalid-name
# pylint: disable=missing-class-docstring,missing-function-docstring

import grpc


_CHANNEL_OPTIONS = [
    ("grpc.max_concurrent_streams", 4),
    ("grpc.max_send_message_length", -1),
    ("grpc.max_receive_message_length", -1),
    ("grpc.http2.max_frame_size", 10 * 1024 * 1024),  # 10MB
]


class Channel:
    def __init__(
        self,
        host: str,
        port: int,
        options: list[tuple[str, int]] | None = None,
        use_ssl: bool = False,
    ):
        self._host = host
        self._port = port
        if options is None:
            self._options = _CHANNEL_OPTIONS
        else:
            self._options = options
        self._use_ssl = use_ssl

        self._channel = self._create_channel()

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def options(self) -> list[tuple[str, int]]:
        return self._options

    @property
    def use_ssl(self) -> bool:
        return self._use_ssl

    @property
    def channel(self) -> grpc.Channel:
        return self._channel

    def _create_channel(self) -> grpc.Channel:
        if self._use_ssl:
            ChannelFactory = grpc.secure_channel
            params = {"credentials": grpc.ssl_channel_credentials()}
        else:
            ChannelFactory = grpc.insecure_channel
            params = {}

        channel = ChannelFactory(
            f"{self._host}:{self._port}",
            options=self._options,
            compression=grpc.Compression.Gzip,
            **params,
        )

        return channel

    def __enter__(self) -> grpc.Channel:
        return self._channel

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._channel.close()
