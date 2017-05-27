// Code generated by protoc-gen-go.
// source: protos/youtube.proto
// DO NOT EDIT!

/*
Package protos is a generated protocol buffer package.

It is generated from these files:
	protos/youtube.proto

It has these top-level messages:
	YoutubeWatchRequest
	YoutubeWatchReply
*/
package protos

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// The request message containing the user's name.
type YoutubeWatchRequest struct {
	Link string `protobuf:"bytes,1,opt,name=link" json:"link,omitempty"`
}

func (m *YoutubeWatchRequest) Reset()                    { *m = YoutubeWatchRequest{} }
func (m *YoutubeWatchRequest) String() string            { return proto.CompactTextString(m) }
func (*YoutubeWatchRequest) ProtoMessage()               {}
func (*YoutubeWatchRequest) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func (m *YoutubeWatchRequest) GetLink() string {
	if m != nil {
		return m.Link
	}
	return ""
}

// The response message containing the greetings
type YoutubeWatchReply struct {
	Id                 string `protobuf:"bytes,1,opt,name=Id" json:"Id,omitempty"`
	Title              string `protobuf:"bytes,2,opt,name=Title" json:"Title,omitempty"`
	ThumbnailUrl       string `protobuf:"bytes,3,opt,name=ThumbnailUrl" json:"ThumbnailUrl,omitempty"`
	ThumbnailFid       string `protobuf:"bytes,4,opt,name=ThumbnailFid" json:"ThumbnailFid,omitempty"`
	ThumbnailImgFitApi string `protobuf:"bytes,5,opt,name=ThumbnailImgFitApi" json:"ThumbnailImgFitApi,omitempty"`
	LengthSeconds      string `protobuf:"bytes,6,opt,name=LengthSeconds" json:"LengthSeconds,omitempty"`
}

func (m *YoutubeWatchReply) Reset()                    { *m = YoutubeWatchReply{} }
func (m *YoutubeWatchReply) String() string            { return proto.CompactTextString(m) }
func (*YoutubeWatchReply) ProtoMessage()               {}
func (*YoutubeWatchReply) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{1} }

func (m *YoutubeWatchReply) GetId() string {
	if m != nil {
		return m.Id
	}
	return ""
}

func (m *YoutubeWatchReply) GetTitle() string {
	if m != nil {
		return m.Title
	}
	return ""
}

func (m *YoutubeWatchReply) GetThumbnailUrl() string {
	if m != nil {
		return m.ThumbnailUrl
	}
	return ""
}

func (m *YoutubeWatchReply) GetThumbnailFid() string {
	if m != nil {
		return m.ThumbnailFid
	}
	return ""
}

func (m *YoutubeWatchReply) GetThumbnailImgFitApi() string {
	if m != nil {
		return m.ThumbnailImgFitApi
	}
	return ""
}

func (m *YoutubeWatchReply) GetLengthSeconds() string {
	if m != nil {
		return m.LengthSeconds
	}
	return ""
}

func init() {
	proto.RegisterType((*YoutubeWatchRequest)(nil), "protos.YoutubeWatchRequest")
	proto.RegisterType((*YoutubeWatchReply)(nil), "protos.YoutubeWatchReply")
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// Client API for Greeter service

type GreeterClient interface {
	// Sends a greeting
	YoutubeWatch(ctx context.Context, in *YoutubeWatchRequest, opts ...grpc.CallOption) (*YoutubeWatchReply, error)
}

type greeterClient struct {
	cc *grpc.ClientConn
}

func NewGreeterClient(cc *grpc.ClientConn) GreeterClient {
	return &greeterClient{cc}
}

func (c *greeterClient) YoutubeWatch(ctx context.Context, in *YoutubeWatchRequest, opts ...grpc.CallOption) (*YoutubeWatchReply, error) {
	out := new(YoutubeWatchReply)
	err := grpc.Invoke(ctx, "/protos.Greeter/YoutubeWatch", in, out, c.cc, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// Server API for Greeter service

type GreeterServer interface {
	// Sends a greeting
	YoutubeWatch(context.Context, *YoutubeWatchRequest) (*YoutubeWatchReply, error)
}

func RegisterGreeterServer(s *grpc.Server, srv GreeterServer) {
	s.RegisterService(&_Greeter_serviceDesc, srv)
}

func _Greeter_YoutubeWatch_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(YoutubeWatchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(GreeterServer).YoutubeWatch(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/protos.Greeter/YoutubeWatch",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(GreeterServer).YoutubeWatch(ctx, req.(*YoutubeWatchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Greeter_serviceDesc = grpc.ServiceDesc{
	ServiceName: "protos.Greeter",
	HandlerType: (*GreeterServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "YoutubeWatch",
			Handler:    _Greeter_YoutubeWatch_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "protos/youtube.proto",
}

func init() { proto.RegisterFile("protos/youtube.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 255 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x09, 0x6e, 0x88, 0x02, 0xff, 0x6c, 0x91, 0x41, 0x4b, 0xc3, 0x30,
	0x18, 0x86, 0x6d, 0xdd, 0x26, 0x7e, 0x4c, 0x61, 0x9f, 0x3b, 0x44, 0xbd, 0x48, 0x11, 0xd1, 0x4b,
	0x05, 0xfd, 0x05, 0xee, 0x50, 0x2d, 0x78, 0x90, 0x6d, 0x22, 0x1e, 0xdb, 0x26, 0xac, 0x61, 0x69,
	0x13, 0xd3, 0xe4, 0xd0, 0x5f, 0xea, 0xdf, 0x11, 0x93, 0x21, 0x66, 0xf4, 0x96, 0xf7, 0x79, 0x9f,
	0x4b, 0xde, 0x0f, 0xe6, 0x4a, 0x4b, 0x23, 0xbb, 0xfb, 0x5e, 0x5a, 0x63, 0x4b, 0x96, 0xba, 0x88,
	0x13, 0x4f, 0x93, 0x3b, 0x38, 0xfb, 0xf4, 0xc5, 0x47, 0x61, 0xaa, 0x7a, 0xc9, 0xbe, 0x2c, 0xeb,
	0x0c, 0x22, 0x8c, 0x04, 0x6f, 0xb7, 0x24, 0xba, 0x8a, 0x6e, 0x8f, 0x97, 0xee, 0x9d, 0x7c, 0x47,
	0x30, 0x0b, 0x5d, 0x25, 0x7a, 0x3c, 0x85, 0x38, 0xa7, 0x3b, 0x2f, 0xce, 0x29, 0xce, 0x61, 0xbc,
	0xe6, 0x46, 0x30, 0x12, 0x3b, 0xe4, 0x03, 0x26, 0x30, 0x5d, 0xd7, 0xb6, 0x29, 0xdb, 0x82, 0x8b,
	0x77, 0x2d, 0xc8, 0xa1, 0x2b, 0x03, 0x16, 0x38, 0x19, 0xa7, 0x64, 0xb4, 0xe7, 0x64, 0x9c, 0x62,
	0x0a, 0xf8, 0x97, 0xf3, 0x66, 0x93, 0x71, 0xf3, 0xa4, 0x38, 0x19, 0x3b, 0x73, 0xa0, 0xc1, 0x6b,
	0x38, 0x79, 0x65, 0xed, 0xc6, 0xd4, 0x2b, 0x56, 0xc9, 0x96, 0x76, 0x64, 0xe2, 0xd4, 0x10, 0x3e,
	0xac, 0xe0, 0xe8, 0x59, 0x33, 0x66, 0x98, 0xc6, 0x17, 0x98, 0xfe, 0xff, 0x23, 0x5e, 0xfa, 0xbd,
	0xba, 0x74, 0x60, 0xa5, 0x8b, 0xf3, 0xe1, 0x52, 0x89, 0x3e, 0x39, 0x58, 0xdc, 0xc0, 0xac, 0x92,
	0x4d, 0x5a, 0xa8, 0xad, 0xb2, 0x7a, 0x37, 0xfb, 0x22, 0x18, 0xf0, 0xed, 0x17, 0x95, 0xfe, 0x12,
	0x8f, 0x3f, 0x01, 0x00, 0x00, 0xff, 0xff, 0x2a, 0xed, 0xa6, 0xa2, 0xa8, 0x01, 0x00, 0x00,
}