# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cognica.protobuf.document_db_pb2 as document__db__pb2


class DocumentDBServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.find = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/find',
                request_serializer=document__db__pb2.FindRequest.SerializeToString,
                response_deserializer=document__db__pb2.FindResponse.FromString,
                )
        self.find_batch = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/find_batch',
                request_serializer=document__db__pb2.FindBatchRequest.SerializeToString,
                response_deserializer=document__db__pb2.FindBatchResponse.FromString,
                )
        self.count = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/count',
                request_serializer=document__db__pb2.CountRequest.SerializeToString,
                response_deserializer=document__db__pb2.CountResponse.FromString,
                )
        self.contains = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/contains',
                request_serializer=document__db__pb2.ContainsRequest.SerializeToString,
                response_deserializer=document__db__pb2.ContainsResponse.FromString,
                )
        self.insert = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/insert',
                request_serializer=document__db__pb2.InsertRequest.SerializeToString,
                response_deserializer=document__db__pb2.InsertResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/update',
                request_serializer=document__db__pb2.UpdateRequest.SerializeToString,
                response_deserializer=document__db__pb2.UpdateResponse.FromString,
                )
        self.remove = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/remove',
                request_serializer=document__db__pb2.RemoveRequest.SerializeToString,
                response_deserializer=document__db__pb2.RemoveResponse.FromString,
                )
        self.explain = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/explain',
                request_serializer=document__db__pb2.ExplainRequest.SerializeToString,
                response_deserializer=document__db__pb2.ExplainResponse.FromString,
                )
        self.create_collection = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/create_collection',
                request_serializer=document__db__pb2.CreateCollectionRequest.SerializeToString,
                response_deserializer=document__db__pb2.CreateCollectionResponse.FromString,
                )
        self.drop_collection = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/drop_collection',
                request_serializer=document__db__pb2.DropCollectionRequest.SerializeToString,
                response_deserializer=document__db__pb2.DropCollectionResponse.FromString,
                )
        self.rename_collection = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/rename_collection',
                request_serializer=document__db__pb2.RenameCollectionRequest.SerializeToString,
                response_deserializer=document__db__pb2.RenameCollectionResponse.FromString,
                )
        self.get_collection = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/get_collection',
                request_serializer=document__db__pb2.GetCollectionRequest.SerializeToString,
                response_deserializer=document__db__pb2.GetCollectionResponse.FromString,
                )
        self.get_collections = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/get_collections',
                request_serializer=document__db__pb2.GetCollectionsRequest.SerializeToString,
                response_deserializer=document__db__pb2.GetCollectionsResponse.FromString,
                )
        self.list_collections = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/list_collections',
                request_serializer=document__db__pb2.ListCollectionsRequest.SerializeToString,
                response_deserializer=document__db__pb2.ListCollectionsResponse.FromString,
                )
        self.truncate_collection = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/truncate_collection',
                request_serializer=document__db__pb2.TruncateCollectionRequest.SerializeToString,
                response_deserializer=document__db__pb2.TruncateCollectionResponse.FromString,
                )
        self.create_index = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/create_index',
                request_serializer=document__db__pb2.CreateIndexRequest.SerializeToString,
                response_deserializer=document__db__pb2.CreateIndexResponse.FromString,
                )
        self.drop_index = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/drop_index',
                request_serializer=document__db__pb2.DropIndexRequest.SerializeToString,
                response_deserializer=document__db__pb2.DropIndexResponse.FromString,
                )
        self.rename_index = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/rename_index',
                request_serializer=document__db__pb2.RenameIndexRequest.SerializeToString,
                response_deserializer=document__db__pb2.RenameIndexResponse.FromString,
                )
        self.get_index = channel.unary_unary(
                '/cognica.rpc.db.document.DocumentDBService/get_index',
                request_serializer=document__db__pb2.GetIndexRequest.SerializeToString,
                response_deserializer=document__db__pb2.GetIndexResponse.FromString,
                )


class DocumentDBServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def find_batch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def contains(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def explain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_collection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def drop_collection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rename_collection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_collection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_collections(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list_collections(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def truncate_collection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def drop_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rename_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DocumentDBServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'find': grpc.unary_unary_rpc_method_handler(
                    servicer.find,
                    request_deserializer=document__db__pb2.FindRequest.FromString,
                    response_serializer=document__db__pb2.FindResponse.SerializeToString,
            ),
            'find_batch': grpc.unary_unary_rpc_method_handler(
                    servicer.find_batch,
                    request_deserializer=document__db__pb2.FindBatchRequest.FromString,
                    response_serializer=document__db__pb2.FindBatchResponse.SerializeToString,
            ),
            'count': grpc.unary_unary_rpc_method_handler(
                    servicer.count,
                    request_deserializer=document__db__pb2.CountRequest.FromString,
                    response_serializer=document__db__pb2.CountResponse.SerializeToString,
            ),
            'contains': grpc.unary_unary_rpc_method_handler(
                    servicer.contains,
                    request_deserializer=document__db__pb2.ContainsRequest.FromString,
                    response_serializer=document__db__pb2.ContainsResponse.SerializeToString,
            ),
            'insert': grpc.unary_unary_rpc_method_handler(
                    servicer.insert,
                    request_deserializer=document__db__pb2.InsertRequest.FromString,
                    response_serializer=document__db__pb2.InsertResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=document__db__pb2.UpdateRequest.FromString,
                    response_serializer=document__db__pb2.UpdateResponse.SerializeToString,
            ),
            'remove': grpc.unary_unary_rpc_method_handler(
                    servicer.remove,
                    request_deserializer=document__db__pb2.RemoveRequest.FromString,
                    response_serializer=document__db__pb2.RemoveResponse.SerializeToString,
            ),
            'explain': grpc.unary_unary_rpc_method_handler(
                    servicer.explain,
                    request_deserializer=document__db__pb2.ExplainRequest.FromString,
                    response_serializer=document__db__pb2.ExplainResponse.SerializeToString,
            ),
            'create_collection': grpc.unary_unary_rpc_method_handler(
                    servicer.create_collection,
                    request_deserializer=document__db__pb2.CreateCollectionRequest.FromString,
                    response_serializer=document__db__pb2.CreateCollectionResponse.SerializeToString,
            ),
            'drop_collection': grpc.unary_unary_rpc_method_handler(
                    servicer.drop_collection,
                    request_deserializer=document__db__pb2.DropCollectionRequest.FromString,
                    response_serializer=document__db__pb2.DropCollectionResponse.SerializeToString,
            ),
            'rename_collection': grpc.unary_unary_rpc_method_handler(
                    servicer.rename_collection,
                    request_deserializer=document__db__pb2.RenameCollectionRequest.FromString,
                    response_serializer=document__db__pb2.RenameCollectionResponse.SerializeToString,
            ),
            'get_collection': grpc.unary_unary_rpc_method_handler(
                    servicer.get_collection,
                    request_deserializer=document__db__pb2.GetCollectionRequest.FromString,
                    response_serializer=document__db__pb2.GetCollectionResponse.SerializeToString,
            ),
            'get_collections': grpc.unary_unary_rpc_method_handler(
                    servicer.get_collections,
                    request_deserializer=document__db__pb2.GetCollectionsRequest.FromString,
                    response_serializer=document__db__pb2.GetCollectionsResponse.SerializeToString,
            ),
            'list_collections': grpc.unary_unary_rpc_method_handler(
                    servicer.list_collections,
                    request_deserializer=document__db__pb2.ListCollectionsRequest.FromString,
                    response_serializer=document__db__pb2.ListCollectionsResponse.SerializeToString,
            ),
            'truncate_collection': grpc.unary_unary_rpc_method_handler(
                    servicer.truncate_collection,
                    request_deserializer=document__db__pb2.TruncateCollectionRequest.FromString,
                    response_serializer=document__db__pb2.TruncateCollectionResponse.SerializeToString,
            ),
            'create_index': grpc.unary_unary_rpc_method_handler(
                    servicer.create_index,
                    request_deserializer=document__db__pb2.CreateIndexRequest.FromString,
                    response_serializer=document__db__pb2.CreateIndexResponse.SerializeToString,
            ),
            'drop_index': grpc.unary_unary_rpc_method_handler(
                    servicer.drop_index,
                    request_deserializer=document__db__pb2.DropIndexRequest.FromString,
                    response_serializer=document__db__pb2.DropIndexResponse.SerializeToString,
            ),
            'rename_index': grpc.unary_unary_rpc_method_handler(
                    servicer.rename_index,
                    request_deserializer=document__db__pb2.RenameIndexRequest.FromString,
                    response_serializer=document__db__pb2.RenameIndexResponse.SerializeToString,
            ),
            'get_index': grpc.unary_unary_rpc_method_handler(
                    servicer.get_index,
                    request_deserializer=document__db__pb2.GetIndexRequest.FromString,
                    response_serializer=document__db__pb2.GetIndexResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cognica.rpc.db.document.DocumentDBService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DocumentDBService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/find',
            document__db__pb2.FindRequest.SerializeToString,
            document__db__pb2.FindResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def find_batch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/find_batch',
            document__db__pb2.FindBatchRequest.SerializeToString,
            document__db__pb2.FindBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/count',
            document__db__pb2.CountRequest.SerializeToString,
            document__db__pb2.CountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def contains(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/contains',
            document__db__pb2.ContainsRequest.SerializeToString,
            document__db__pb2.ContainsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/insert',
            document__db__pb2.InsertRequest.SerializeToString,
            document__db__pb2.InsertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/update',
            document__db__pb2.UpdateRequest.SerializeToString,
            document__db__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/remove',
            document__db__pb2.RemoveRequest.SerializeToString,
            document__db__pb2.RemoveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def explain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/explain',
            document__db__pb2.ExplainRequest.SerializeToString,
            document__db__pb2.ExplainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_collection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/create_collection',
            document__db__pb2.CreateCollectionRequest.SerializeToString,
            document__db__pb2.CreateCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def drop_collection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/drop_collection',
            document__db__pb2.DropCollectionRequest.SerializeToString,
            document__db__pb2.DropCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rename_collection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/rename_collection',
            document__db__pb2.RenameCollectionRequest.SerializeToString,
            document__db__pb2.RenameCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_collection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/get_collection',
            document__db__pb2.GetCollectionRequest.SerializeToString,
            document__db__pb2.GetCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_collections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/get_collections',
            document__db__pb2.GetCollectionsRequest.SerializeToString,
            document__db__pb2.GetCollectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list_collections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/list_collections',
            document__db__pb2.ListCollectionsRequest.SerializeToString,
            document__db__pb2.ListCollectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def truncate_collection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/truncate_collection',
            document__db__pb2.TruncateCollectionRequest.SerializeToString,
            document__db__pb2.TruncateCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/create_index',
            document__db__pb2.CreateIndexRequest.SerializeToString,
            document__db__pb2.CreateIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def drop_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/drop_index',
            document__db__pb2.DropIndexRequest.SerializeToString,
            document__db__pb2.DropIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rename_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/rename_index',
            document__db__pb2.RenameIndexRequest.SerializeToString,
            document__db__pb2.RenameIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cognica.rpc.db.document.DocumentDBService/get_index',
            document__db__pb2.GetIndexRequest.SerializeToString,
            document__db__pb2.GetIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
