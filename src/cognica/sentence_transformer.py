#
# Cognica
#
# Copyright (c) 2023 Cognica, Inc.
#

# pylint: disable=no-member,broad-exception-caught
# pylint: disable=missing-class-docstring,missing-function-docstring

import io
import time
import typing as t

import grpc
import numpy as np
from PIL import Image

from cognica.channel import Channel
from cognica.protobuf import (
    sentence_transformer_pb2,
    sentence_transformer_pb2_grpc,
)


messages: t.TypeAlias = sentence_transformer_pb2  # type: ignore

SentenceTransformerServiceStub = (
    sentence_transformer_pb2_grpc.SentenceTransformerServiceStub
)
CrossEncoderServiceStub = sentence_transformer_pb2_grpc.CrossEncoderServiceStub
CLIPEncoderServiceStub = sentence_transformer_pb2_grpc.CLIPEncoderServiceStub
QAEncoderServiceStub = sentence_transformer_pb2_grpc.QAEncoderServiceStub

StatusType: t.TypeAlias = messages.StatusType  # type: ignore
Tensor: t.TypeAlias = messages.Tensor  # type: ignore
SentenceEncoderRequest: t.TypeAlias = (
    messages.SentenceEncoderRequest  # type: ignore
)
SentenceEncoderResponse: t.TypeAlias = (
    messages.SentenceEncoderResponse  # type: ignore
)
SentencePair: t.TypeAlias = messages.SentencePair  # type: ignore
CrossEncoderRequest: t.TypeAlias = messages.CrossEncoderRequest  # type: ignore
CrossEncoderResponse: t.TypeAlias = (
    messages.CrossEncoderResponse  # type: ignore
)
CLIPEncoderRequest: t.TypeAlias = messages.CLIPEncoderRequest  # type: ignore
CLIPEncoderResponse: t.TypeAlias = messages.CLIPEncoderResponse  # type: ignore
QAEncoderRequest: t.TypeAlias = messages.QAEncoderRequest  # type: ignore
QAEncoderResponse: t.TypeAlias = messages.QAEncoderResponse  # type: ignore


def _create_stub(stub: t.Callable, channel: Channel):
    return stub(channel.channel)


class SentenceTransformerEncoder:
    def __init__(
        self, channel: Channel, model_name: str, timeout: int | None = None
    ):
        self._model_name = model_name
        self._max_retry_count = 5
        self._stub = _create_stub(SentenceTransformerServiceStub, channel)
        self._timeout = timeout

    def encode(self, sentences: t.List[str] | str) -> t.Optional[np.ndarray]:
        if not isinstance(sentences, list):
            sentences = [sentences]

        req = SentenceEncoderRequest(
            model_name=self._model_name, sentences=sentences
        )
        try:
            resp: SentenceEncoderResponse = self._invoke(
                self._stub.encode, req, wait_for_ready=True
            )
        except Exception:
            return None

        if resp.status != StatusType.kOK:
            return None

        data = []
        for tensor in resp.tensors:
            data.append(tensor.data)

        return np.array(data, dtype=np.float32)

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


class SentenceTransformerCrossEncoder:
    def __init__(
        self, channel: Channel, model_name: str, timeout: int | None = None
    ):
        self._model_name = model_name
        self._max_retry_count = 5
        self._stub = _create_stub(CrossEncoderServiceStub, channel)
        self._timeout = timeout

    def predict(
        self, sentence_pairs: t.List[t.Tuple[str, str]]
    ) -> t.Optional[np.ndarray]:
        if not isinstance(sentence_pairs, list):
            sentence_pairs = [sentence_pairs]

        sentences = []
        for s1, s2 in sentence_pairs:
            pair = SentencePair(sentence1=s1, sentence2=s2)
            sentences.append(pair)
        req = CrossEncoderRequest(
            model_name=self._model_name, sentences=sentences
        )
        try:
            resp: CrossEncoderResponse = self._invoke(
                self._stub.predict, req, wait_for_ready=True
            )
        except Exception:
            return None

        if resp.status != StatusType.kOK:
            return None

        return np.array(resp.scores, dtype=np.float32)

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


class SentenceTransformerCLIPEncoder:
    def __init__(
        self, channel: Channel, model_name: str, timeout: int | None = None
    ):
        self._model_name = model_name
        self._max_retry_count = 5
        self._stub = _create_stub(CLIPEncoderServiceStub, channel)
        self._timeout = timeout

    def encode(
        self, inputs: t.List[t.Union[bytes, Image.Image]]
    ) -> t.Optional[np.ndarray]:
        if not isinstance(inputs, list):
            inputs = [inputs]

        new_inputs = []
        for s in inputs:
            if isinstance(s, Image.Image):
                buffer = io.BytesIO()
                s.save(buffer, format="png")
                new_inputs.append(buffer.getvalue())
            else:
                new_inputs.append(s)

        req = CLIPEncoderRequest(model_name=self._model_name, inputs=new_inputs)
        try:
            resp: CLIPEncoderResponse = self._invoke(
                self._stub.encode, req, wait_for_ready=True
            )
        except Exception:
            return None

        if resp.status != StatusType.kOK:
            return None

        data = []
        for tensor in resp.tensors:
            data.append(tensor.data)

        return np.array(data, dtype=np.float32)

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


class SentenceTransformerQAEncoder:
    def __init__(
        self, channel: Channel, model_name: str, timeout: int | None = None
    ):
        self._model_name = model_name
        self._max_retry_count = 5
        self._stub = _create_stub(QAEncoderServiceStub, channel)
        self._timeout = timeout

    def predict(
        self,
        questions: t.Union[str, t.List[str]],
        contexts: t.Union[str, t.List[str]],
        top_k: int = 1,
    ) -> t.Optional[t.List[t.List[t.Dict[str, t.Any]]]]:
        if not isinstance(questions, list):
            questions = [questions]
        if not isinstance(contexts, list):
            contexts = [contexts]

        req = QAEncoderRequest(
            model_name=self._model_name,
            questions=questions,
            contexts=contexts,
            top_k=top_k,
        )
        try:
            resp: QAEncoderResponse = self._invoke(
                self._stub.predict, req, wait_for_ready=True
            )
        except Exception:
            return None

        if resp.status != StatusType.kOK:
            return None

        outputs: t.List[t.List[t.Dict[str, t.Any]]] = []
        for answer in resp.answers:
            candidates: t.List[t.Dict[str, t.Any]] = []
            for candidate in answer.candidates:
                candidates.append(
                    {
                        "score": candidate.score,
                        "begin": candidate.begin,
                        "end": candidate.end,
                        "answer": candidate.answer,
                    }
                )
            outputs.append(candidates)

        return outputs

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
