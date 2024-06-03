# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library/teka/events/test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from library.teka.events import event_pb2 as library_dot_teka_dot_events_dot_event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='library/teka/events/test.proto',
  package='tekone.library.teka.events',
  syntax='proto3',
  serialized_options=b'Z*go.tekoapis.com/tekone/library/teka/events',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1elibrary/teka/events/test.proto\x12\x1atekone.library.teka.events\x1a\x1flibrary/teka/events/event.proto\"0\n\x04Ping\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t:\x0b\x8a\x91$\x07\n\x02Id\x1a\x01\x01\"y\n\x03\x46oo\x12\x0f\n\x07message\x18\x01 \x01(\t\x12<\n\x13\x62\x61r_with_underscore\x18\x02 \x01(\x0b\x32\x1f.tekone.library.teka.events.Bar:#\x8a\x91$\x1f\n\x1a\x62\x61r_with_underscore.bar_id\x1a\x01\x01\"#\n\x03\x42\x61r\x12\x0e\n\x06\x62\x61r_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"7\n\x04Pong\x12\x0f\n\x07pong_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t:\x10\x8a\x91$\x0c\n\x07pong_id\x1a\x01\x01\x42,Z*go.tekoapis.com/tekone/library/teka/eventsb\x06proto3'
  ,
  dependencies=[library_dot_teka_dot_events_dot_event__pb2.DESCRIPTOR,])




_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='tekone.library.teka.events.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tekone.library.teka.events.Ping.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='tekone.library.teka.events.Ping.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\221$\007\n\002Id\032\001\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=143,
)


_FOO = _descriptor.Descriptor(
  name='Foo',
  full_name='tekone.library.teka.events.Foo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tekone.library.teka.events.Foo.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bar_with_underscore', full_name='tekone.library.teka.events.Foo.bar_with_underscore', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\221$\037\n\032bar_with_underscore.bar_id\032\001\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=266,
)


_BAR = _descriptor.Descriptor(
  name='Bar',
  full_name='tekone.library.teka.events.Bar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bar_id', full_name='tekone.library.teka.events.Bar.bar_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='tekone.library.teka.events.Bar.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=268,
  serialized_end=303,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='tekone.library.teka.events.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pong_id', full_name='tekone.library.teka.events.Pong.pong_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='tekone.library.teka.events.Pong.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\221$\014\n\007pong_id\032\001\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=360,
)

_FOO.fields_by_name['bar_with_underscore'].message_type = _BAR
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Foo'] = _FOO
DESCRIPTOR.message_types_by_name['Bar'] = _BAR
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), {
  'DESCRIPTOR' : _PING,
  '__module__' : 'library.teka.events.test_pb2'
  # @@protoc_insertion_point(class_scope:tekone.library.teka.events.Ping)
  })
_sym_db.RegisterMessage(Ping)

Foo = _reflection.GeneratedProtocolMessageType('Foo', (_message.Message,), {
  'DESCRIPTOR' : _FOO,
  '__module__' : 'library.teka.events.test_pb2'
  # @@protoc_insertion_point(class_scope:tekone.library.teka.events.Foo)
  })
_sym_db.RegisterMessage(Foo)

Bar = _reflection.GeneratedProtocolMessageType('Bar', (_message.Message,), {
  'DESCRIPTOR' : _BAR,
  '__module__' : 'library.teka.events.test_pb2'
  # @@protoc_insertion_point(class_scope:tekone.library.teka.events.Bar)
  })
_sym_db.RegisterMessage(Bar)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), {
  'DESCRIPTOR' : _PONG,
  '__module__' : 'library.teka.events.test_pb2'
  # @@protoc_insertion_point(class_scope:tekone.library.teka.events.Pong)
  })
_sym_db.RegisterMessage(Pong)


DESCRIPTOR._options = None
_PING._options = None
_FOO._options = None
_PONG._options = None
# @@protoc_insertion_point(module_scope)