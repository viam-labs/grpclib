# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpclib/reflection/v1/reflection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&grpclib/reflection/v1/reflection.proto\x12\x12grpc.reflection.v1\"\x85\x02\n\x17ServerReflectionRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x1a\n\x10\x66ile_by_filename\x18\x03 \x01(\tH\x00\x12 \n\x16\x66ile_containing_symbol\x18\x04 \x01(\tH\x00\x12I\n\x19\x66ile_containing_extension\x18\x05 \x01(\x0b\x32$.grpc.reflection.v1.ExtensionRequestH\x00\x12\'\n\x1d\x61ll_extension_numbers_of_type\x18\x06 \x01(\tH\x00\x12\x17\n\rlist_services\x18\x07 \x01(\tH\x00\x42\x11\n\x0fmessage_request\"E\n\x10\x45xtensionRequest\x12\x17\n\x0f\x63ontaining_type\x18\x01 \x01(\t\x12\x18\n\x10\x65xtension_number\x18\x02 \x01(\x05\"\xb8\x03\n\x18ServerReflectionResponse\x12\x12\n\nvalid_host\x18\x01 \x01(\t\x12\x45\n\x10original_request\x18\x02 \x01(\x0b\x32+.grpc.reflection.v1.ServerReflectionRequest\x12N\n\x18\x66ile_descriptor_response\x18\x04 \x01(\x0b\x32*.grpc.reflection.v1.FileDescriptorResponseH\x00\x12U\n\x1e\x61ll_extension_numbers_response\x18\x05 \x01(\x0b\x32+.grpc.reflection.v1.ExtensionNumberResponseH\x00\x12I\n\x16list_services_response\x18\x06 \x01(\x0b\x32\'.grpc.reflection.v1.ListServiceResponseH\x00\x12;\n\x0e\x65rror_response\x18\x07 \x01(\x0b\x32!.grpc.reflection.v1.ErrorResponseH\x00\x42\x12\n\x10message_response\"7\n\x16\x46ileDescriptorResponse\x12\x1d\n\x15\x66ile_descriptor_proto\x18\x01 \x03(\x0c\"K\n\x17\x45xtensionNumberResponse\x12\x16\n\x0e\x62\x61se_type_name\x18\x01 \x01(\t\x12\x18\n\x10\x65xtension_number\x18\x02 \x03(\x05\"K\n\x13ListServiceResponse\x12\x34\n\x07service\x18\x01 \x03(\x0b\x32#.grpc.reflection.v1.ServiceResponse\"\x1f\n\x0fServiceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\rErrorResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t2\x89\x01\n\x10ServerReflection\x12u\n\x14ServerReflectionInfo\x12+.grpc.reflection.v1.ServerReflectionRequest\x1a,.grpc.reflection.v1.ServerReflectionResponse(\x01\x30\x01\x42\x66\n\x15io.grpc.reflection.v1B\x15ServerReflectionProtoP\x01Z4google.golang.org/grpc/reflection/grpc_reflection_v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpclib.reflection.v1.reflection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025io.grpc.reflection.v1B\025ServerReflectionProtoP\001Z4google.golang.org/grpc/reflection/grpc_reflection_v1'
  _globals['_SERVERREFLECTIONREQUEST']._serialized_start=63
  _globals['_SERVERREFLECTIONREQUEST']._serialized_end=324
  _globals['_EXTENSIONREQUEST']._serialized_start=326
  _globals['_EXTENSIONREQUEST']._serialized_end=395
  _globals['_SERVERREFLECTIONRESPONSE']._serialized_start=398
  _globals['_SERVERREFLECTIONRESPONSE']._serialized_end=838
  _globals['_FILEDESCRIPTORRESPONSE']._serialized_start=840
  _globals['_FILEDESCRIPTORRESPONSE']._serialized_end=895
  _globals['_EXTENSIONNUMBERRESPONSE']._serialized_start=897
  _globals['_EXTENSIONNUMBERRESPONSE']._serialized_end=972
  _globals['_LISTSERVICERESPONSE']._serialized_start=974
  _globals['_LISTSERVICERESPONSE']._serialized_end=1049
  _globals['_SERVICERESPONSE']._serialized_start=1051
  _globals['_SERVICERESPONSE']._serialized_end=1082
  _globals['_ERRORRESPONSE']._serialized_start=1084
  _globals['_ERRORRESPONSE']._serialized_end=1142
  _globals['_SERVERREFLECTION']._serialized_start=1145
  _globals['_SERVERREFLECTION']._serialized_end=1282
# @@protoc_insertion_point(module_scope)
