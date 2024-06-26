# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key_value_db.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12key_value_db.proto\x12\x0e\x61\x65\x63\x61.rpc.db.kv\"\"\n\x0bProfileInfo\x12\x13\n\x0b\x64uration_us\x18\x01 \x01(\x04\"u\n\x08Response\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.aeca.rpc.db.kv.StatusType\x12\x0f\n\x07message\x18\x02 \x01(\t\x12,\n\x07profile\x18\x03 \x01(\x0b\x32\x1b.aeca.rpc.db.kv.ProfileInfo\"g\n\nPutRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\r\n\x05value\x18\x03 \x01(\x0c\x12\x0b\n\x03ttl\x18\x04 \x01(\x03\x12\x19\n\x11\x63reate_if_missing\x18\x05 \x01(\x08\"9\n\x0bPutResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\"3\n\rRemoveRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\"<\n\x0eRemoveResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\"0\n\nGetRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\"H\n\x0bGetResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\x12\r\n\x05value\x18\x02 \x01(\x0c\"6\n\x0fMultiGetRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\x0c\"O\n\x10MultiGetResponse\x12+\n\tresponses\x18\x01 \x03(\x0b\x32\x18.aeca.rpc.db.kv.Response\x12\x0e\n\x06values\x18\x02 \x03(\x0c\"q\n\x11\x42\x61tchedPutRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\x0c\x12\x0e\n\x06values\x18\x03 \x03(\x0c\x12\x0c\n\x04ttls\x18\x04 \x03(\x03\x12\x19\n\x11\x63reate_if_missing\x18\x05 \x01(\x08\"A\n\x12\x42\x61tchedPutResponse\x12+\n\tresponses\x18\x01 \x03(\x0b\x32\x18.aeca.rpc.db.kv.Response\";\n\x14\x42\x61tchedRemoveRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\x0c\"D\n\x15\x42\x61tchedRemoveResponse\x12+\n\tresponses\x18\x01 \x03(\x0b\x32\x18.aeca.rpc.db.kv.Response\"8\n\x11\x42\x61tchedGetRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\x0c\"Q\n\x12\x42\x61tchedGetResponse\x12+\n\tresponses\x18\x01 \x03(\x0b\x32\x18.aeca.rpc.db.kv.Response\x12\x0e\n\x06values\x18\x02 \x03(\x0c\".\n\x15\x43reateKeyspaceRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\"D\n\x16\x43reateKeyspaceResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\",\n\x13\x44ropKeyspaceRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\"B\n\x14\x44ropKeyspaceResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\"0\n\x17TruncateKeyspaceRequest\x12\x15\n\rkeyspace_name\x18\x01 \x01(\t\"F\n\x18TruncateKeyspaceResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\"\x16\n\x14ListKeyspacesRequest\"[\n\x15ListKeyspacesResponse\x12*\n\x08response\x18\x01 \x01(\x0b\x32\x18.aeca.rpc.db.kv.Response\x12\x16\n\x0ekeyspace_names\x18\x02 \x03(\t*3\n\nStatusType\x12\x07\n\x03kOK\x10\x00\x12\r\n\tkNotFound\x10\x01\x12\r\n\tkInternal\x10\n2\xba\x04\n\x11KeyValueDBService\x12@\n\x03put\x12\x1a.aeca.rpc.db.kv.PutRequest\x1a\x1b.aeca.rpc.db.kv.PutResponse\"\x00\x12I\n\x06remove\x12\x1d.aeca.rpc.db.kv.RemoveRequest\x1a\x1e.aeca.rpc.db.kv.RemoveResponse\"\x00\x12@\n\x03get\x12\x1a.aeca.rpc.db.kv.GetRequest\x1a\x1b.aeca.rpc.db.kv.GetResponse\"\x00\x12K\n\x04mget\x12\x1f.aeca.rpc.db.kv.MultiGetRequest\x1a .aeca.rpc.db.kv.MultiGetResponse\"\x00\x12T\n\tput_batch\x12!.aeca.rpc.db.kv.BatchedPutRequest\x1a\".aeca.rpc.db.kv.BatchedPutResponse\"\x00\x12]\n\x0cremove_batch\x12$.aeca.rpc.db.kv.BatchedRemoveRequest\x1a%.aeca.rpc.db.kv.BatchedRemoveResponse\"\x00\x12T\n\tget_batch\x12!.aeca.rpc.db.kv.BatchedGetRequest\x1a\".aeca.rpc.db.kv.BatchedGetResponse\"\x00\x32\xa5\x03\n\x16KeyspaceManagerService\x12\x62\n\x0f\x63reate_keyspace\x12%.aeca.rpc.db.kv.CreateKeyspaceRequest\x1a&.aeca.rpc.db.kv.CreateKeyspaceResponse\"\x00\x12\\\n\rdrop_keyspace\x12#.aeca.rpc.db.kv.DropKeyspaceRequest\x1a$.aeca.rpc.db.kv.DropKeyspaceResponse\"\x00\x12h\n\x11truncate_keyspace\x12\'.aeca.rpc.db.kv.TruncateKeyspaceRequest\x1a(.aeca.rpc.db.kv.TruncateKeyspaceResponse\"\x00\x12_\n\x0elist_keyspaces\x12$.aeca.rpc.db.kv.ListKeyspacesRequest\x1a%.aeca.rpc.db.kv.ListKeyspacesResponse\"\x00\x42\x03\xf8\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'key_value_db_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\370\001\001'
  _globals['_STATUSTYPE']._serialized_start=1658
  _globals['_STATUSTYPE']._serialized_end=1709
  _globals['_PROFILEINFO']._serialized_start=38
  _globals['_PROFILEINFO']._serialized_end=72
  _globals['_RESPONSE']._serialized_start=74
  _globals['_RESPONSE']._serialized_end=191
  _globals['_PUTREQUEST']._serialized_start=193
  _globals['_PUTREQUEST']._serialized_end=296
  _globals['_PUTRESPONSE']._serialized_start=298
  _globals['_PUTRESPONSE']._serialized_end=355
  _globals['_REMOVEREQUEST']._serialized_start=357
  _globals['_REMOVEREQUEST']._serialized_end=408
  _globals['_REMOVERESPONSE']._serialized_start=410
  _globals['_REMOVERESPONSE']._serialized_end=470
  _globals['_GETREQUEST']._serialized_start=472
  _globals['_GETREQUEST']._serialized_end=520
  _globals['_GETRESPONSE']._serialized_start=522
  _globals['_GETRESPONSE']._serialized_end=594
  _globals['_MULTIGETREQUEST']._serialized_start=596
  _globals['_MULTIGETREQUEST']._serialized_end=650
  _globals['_MULTIGETRESPONSE']._serialized_start=652
  _globals['_MULTIGETRESPONSE']._serialized_end=731
  _globals['_BATCHEDPUTREQUEST']._serialized_start=733
  _globals['_BATCHEDPUTREQUEST']._serialized_end=846
  _globals['_BATCHEDPUTRESPONSE']._serialized_start=848
  _globals['_BATCHEDPUTRESPONSE']._serialized_end=913
  _globals['_BATCHEDREMOVEREQUEST']._serialized_start=915
  _globals['_BATCHEDREMOVEREQUEST']._serialized_end=974
  _globals['_BATCHEDREMOVERESPONSE']._serialized_start=976
  _globals['_BATCHEDREMOVERESPONSE']._serialized_end=1044
  _globals['_BATCHEDGETREQUEST']._serialized_start=1046
  _globals['_BATCHEDGETREQUEST']._serialized_end=1102
  _globals['_BATCHEDGETRESPONSE']._serialized_start=1104
  _globals['_BATCHEDGETRESPONSE']._serialized_end=1185
  _globals['_CREATEKEYSPACEREQUEST']._serialized_start=1187
  _globals['_CREATEKEYSPACEREQUEST']._serialized_end=1233
  _globals['_CREATEKEYSPACERESPONSE']._serialized_start=1235
  _globals['_CREATEKEYSPACERESPONSE']._serialized_end=1303
  _globals['_DROPKEYSPACEREQUEST']._serialized_start=1305
  _globals['_DROPKEYSPACEREQUEST']._serialized_end=1349
  _globals['_DROPKEYSPACERESPONSE']._serialized_start=1351
  _globals['_DROPKEYSPACERESPONSE']._serialized_end=1417
  _globals['_TRUNCATEKEYSPACEREQUEST']._serialized_start=1419
  _globals['_TRUNCATEKEYSPACEREQUEST']._serialized_end=1467
  _globals['_TRUNCATEKEYSPACERESPONSE']._serialized_start=1469
  _globals['_TRUNCATEKEYSPACERESPONSE']._serialized_end=1539
  _globals['_LISTKEYSPACESREQUEST']._serialized_start=1541
  _globals['_LISTKEYSPACESREQUEST']._serialized_end=1563
  _globals['_LISTKEYSPACESRESPONSE']._serialized_start=1565
  _globals['_LISTKEYSPACESRESPONSE']._serialized_end=1656
  _globals['_KEYVALUEDBSERVICE']._serialized_start=1712
  _globals['_KEYVALUEDBSERVICE']._serialized_end=2282
  _globals['_KEYSPACEMANAGERSERVICE']._serialized_start=2285
  _globals['_KEYSPACEMANAGERSERVICE']._serialized_end=2706
# @@protoc_insertion_point(module_scope)
