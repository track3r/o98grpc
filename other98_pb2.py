# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: other98.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='other98.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\rother98.proto\x12\nhelloworld\"\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\t\"A\n\x0b\x46\x65\x65\x64Request\x12\x10\n\x08postTags\x18\x01 \x03(\t\x12\x0e\n\x06pageId\x18\x02 \x01(\t\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\"\x17\n\x06Handle\x12\r\n\x05value\x18\x01 \x01(\t\"\x95\x01\n\x06Result\x12\x31\n\nstatusCode\x18\x01 \x01(\x0e\x32\x1d.helloworld.Result.StatusCode\"X\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0cUNAUTHORIZED\x10\x01\x12\r\n\tFORBIDDEN\x10\x02\x12\r\n\tNOT_FOUND\x10\x03\x12\x12\n\x0eINTERNAL_ERROR\x10\x04\"\x86\x01\n\rPostSmallView\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x19\n\x11\x66\x65\x61turedImageLink\x18\x03 \x01(\t\x12\x12\n\ncreateDate\x18\x06 \x01(\x03\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x14\n\x0c\x61uthorHandle\x18\x08 \x01(\t\"{\n\x04Post\x12\x30\n\rpostSmallView\x18\x01 \x01(\x0b\x32\x19.helloworld.PostSmallView\x12/\n\rcontentBlocks\x18\x02 \x03(\x0b\x32\x18.helloworld.ContentBlock\x12\x10\n\x08postTags\x18\x03 \x03(\t\"K\n\x11\x43reatePostRequest\x12\x1e\n\x04post\x18\x01 \x01(\x0b\x32\x10.helloworld.Post\x12\x16\n\x0eviewable_roles\x18\x02 \x03(\t\"\xb2\x01\n\x08PostView\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\rpostSmallView\x18\x02 \x01(\x0b\x32\x19.helloworld.PostSmallView\x12/\n\rcontentBlocks\x18\x03 \x03(\x0b\x32\x18.helloworld.ContentBlock\x12\x10\n\x08postTags\x18\x04 \x03(\t\x12%\n\x08\x63omments\x18\x05 \x03(\x0b\x32\x13.helloworld.Comment\"\x89\x01\n\x0cPostFeedView\x12\x12\n\npostViewId\x18\x01 \x01(\t\x12\x30\n\rpostSmallView\x18\x02 \x01(\x0b\x32\x19.helloworld.PostSmallView\x12\x18\n\x10numberOfComments\x18\x03 \x01(\x03\x12\x19\n\x11\x64\x61teOfLastComment\x18\x04 \x01(\x03\"6\n\x07Profile\x12\x0e\n\x06handle\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\"\xdf\x01\n\x0c\x43ontentBlock\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).helloworld.ContentBlock.ContentBlockType\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12*\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x18.helloworld.ContentBlock\"Y\n\x10\x43ontentBlockType\x12\x08\n\x04Text\x10\x00\x12\t\n\x05Image\x10\x01\x12\x10\n\x0cImageGallery\x10\x02\x12\x08\n\x04Link\x10\x03\x12\t\n\x05Video\x10\x04\x12\t\n\x05Quote\x10\x05\"v\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x12\n\npostViewId\x18\x02 \x01(\t\x12\x18\n\x10\x63reateDateMillis\x18\x03 \x01(\x03\x12\x14\n\x0c\x61uthorHandle\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\r\n\x05score\x18\x06 \x01(\x03\"E\n\x0b\x43ommentView\x12$\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x13.helloworld.Comment\x12\x10\n\x08userVote\x18\x03 \x01(\x05\x32\xb9\x02\n\nTheOther98\x12@\n\x07GetFeed\x12\x17.helloworld.FeedRequest\x1a\x18.helloworld.PostFeedView\"\x00\x30\x01\x12\x31\n\x07GetPost\x12\x0e.helloworld.Id\x1a\x14.helloworld.PostView\"\x00\x12\x37\n\nGetProfile\x12\x12.helloworld.Handle\x1a\x13.helloworld.Profile\"\x00\x12\x41\n\nCreatePost\x12\x1d.helloworld.CreatePostRequest\x1a\x12.helloworld.Result\"\x00\x12:\n\rCreateComment\x12\x13.helloworld.Comment\x1a\x12.helloworld.Result\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)



_RESULT_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='helloworld.Result.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORBIDDEN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=204,
  serialized_end=292,
)
_sym_db.RegisterEnumDescriptor(_RESULT_STATUSCODE)

_CONTENTBLOCK_CONTENTBLOCKTYPE = _descriptor.EnumDescriptor(
  name='ContentBlockType',
  full_name='helloworld.ContentBlock.ContentBlockType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Text', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Image', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ImageGallery', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Link', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Video', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Quote', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1145,
  serialized_end=1234,
)
_sym_db.RegisterEnumDescriptor(_CONTENTBLOCK_CONTENTBLOCKTYPE)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='helloworld.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='helloworld.Id.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=48,
)


_FEEDREQUEST = _descriptor.Descriptor(
  name='FeedRequest',
  full_name='helloworld.FeedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='postTags', full_name='helloworld.FeedRequest.postTags', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageId', full_name='helloworld.FeedRequest.pageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='helloworld.FeedRequest.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=115,
)


_HANDLE = _descriptor.Descriptor(
  name='Handle',
  full_name='helloworld.Handle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='helloworld.Handle.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=140,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='helloworld.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statusCode', full_name='helloworld.Result.statusCode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESULT_STATUSCODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=292,
)


_POSTSMALLVIEW = _descriptor.Descriptor(
  name='PostSmallView',
  full_name='helloworld.PostSmallView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='helloworld.PostSmallView.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='helloworld.PostSmallView.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='featuredImageLink', full_name='helloworld.PostSmallView.featuredImageLink', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createDate', full_name='helloworld.PostSmallView.createDate', index=3,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='helloworld.PostSmallView.type', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authorHandle', full_name='helloworld.PostSmallView.authorHandle', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=429,
)


_POST = _descriptor.Descriptor(
  name='Post',
  full_name='helloworld.Post',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='postSmallView', full_name='helloworld.Post.postSmallView', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contentBlocks', full_name='helloworld.Post.contentBlocks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postTags', full_name='helloworld.Post.postTags', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=554,
)


_CREATEPOSTREQUEST = _descriptor.Descriptor(
  name='CreatePostRequest',
  full_name='helloworld.CreatePostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='post', full_name='helloworld.CreatePostRequest.post', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewable_roles', full_name='helloworld.CreatePostRequest.viewable_roles', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=631,
)


_POSTVIEW = _descriptor.Descriptor(
  name='PostView',
  full_name='helloworld.PostView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='helloworld.PostView.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postSmallView', full_name='helloworld.PostView.postSmallView', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contentBlocks', full_name='helloworld.PostView.contentBlocks', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postTags', full_name='helloworld.PostView.postTags', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='helloworld.PostView.comments', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=812,
)


_POSTFEEDVIEW = _descriptor.Descriptor(
  name='PostFeedView',
  full_name='helloworld.PostFeedView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='postViewId', full_name='helloworld.PostFeedView.postViewId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postSmallView', full_name='helloworld.PostFeedView.postSmallView', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberOfComments', full_name='helloworld.PostFeedView.numberOfComments', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dateOfLastComment', full_name='helloworld.PostFeedView.dateOfLastComment', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=952,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='helloworld.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='handle', full_name='helloworld.Profile.handle', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='helloworld.Profile.email', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='helloworld.Profile.type', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=954,
  serialized_end=1008,
)


_CONTENTBLOCK = _descriptor.Descriptor(
  name='ContentBlock',
  full_name='helloworld.ContentBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='helloworld.ContentBlock.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='helloworld.ContentBlock.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='helloworld.ContentBlock.children', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTENTBLOCK_CONTENTBLOCKTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1011,
  serialized_end=1234,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='helloworld.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='helloworld.Comment.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postViewId', full_name='helloworld.Comment.postViewId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createDateMillis', full_name='helloworld.Comment.createDateMillis', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authorHandle', full_name='helloworld.Comment.authorHandle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='helloworld.Comment.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='helloworld.Comment.score', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1236,
  serialized_end=1354,
)


_COMMENTVIEW = _descriptor.Descriptor(
  name='CommentView',
  full_name='helloworld.CommentView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment', full_name='helloworld.CommentView.comment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userVote', full_name='helloworld.CommentView.userVote', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1356,
  serialized_end=1425,
)

_RESULT.fields_by_name['statusCode'].enum_type = _RESULT_STATUSCODE
_RESULT_STATUSCODE.containing_type = _RESULT
_POST.fields_by_name['postSmallView'].message_type = _POSTSMALLVIEW
_POST.fields_by_name['contentBlocks'].message_type = _CONTENTBLOCK
_CREATEPOSTREQUEST.fields_by_name['post'].message_type = _POST
_POSTVIEW.fields_by_name['postSmallView'].message_type = _POSTSMALLVIEW
_POSTVIEW.fields_by_name['contentBlocks'].message_type = _CONTENTBLOCK
_POSTVIEW.fields_by_name['comments'].message_type = _COMMENT
_POSTFEEDVIEW.fields_by_name['postSmallView'].message_type = _POSTSMALLVIEW
_CONTENTBLOCK.fields_by_name['type'].enum_type = _CONTENTBLOCK_CONTENTBLOCKTYPE
_CONTENTBLOCK.fields_by_name['children'].message_type = _CONTENTBLOCK
_CONTENTBLOCK_CONTENTBLOCKTYPE.containing_type = _CONTENTBLOCK
_COMMENTVIEW.fields_by_name['comment'].message_type = _COMMENT
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['FeedRequest'] = _FEEDREQUEST
DESCRIPTOR.message_types_by_name['Handle'] = _HANDLE
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['PostSmallView'] = _POSTSMALLVIEW
DESCRIPTOR.message_types_by_name['Post'] = _POST
DESCRIPTOR.message_types_by_name['CreatePostRequest'] = _CREATEPOSTREQUEST
DESCRIPTOR.message_types_by_name['PostView'] = _POSTVIEW
DESCRIPTOR.message_types_by_name['PostFeedView'] = _POSTFEEDVIEW
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE
DESCRIPTOR.message_types_by_name['ContentBlock'] = _CONTENTBLOCK
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['CommentView'] = _COMMENTVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), dict(
  DESCRIPTOR = _ID,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Id)
  ))
_sym_db.RegisterMessage(Id)

FeedRequest = _reflection.GeneratedProtocolMessageType('FeedRequest', (_message.Message,), dict(
  DESCRIPTOR = _FEEDREQUEST,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.FeedRequest)
  ))
_sym_db.RegisterMessage(FeedRequest)

Handle = _reflection.GeneratedProtocolMessageType('Handle', (_message.Message,), dict(
  DESCRIPTOR = _HANDLE,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Handle)
  ))
_sym_db.RegisterMessage(Handle)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Result)
  ))
_sym_db.RegisterMessage(Result)

PostSmallView = _reflection.GeneratedProtocolMessageType('PostSmallView', (_message.Message,), dict(
  DESCRIPTOR = _POSTSMALLVIEW,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.PostSmallView)
  ))
_sym_db.RegisterMessage(PostSmallView)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), dict(
  DESCRIPTOR = _POST,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Post)
  ))
_sym_db.RegisterMessage(Post)

CreatePostRequest = _reflection.GeneratedProtocolMessageType('CreatePostRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEPOSTREQUEST,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.CreatePostRequest)
  ))
_sym_db.RegisterMessage(CreatePostRequest)

PostView = _reflection.GeneratedProtocolMessageType('PostView', (_message.Message,), dict(
  DESCRIPTOR = _POSTVIEW,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.PostView)
  ))
_sym_db.RegisterMessage(PostView)

PostFeedView = _reflection.GeneratedProtocolMessageType('PostFeedView', (_message.Message,), dict(
  DESCRIPTOR = _POSTFEEDVIEW,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.PostFeedView)
  ))
_sym_db.RegisterMessage(PostFeedView)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
  DESCRIPTOR = _PROFILE,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Profile)
  ))
_sym_db.RegisterMessage(Profile)

ContentBlock = _reflection.GeneratedProtocolMessageType('ContentBlock', (_message.Message,), dict(
  DESCRIPTOR = _CONTENTBLOCK,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.ContentBlock)
  ))
_sym_db.RegisterMessage(ContentBlock)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), dict(
  DESCRIPTOR = _COMMENT,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Comment)
  ))
_sym_db.RegisterMessage(Comment)

CommentView = _reflection.GeneratedProtocolMessageType('CommentView', (_message.Message,), dict(
  DESCRIPTOR = _COMMENTVIEW,
  __module__ = 'other98_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.CommentView)
  ))
_sym_db.RegisterMessage(CommentView)


DESCRIPTOR._options = None

_THEOTHER98 = _descriptor.ServiceDescriptor(
  name='TheOther98',
  full_name='helloworld.TheOther98',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1428,
  serialized_end=1741,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeed',
    full_name='helloworld.TheOther98.GetFeed',
    index=0,
    containing_service=None,
    input_type=_FEEDREQUEST,
    output_type=_POSTFEEDVIEW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPost',
    full_name='helloworld.TheOther98.GetPost',
    index=1,
    containing_service=None,
    input_type=_ID,
    output_type=_POSTVIEW,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetProfile',
    full_name='helloworld.TheOther98.GetProfile',
    index=2,
    containing_service=None,
    input_type=_HANDLE,
    output_type=_PROFILE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePost',
    full_name='helloworld.TheOther98.CreatePost',
    index=3,
    containing_service=None,
    input_type=_CREATEPOSTREQUEST,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateComment',
    full_name='helloworld.TheOther98.CreateComment',
    index=4,
    containing_service=None,
    input_type=_COMMENT,
    output_type=_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_THEOTHER98)

DESCRIPTOR.services_by_name['TheOther98'] = _THEOTHER98

# @@protoc_insertion_point(module_scope)
