"""The Python implementation of the GRPC youtube.watch client."""
from __future__ import print_function

import grpc

import youtube_pb2
import youtube_pb2_grpc


def main():
    channel = grpc.insecure_channel('192.168.0.41:5001')
    stub = youtube_pb2_grpc.GreeterStub(channel)
    print("stub:", stub)
    resp = stub.YoutubeWatch(
        youtube_pb2.YoutubeWatchRequest(link="https://www.youtube.com/watch?v=F--SV-2A1x4&spfreload=10"))
    print(resp.Title)
    # for k, v in resp._fields:
    #     print("k:{} v:{}".format(k, v))

if __name__ == '__main__':
    main()
