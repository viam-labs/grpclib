# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpclib/channelz/v1/channelz.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"grpclib/channelz/v1/channelz.proto\x12\x10grpc.channelz.v1\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xfe\x01\n\x07\x43hannel\x12)\n\x03ref\x18\x01 \x01(\x0b\x32\x1c.grpc.channelz.v1.ChannelRef\x12+\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1d.grpc.channelz.v1.ChannelData\x12\x31\n\x0b\x63hannel_ref\x18\x03 \x03(\x0b\x32\x1c.grpc.channelz.v1.ChannelRef\x12\x37\n\x0esubchannel_ref\x18\x04 \x03(\x0b\x32\x1f.grpc.channelz.v1.SubchannelRef\x12/\n\nsocket_ref\x18\x05 \x03(\x0b\x32\x1b.grpc.channelz.v1.SocketRef\"\x84\x02\n\nSubchannel\x12,\n\x03ref\x18\x01 \x01(\x0b\x32\x1f.grpc.channelz.v1.SubchannelRef\x12+\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1d.grpc.channelz.v1.ChannelData\x12\x31\n\x0b\x63hannel_ref\x18\x03 \x03(\x0b\x32\x1c.grpc.channelz.v1.ChannelRef\x12\x37\n\x0esubchannel_ref\x18\x04 \x03(\x0b\x32\x1f.grpc.channelz.v1.SubchannelRef\x12/\n\nsocket_ref\x18\x05 \x03(\x0b\x32\x1b.grpc.channelz.v1.SocketRef\"\xbb\x01\n\x18\x43hannelConnectivityState\x12?\n\x05state\x18\x01 \x01(\x0e\x32\x30.grpc.channelz.v1.ChannelConnectivityState.State\"^\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\x0e\n\nCONNECTING\x10\x02\x12\t\n\x05READY\x10\x03\x12\x15\n\x11TRANSIENT_FAILURE\x10\x04\x12\x0c\n\x08SHUTDOWN\x10\x05\"\x8e\x02\n\x0b\x43hannelData\x12\x39\n\x05state\x18\x01 \x01(\x0b\x32*.grpc.channelz.v1.ChannelConnectivityState\x12\x0e\n\x06target\x18\x02 \x01(\t\x12-\n\x05trace\x18\x03 \x01(\x0b\x32\x1e.grpc.channelz.v1.ChannelTrace\x12\x15\n\rcalls_started\x18\x04 \x01(\x03\x12\x17\n\x0f\x63\x61lls_succeeded\x18\x05 \x01(\x03\x12\x14\n\x0c\x63\x61lls_failed\x18\x06 \x01(\x03\x12?\n\x1blast_call_started_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xdb\x02\n\x11\x43hannelTraceEvent\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12>\n\x08severity\x18\x02 \x01(\x0e\x32,.grpc.channelz.v1.ChannelTraceEvent.Severity\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0b\x63hannel_ref\x18\x04 \x01(\x0b\x32\x1c.grpc.channelz.v1.ChannelRefH\x00\x12\x39\n\x0esubchannel_ref\x18\x05 \x01(\x0b\x32\x1f.grpc.channelz.v1.SubchannelRefH\x00\"E\n\x08Severity\x12\x0e\n\nCT_UNKNOWN\x10\x00\x12\x0b\n\x07\x43T_INFO\x10\x01\x12\x0e\n\nCT_WARNING\x10\x02\x12\x0c\n\x08\x43T_ERROR\x10\x03\x42\x0b\n\tchild_ref\"\x96\x01\n\x0c\x43hannelTrace\x12\x19\n\x11num_events_logged\x18\x01 \x01(\x03\x12\x36\n\x12\x63reation_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x06\x65vents\x18\x03 \x03(\x0b\x32#.grpc.channelz.v1.ChannelTraceEvent\"R\n\nChannelRef\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\tJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\t\"X\n\rSubchannelRef\x12\x15\n\rsubchannel_id\x18\x07 \x01(\x03\x12\x0c\n\x04name\x18\x08 \x01(\tJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07\"P\n\tSocketRef\x12\x11\n\tsocket_id\x18\x03 \x01(\x03\x12\x0c\n\x04name\x18\x04 \x01(\tJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\t\"P\n\tServerRef\x12\x11\n\tserver_id\x18\x05 \x01(\x03\x12\x0c\n\x04name\x18\x06 \x01(\tJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\t\"\x92\x01\n\x06Server\x12(\n\x03ref\x18\x01 \x01(\x0b\x32\x1b.grpc.channelz.v1.ServerRef\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.grpc.channelz.v1.ServerData\x12\x32\n\rlisten_socket\x18\x03 \x03(\x0b\x32\x1b.grpc.channelz.v1.SocketRef\"\xc2\x01\n\nServerData\x12-\n\x05trace\x18\x01 \x01(\x0b\x32\x1e.grpc.channelz.v1.ChannelTrace\x12\x15\n\rcalls_started\x18\x02 \x01(\x03\x12\x17\n\x0f\x63\x61lls_succeeded\x18\x03 \x01(\x03\x12\x14\n\x0c\x63\x61lls_failed\x18\x04 \x01(\x03\x12?\n\x1blast_call_started_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xf6\x01\n\x06Socket\x12(\n\x03ref\x18\x01 \x01(\x0b\x32\x1b.grpc.channelz.v1.SocketRef\x12*\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1c.grpc.channelz.v1.SocketData\x12(\n\x05local\x18\x03 \x01(\x0b\x32\x19.grpc.channelz.v1.Address\x12)\n\x06remote\x18\x04 \x01(\x0b\x32\x19.grpc.channelz.v1.Address\x12,\n\x08security\x18\x05 \x01(\x0b\x32\x1a.grpc.channelz.v1.Security\x12\x13\n\x0bremote_name\x18\x06 \x01(\t\"\xee\x04\n\nSocketData\x12\x17\n\x0fstreams_started\x18\x01 \x01(\x03\x12\x19\n\x11streams_succeeded\x18\x02 \x01(\x03\x12\x16\n\x0estreams_failed\x18\x03 \x01(\x03\x12\x15\n\rmessages_sent\x18\x04 \x01(\x03\x12\x19\n\x11messages_received\x18\x05 \x01(\x03\x12\x18\n\x10keep_alives_sent\x18\x06 \x01(\x03\x12G\n#last_local_stream_created_timestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n$last_remote_stream_created_timestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x1blast_message_sent_timestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x43\n\x1flast_message_received_timestamp\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x19local_flow_control_window\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12?\n\x1aremote_flow_control_window\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12.\n\x06option\x18\r \x03(\x0b\x32\x1e.grpc.channelz.v1.SocketOption\"\xe8\x02\n\x07\x41\x64\x64ress\x12?\n\rtcpip_address\x18\x01 \x01(\x0b\x32&.grpc.channelz.v1.Address.TcpIpAddressH\x00\x12;\n\x0buds_address\x18\x02 \x01(\x0b\x32$.grpc.channelz.v1.Address.UdsAddressH\x00\x12?\n\rother_address\x18\x03 \x01(\x0b\x32&.grpc.channelz.v1.Address.OtherAddressH\x00\x1a\x30\n\x0cTcpIpAddress\x12\x12\n\nip_address\x18\x01 \x01(\x0c\x12\x0c\n\x04port\x18\x02 \x01(\x05\x1a\x1e\n\nUdsAddress\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x1a\x41\n\x0cOtherAddress\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\t\n\x07\x61\x64\x64ress\"\xbe\x02\n\x08Security\x12-\n\x03tls\x18\x01 \x01(\x0b\x32\x1e.grpc.channelz.v1.Security.TlsH\x00\x12\x39\n\x05other\x18\x02 \x01(\x0b\x32(.grpc.channelz.v1.Security.OtherSecurityH\x00\x1a{\n\x03Tls\x12\x17\n\rstandard_name\x18\x01 \x01(\tH\x00\x12\x14\n\nother_name\x18\x02 \x01(\tH\x00\x12\x19\n\x11local_certificate\x18\x03 \x01(\x0c\x12\x1a\n\x12remote_certificate\x18\x04 \x01(\x0c\x42\x0e\n\x0c\x63ipher_suite\x1a\x42\n\rOtherSecurity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB\x07\n\x05model\"U\n\x0cSocketOption\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12(\n\nadditional\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"B\n\x13SocketOptionTimeout\x12+\n\x08\x64uration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"Q\n\x12SocketOptionLinger\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"\xae\x05\n\x13SocketOptionTcpInfo\x12\x12\n\ntcpi_state\x18\x01 \x01(\r\x12\x15\n\rtcpi_ca_state\x18\x02 \x01(\r\x12\x18\n\x10tcpi_retransmits\x18\x03 \x01(\r\x12\x13\n\x0btcpi_probes\x18\x04 \x01(\r\x12\x14\n\x0ctcpi_backoff\x18\x05 \x01(\r\x12\x14\n\x0ctcpi_options\x18\x06 \x01(\r\x12\x17\n\x0ftcpi_snd_wscale\x18\x07 \x01(\r\x12\x17\n\x0ftcpi_rcv_wscale\x18\x08 \x01(\r\x12\x10\n\x08tcpi_rto\x18\t \x01(\r\x12\x10\n\x08tcpi_ato\x18\n \x01(\r\x12\x14\n\x0ctcpi_snd_mss\x18\x0b \x01(\r\x12\x14\n\x0ctcpi_rcv_mss\x18\x0c \x01(\r\x12\x14\n\x0ctcpi_unacked\x18\r \x01(\r\x12\x13\n\x0btcpi_sacked\x18\x0e \x01(\r\x12\x11\n\ttcpi_lost\x18\x0f \x01(\r\x12\x14\n\x0ctcpi_retrans\x18\x10 \x01(\r\x12\x14\n\x0ctcpi_fackets\x18\x11 \x01(\r\x12\x1b\n\x13tcpi_last_data_sent\x18\x12 \x01(\r\x12\x1a\n\x12tcpi_last_ack_sent\x18\x13 \x01(\r\x12\x1b\n\x13tcpi_last_data_recv\x18\x14 \x01(\r\x12\x1a\n\x12tcpi_last_ack_recv\x18\x15 \x01(\r\x12\x11\n\ttcpi_pmtu\x18\x16 \x01(\r\x12\x19\n\x11tcpi_rcv_ssthresh\x18\x17 \x01(\r\x12\x10\n\x08tcpi_rtt\x18\x18 \x01(\r\x12\x13\n\x0btcpi_rttvar\x18\x19 \x01(\r\x12\x19\n\x11tcpi_snd_ssthresh\x18\x1a \x01(\r\x12\x15\n\rtcpi_snd_cwnd\x18\x1b \x01(\r\x12\x13\n\x0btcpi_advmss\x18\x1c \x01(\r\x12\x17\n\x0ftcpi_reordering\x18\x1d \x01(\r\"F\n\x15GetTopChannelsRequest\x12\x18\n\x10start_channel_id\x18\x01 \x01(\x03\x12\x13\n\x0bmax_results\x18\x02 \x01(\x03\"Q\n\x16GetTopChannelsResponse\x12*\n\x07\x63hannel\x18\x01 \x03(\x0b\x32\x19.grpc.channelz.v1.Channel\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x08\"A\n\x11GetServersRequest\x12\x17\n\x0fstart_server_id\x18\x01 \x01(\x03\x12\x13\n\x0bmax_results\x18\x02 \x01(\x03\"K\n\x12GetServersResponse\x12(\n\x06server\x18\x01 \x03(\x0b\x32\x18.grpc.channelz.v1.Server\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x08\"%\n\x10GetServerRequest\x12\x11\n\tserver_id\x18\x01 \x01(\x03\"=\n\x11GetServerResponse\x12(\n\x06server\x18\x01 \x01(\x0b\x32\x18.grpc.channelz.v1.Server\"Z\n\x17GetServerSocketsRequest\x12\x11\n\tserver_id\x18\x01 \x01(\x03\x12\x17\n\x0fstart_socket_id\x18\x02 \x01(\x03\x12\x13\n\x0bmax_results\x18\x03 \x01(\x03\"X\n\x18GetServerSocketsResponse\x12/\n\nsocket_ref\x18\x01 \x03(\x0b\x32\x1b.grpc.channelz.v1.SocketRef\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x08\"\'\n\x11GetChannelRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\"@\n\x12GetChannelResponse\x12*\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\x19.grpc.channelz.v1.Channel\"-\n\x14GetSubchannelRequest\x12\x15\n\rsubchannel_id\x18\x01 \x01(\x03\"I\n\x15GetSubchannelResponse\x12\x30\n\nsubchannel\x18\x01 \x01(\x0b\x32\x1c.grpc.channelz.v1.Subchannel\"6\n\x10GetSocketRequest\x12\x11\n\tsocket_id\x18\x01 \x01(\x03\x12\x0f\n\x07summary\x18\x02 \x01(\x08\"=\n\x11GetSocketResponse\x12(\n\x06socket\x18\x01 \x01(\x0b\x32\x18.grpc.channelz.v1.Socket2\x9a\x05\n\x08\x43hannelz\x12\x63\n\x0eGetTopChannels\x12\'.grpc.channelz.v1.GetTopChannelsRequest\x1a(.grpc.channelz.v1.GetTopChannelsResponse\x12W\n\nGetServers\x12#.grpc.channelz.v1.GetServersRequest\x1a$.grpc.channelz.v1.GetServersResponse\x12T\n\tGetServer\x12\".grpc.channelz.v1.GetServerRequest\x1a#.grpc.channelz.v1.GetServerResponse\x12i\n\x10GetServerSockets\x12).grpc.channelz.v1.GetServerSocketsRequest\x1a*.grpc.channelz.v1.GetServerSocketsResponse\x12W\n\nGetChannel\x12#.grpc.channelz.v1.GetChannelRequest\x1a$.grpc.channelz.v1.GetChannelResponse\x12`\n\rGetSubchannel\x12&.grpc.channelz.v1.GetSubchannelRequest\x1a\'.grpc.channelz.v1.GetSubchannelResponse\x12T\n\tGetSocket\x12\".grpc.channelz.v1.GetSocketRequest\x1a#.grpc.channelz.v1.GetSocketResponseBX\n\x13io.grpc.channelz.v1B\rChannelzProtoP\x01Z0google.golang.org/grpc/channelz/grpc_channelz_v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpclib.channelz.v1.channelz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023io.grpc.channelz.v1B\rChannelzProtoP\001Z0google.golang.org/grpc/channelz/grpc_channelz_v1'
  _globals['_CHANNEL']._serialized_start=181
  _globals['_CHANNEL']._serialized_end=435
  _globals['_SUBCHANNEL']._serialized_start=438
  _globals['_SUBCHANNEL']._serialized_end=698
  _globals['_CHANNELCONNECTIVITYSTATE']._serialized_start=701
  _globals['_CHANNELCONNECTIVITYSTATE']._serialized_end=888
  _globals['_CHANNELCONNECTIVITYSTATE_STATE']._serialized_start=794
  _globals['_CHANNELCONNECTIVITYSTATE_STATE']._serialized_end=888
  _globals['_CHANNELDATA']._serialized_start=891
  _globals['_CHANNELDATA']._serialized_end=1161
  _globals['_CHANNELTRACEEVENT']._serialized_start=1164
  _globals['_CHANNELTRACEEVENT']._serialized_end=1511
  _globals['_CHANNELTRACEEVENT_SEVERITY']._serialized_start=1429
  _globals['_CHANNELTRACEEVENT_SEVERITY']._serialized_end=1498
  _globals['_CHANNELTRACE']._serialized_start=1514
  _globals['_CHANNELTRACE']._serialized_end=1664
  _globals['_CHANNELREF']._serialized_start=1666
  _globals['_CHANNELREF']._serialized_end=1748
  _globals['_SUBCHANNELREF']._serialized_start=1750
  _globals['_SUBCHANNELREF']._serialized_end=1838
  _globals['_SOCKETREF']._serialized_start=1840
  _globals['_SOCKETREF']._serialized_end=1920
  _globals['_SERVERREF']._serialized_start=1922
  _globals['_SERVERREF']._serialized_end=2002
  _globals['_SERVER']._serialized_start=2005
  _globals['_SERVER']._serialized_end=2151
  _globals['_SERVERDATA']._serialized_start=2154
  _globals['_SERVERDATA']._serialized_end=2348
  _globals['_SOCKET']._serialized_start=2351
  _globals['_SOCKET']._serialized_end=2597
  _globals['_SOCKETDATA']._serialized_start=2600
  _globals['_SOCKETDATA']._serialized_end=3222
  _globals['_ADDRESS']._serialized_start=3225
  _globals['_ADDRESS']._serialized_end=3585
  _globals['_ADDRESS_TCPIPADDRESS']._serialized_start=3427
  _globals['_ADDRESS_TCPIPADDRESS']._serialized_end=3475
  _globals['_ADDRESS_UDSADDRESS']._serialized_start=3477
  _globals['_ADDRESS_UDSADDRESS']._serialized_end=3507
  _globals['_ADDRESS_OTHERADDRESS']._serialized_start=3509
  _globals['_ADDRESS_OTHERADDRESS']._serialized_end=3574
  _globals['_SECURITY']._serialized_start=3588
  _globals['_SECURITY']._serialized_end=3906
  _globals['_SECURITY_TLS']._serialized_start=3706
  _globals['_SECURITY_TLS']._serialized_end=3829
  _globals['_SECURITY_OTHERSECURITY']._serialized_start=3831
  _globals['_SECURITY_OTHERSECURITY']._serialized_end=3897
  _globals['_SOCKETOPTION']._serialized_start=3908
  _globals['_SOCKETOPTION']._serialized_end=3993
  _globals['_SOCKETOPTIONTIMEOUT']._serialized_start=3995
  _globals['_SOCKETOPTIONTIMEOUT']._serialized_end=4061
  _globals['_SOCKETOPTIONLINGER']._serialized_start=4063
  _globals['_SOCKETOPTIONLINGER']._serialized_end=4144
  _globals['_SOCKETOPTIONTCPINFO']._serialized_start=4147
  _globals['_SOCKETOPTIONTCPINFO']._serialized_end=4833
  _globals['_GETTOPCHANNELSREQUEST']._serialized_start=4835
  _globals['_GETTOPCHANNELSREQUEST']._serialized_end=4905
  _globals['_GETTOPCHANNELSRESPONSE']._serialized_start=4907
  _globals['_GETTOPCHANNELSRESPONSE']._serialized_end=4988
  _globals['_GETSERVERSREQUEST']._serialized_start=4990
  _globals['_GETSERVERSREQUEST']._serialized_end=5055
  _globals['_GETSERVERSRESPONSE']._serialized_start=5057
  _globals['_GETSERVERSRESPONSE']._serialized_end=5132
  _globals['_GETSERVERREQUEST']._serialized_start=5134
  _globals['_GETSERVERREQUEST']._serialized_end=5171
  _globals['_GETSERVERRESPONSE']._serialized_start=5173
  _globals['_GETSERVERRESPONSE']._serialized_end=5234
  _globals['_GETSERVERSOCKETSREQUEST']._serialized_start=5236
  _globals['_GETSERVERSOCKETSREQUEST']._serialized_end=5326
  _globals['_GETSERVERSOCKETSRESPONSE']._serialized_start=5328
  _globals['_GETSERVERSOCKETSRESPONSE']._serialized_end=5416
  _globals['_GETCHANNELREQUEST']._serialized_start=5418
  _globals['_GETCHANNELREQUEST']._serialized_end=5457
  _globals['_GETCHANNELRESPONSE']._serialized_start=5459
  _globals['_GETCHANNELRESPONSE']._serialized_end=5523
  _globals['_GETSUBCHANNELREQUEST']._serialized_start=5525
  _globals['_GETSUBCHANNELREQUEST']._serialized_end=5570
  _globals['_GETSUBCHANNELRESPONSE']._serialized_start=5572
  _globals['_GETSUBCHANNELRESPONSE']._serialized_end=5645
  _globals['_GETSOCKETREQUEST']._serialized_start=5647
  _globals['_GETSOCKETREQUEST']._serialized_end=5701
  _globals['_GETSOCKETRESPONSE']._serialized_start=5703
  _globals['_GETSOCKETRESPONSE']._serialized_end=5764
  _globals['_CHANNELZ']._serialized_start=5767
  _globals['_CHANNELZ']._serialized_end=6433
# @@protoc_insertion_point(module_scope)
