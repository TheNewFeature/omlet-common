# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: container.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63ontainer.proto\x12\x05omlet\"G\n\x1b\x41ttachStandardOutputRequest\x12\x12\n\nip_address\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\".\n\x1c\x41ttachStandardOutputResponse\x12\x0e\n\x06stdout\x18\x01 \x01(\t2w\n\x10\x43ontainerService\x12\x63\n\x14\x41ttachStandardOutput\x12\".omlet.AttachStandardOutputRequest\x1a#.omlet.AttachStandardOutputResponse\"\x00\x30\x01\x62\x06proto3')



_ATTACHSTANDARDOUTPUTREQUEST = DESCRIPTOR.message_types_by_name['AttachStandardOutputRequest']
_ATTACHSTANDARDOUTPUTRESPONSE = DESCRIPTOR.message_types_by_name['AttachStandardOutputResponse']
AttachStandardOutputRequest = _reflection.GeneratedProtocolMessageType('AttachStandardOutputRequest', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHSTANDARDOUTPUTREQUEST,
  '__module__' : 'container_pb2'
  # @@protoc_insertion_point(class_scope:omlet.AttachStandardOutputRequest)
  })
_sym_db.RegisterMessage(AttachStandardOutputRequest)

AttachStandardOutputResponse = _reflection.GeneratedProtocolMessageType('AttachStandardOutputResponse', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHSTANDARDOUTPUTRESPONSE,
  '__module__' : 'container_pb2'
  # @@protoc_insertion_point(class_scope:omlet.AttachStandardOutputResponse)
  })
_sym_db.RegisterMessage(AttachStandardOutputResponse)

_CONTAINERSERVICE = DESCRIPTOR.services_by_name['ContainerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ATTACHSTANDARDOUTPUTREQUEST._serialized_start=26
  _ATTACHSTANDARDOUTPUTREQUEST._serialized_end=97
  _ATTACHSTANDARDOUTPUTRESPONSE._serialized_start=99
  _ATTACHSTANDARDOUTPUTRESPONSE._serialized_end=145
  _CONTAINERSERVICE._serialized_start=147
  _CONTAINERSERVICE._serialized_end=266
# @@protoc_insertion_point(module_scope)
