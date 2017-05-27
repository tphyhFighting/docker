# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/youtube.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/youtube.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x14protos/youtube.proto\x12\x06protos\"#\n\x13YoutubeWatchRequest\x12\x0c\n\x04link\x18\x01 \x01(\t\"\x8d\x01\n\x11YoutubeWatchReply\x12\n\n\x02Id\x18\x01 \x01(\t\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x14\n\x0cThumbnailUrl\x18\x03 \x01(\t\x12\x14\n\x0cThumbnailFid\x18\x04 \x01(\t\x12\x1a\n\x12ThumbnailImgFitApi\x18\x05 \x01(\t\x12\x15\n\rLengthSeconds\x18\x06 \x01(\t2S\n\x07Greeter\x12H\n\x0cYoutubeWatch\x12\x1b.protos.YoutubeWatchRequest\x1a\x19.protos.YoutubeWatchReply\"\x00\x42&\n\x11\x63om.apkpure.protoB\x11YoutubeWatchProtob\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_YOUTUBEWATCHREQUEST = _descriptor.Descriptor(
  name='YoutubeWatchRequest',
  full_name='protos.YoutubeWatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link', full_name='protos.YoutubeWatchRequest.link', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=67,
)


_YOUTUBEWATCHREPLY = _descriptor.Descriptor(
  name='YoutubeWatchReply',
  full_name='protos.YoutubeWatchReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='protos.YoutubeWatchReply.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Title', full_name='protos.YoutubeWatchReply.Title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ThumbnailUrl', full_name='protos.YoutubeWatchReply.ThumbnailUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ThumbnailFid', full_name='protos.YoutubeWatchReply.ThumbnailFid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ThumbnailImgFitApi', full_name='protos.YoutubeWatchReply.ThumbnailImgFitApi', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LengthSeconds', full_name='protos.YoutubeWatchReply.LengthSeconds', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=211,
)

DESCRIPTOR.message_types_by_name['YoutubeWatchRequest'] = _YOUTUBEWATCHREQUEST
DESCRIPTOR.message_types_by_name['YoutubeWatchReply'] = _YOUTUBEWATCHREPLY

YoutubeWatchRequest = _reflection.GeneratedProtocolMessageType('YoutubeWatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _YOUTUBEWATCHREQUEST,
  __module__ = 'protos.youtube_pb2'
  # @@protoc_insertion_point(class_scope:protos.YoutubeWatchRequest)
  ))
_sym_db.RegisterMessage(YoutubeWatchRequest)

YoutubeWatchReply = _reflection.GeneratedProtocolMessageType('YoutubeWatchReply', (_message.Message,), dict(
  DESCRIPTOR = _YOUTUBEWATCHREPLY,
  __module__ = 'protos.youtube_pb2'
  # @@protoc_insertion_point(class_scope:protos.YoutubeWatchReply)
  ))
_sym_db.RegisterMessage(YoutubeWatchReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\021com.apkpure.protoB\021YoutubeWatchProto'))
# @@protoc_insertion_point(module_scope)