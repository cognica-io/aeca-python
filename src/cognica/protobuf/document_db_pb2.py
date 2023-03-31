# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: document_db.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import cognica.protobuf.document_pb2 as document__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64ocument_db.proto\x12\x17\x63ognica.rpc.db.document\x1a\x0e\x64ocument.proto\"\xf3\x01\n\tIndexDesc\x12\x10\n\x08index_id\x18\x01 \x01(\r\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\x0e\n\x06unique\x18\x04 \x01(\x08\x12\x36\n\nindex_type\x18\x05 \x01(\x0e\x32\".cognica.rpc.db.document.IndexType\x12\x34\n\x06status\x18\x07 \x01(\x0e\x32$.cognica.rpc.db.document.IndexStatus\x12\x32\n\x07options\x18\x08 \x01(\x0b\x32!.cognica.rpc.db.document.Document\"e\n\x12\x43reateIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x36\n\nindex_desc\x18\x02 \x01(\x0b\x32\".cognica.rpc.db.document.IndexDesc\"6\n\x13\x43reateIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"?\n\x10\x44ropIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"4\n\x11\x44ropIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\">\n\x0fGetIndexRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"\x84\x01\n\x10GetIndexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_name\x18\x03 \x01(\t\x12\x36\n\nindex_desc\x18\x04 \x01(\x0b\x32\".cognica.rpc.db.document.IndexDesc\"R\n\x05Query\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x30\n\x05query\x18\x02 \x01(\x0b\x32!.cognica.rpc.db.document.Document\"\xfb\x01\n\x0b\x46indRequest\x12-\n\x05query\x18\x01 \x01(\x0b\x32\x1e.cognica.rpc.db.document.Query\x12\x15\n\rindex_columns\x18\x02 \x03(\t\x12\x0f\n\x07\x63olumns\x18\x03 \x03(\t\x12@\n\x06\x64types\x18\x04 \x03(\x0b\x32\x30.cognica.rpc.db.document.FindRequest.DtypesEntry\x12\x0e\n\x06no_obs\x18\x05 \x01(\x05\x12\x14\n\x0cprivate_info\x18\x06 \x01(\x08\x1a-\n\x0b\x44typesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x0c\x46indResponse\x12\x13\n\x0bnum_columns\x18\x01 \x01(\x05\x12\x10\n\x08num_rows\x18\x02 \x01(\x05\x12\x0e\n\x06\x62uffer\x18\x03 \x01(\x0c\"J\n\x10\x46indBatchRequest\x12\x36\n\x08requests\x18\x01 \x03(\x0b\x32$.cognica.rpc.db.document.FindRequest\"M\n\x11\x46indBatchResponse\x12\x38\n\tresponses\x18\x01 \x03(\x0b\x32%.cognica.rpc.db.document.FindResponse\"=\n\x0c\x43ountRequest\x12-\n\x05query\x18\x01 \x01(\x0b\x32\x1e.cognica.rpc.db.document.Query\"?\n\rCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"@\n\x0f\x43ontainsRequest\x12-\n\x05query\x18\x01 \x01(\x0b\x32\x1e.cognica.rpc.db.document.Query\"B\n\x10\x43ontainsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x66ound\x18\x03 \x01(\x08\"A\n\rInsertRequest\x12\x30\n\x08requests\x18\x01 \x03(\x0b\x32\x1e.cognica.rpc.db.document.Query\"1\n\x0eInsertResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x8f\x01\n\rUpdateRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\x12\x31\n\x06\x66ilter\x18\x02 \x01(\x0b\x32!.cognica.rpc.db.document.Document\x12\x32\n\x07updates\x18\x03 \x01(\x0b\x32!.cognica.rpc.db.document.Document\"1\n\x0eUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"A\n\rRemoveRequest\x12\x30\n\x08requests\x18\x01 \x03(\x0b\x32\x1e.cognica.rpc.db.document.Query\"1\n\x0eRemoveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"4\n\x19TruncateCollectionRequest\x12\x17\n\x0f\x63ollection_name\x18\x01 \x01(\t\"=\n\x1aTruncateCollectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x18\n\x16ListCollectionsRequest\"T\n\x17ListCollectionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x10\x63ollection_names\x18\x03 \x03(\t*e\n\tIndexType\x12\x0f\n\x0bkPrimaryKey\x10\x00\x12\x11\n\rkSecondaryKey\x10\x01\x12\x1a\n\x16kClusteredSecondaryKey\x10\x02\x12\x18\n\x14kFullTextSearchIndex\x10\x03*\x8d\x01\n\x0bIndexStatus\x12\x0c\n\x08kEnabled\x10\x00\x12\r\n\tkDisabled\x10\x01\x12\x0f\n\x0bkReadyToUse\x10\x02\x12\x14\n\x10kBuildInProgress\x10\x03\x12\x12\n\x0ekBuildFinished\x10\x04\x12\x13\n\x0fkDropInProgress\x10\x05\x12\x11\n\rkDropFinished\x10\x06\x32\xd9\t\n\x11\x44ocumentDBService\x12U\n\x04\x66ind\x12$.cognica.rpc.db.document.FindRequest\x1a%.cognica.rpc.db.document.FindResponse\"\x00\x12\x65\n\nfind_batch\x12).cognica.rpc.db.document.FindBatchRequest\x1a*.cognica.rpc.db.document.FindBatchResponse\"\x00\x12X\n\x05\x63ount\x12%.cognica.rpc.db.document.CountRequest\x1a&.cognica.rpc.db.document.CountResponse\"\x00\x12\x61\n\x08\x63ontains\x12(.cognica.rpc.db.document.ContainsRequest\x1a).cognica.rpc.db.document.ContainsResponse\"\x00\x12[\n\x06insert\x12&.cognica.rpc.db.document.InsertRequest\x1a\'.cognica.rpc.db.document.InsertResponse\"\x00\x12[\n\x06update\x12&.cognica.rpc.db.document.UpdateRequest\x1a\'.cognica.rpc.db.document.UpdateResponse\"\x00\x12[\n\x06remove\x12&.cognica.rpc.db.document.RemoveRequest\x1a\'.cognica.rpc.db.document.RemoveResponse\"\x00\x12w\n\x10list_collections\x12/.cognica.rpc.db.document.ListCollectionsRequest\x1a\x30.cognica.rpc.db.document.ListCollectionsResponse\"\x00\x12\x80\x01\n\x13truncate_collection\x12\x32.cognica.rpc.db.document.TruncateCollectionRequest\x1a\x33.cognica.rpc.db.document.TruncateCollectionResponse\"\x00\x12k\n\x0c\x63reate_index\x12+.cognica.rpc.db.document.CreateIndexRequest\x1a,.cognica.rpc.db.document.CreateIndexResponse\"\x00\x12\x65\n\ndrop_index\x12).cognica.rpc.db.document.DropIndexRequest\x1a*.cognica.rpc.db.document.DropIndexResponse\"\x00\x12\x62\n\tget_index\x12(.cognica.rpc.db.document.GetIndexRequest\x1a).cognica.rpc.db.document.GetIndexResponse\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'document_db_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001'
  _FINDREQUEST_DTYPESENTRY._options = None
  _FINDREQUEST_DTYPESENTRY._serialized_options = b'8\001'
  _INDEXTYPE._serialized_start=2273
  _INDEXTYPE._serialized_end=2374
  _INDEXSTATUS._serialized_start=2377
  _INDEXSTATUS._serialized_end=2518
  _INDEXDESC._serialized_start=63
  _INDEXDESC._serialized_end=306
  _CREATEINDEXREQUEST._serialized_start=308
  _CREATEINDEXREQUEST._serialized_end=409
  _CREATEINDEXRESPONSE._serialized_start=411
  _CREATEINDEXRESPONSE._serialized_end=465
  _DROPINDEXREQUEST._serialized_start=467
  _DROPINDEXREQUEST._serialized_end=530
  _DROPINDEXRESPONSE._serialized_start=532
  _DROPINDEXRESPONSE._serialized_end=584
  _GETINDEXREQUEST._serialized_start=586
  _GETINDEXREQUEST._serialized_end=648
  _GETINDEXRESPONSE._serialized_start=651
  _GETINDEXRESPONSE._serialized_end=783
  _QUERY._serialized_start=785
  _QUERY._serialized_end=867
  _FINDREQUEST._serialized_start=870
  _FINDREQUEST._serialized_end=1121
  _FINDREQUEST_DTYPESENTRY._serialized_start=1076
  _FINDREQUEST_DTYPESENTRY._serialized_end=1121
  _FINDRESPONSE._serialized_start=1123
  _FINDRESPONSE._serialized_end=1192
  _FINDBATCHREQUEST._serialized_start=1194
  _FINDBATCHREQUEST._serialized_end=1268
  _FINDBATCHRESPONSE._serialized_start=1270
  _FINDBATCHRESPONSE._serialized_end=1347
  _COUNTREQUEST._serialized_start=1349
  _COUNTREQUEST._serialized_end=1410
  _COUNTRESPONSE._serialized_start=1412
  _COUNTRESPONSE._serialized_end=1475
  _CONTAINSREQUEST._serialized_start=1477
  _CONTAINSREQUEST._serialized_end=1541
  _CONTAINSRESPONSE._serialized_start=1543
  _CONTAINSRESPONSE._serialized_end=1609
  _INSERTREQUEST._serialized_start=1611
  _INSERTREQUEST._serialized_end=1676
  _INSERTRESPONSE._serialized_start=1678
  _INSERTRESPONSE._serialized_end=1727
  _UPDATEREQUEST._serialized_start=1730
  _UPDATEREQUEST._serialized_end=1873
  _UPDATERESPONSE._serialized_start=1875
  _UPDATERESPONSE._serialized_end=1924
  _REMOVEREQUEST._serialized_start=1926
  _REMOVEREQUEST._serialized_end=1991
  _REMOVERESPONSE._serialized_start=1993
  _REMOVERESPONSE._serialized_end=2042
  _TRUNCATECOLLECTIONREQUEST._serialized_start=2044
  _TRUNCATECOLLECTIONREQUEST._serialized_end=2096
  _TRUNCATECOLLECTIONRESPONSE._serialized_start=2098
  _TRUNCATECOLLECTIONRESPONSE._serialized_end=2159
  _LISTCOLLECTIONSREQUEST._serialized_start=2161
  _LISTCOLLECTIONSREQUEST._serialized_end=2185
  _LISTCOLLECTIONSRESPONSE._serialized_start=2187
  _LISTCOLLECTIONSRESPONSE._serialized_end=2271
  _DOCUMENTDBSERVICE._serialized_start=2521
  _DOCUMENTDBSERVICE._serialized_end=3762
# @@protoc_insertion_point(module_scope)