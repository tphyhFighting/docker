# coding:utf-8

import time
import urllib2
import json
import requests
import StringIO
import gzip

from protos import log_request_pb2

url = "http://localhost:8080/m/v1/log/"
lr = log_request_pb2.LogRequest()
data = {"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item0"}
#

for i in range(0, 20):
    l = log_request_pb2.Log()
    l.type = str(i)
    l.logData = json.dumps(data)
    # l.delayTimeMs = int(time.time())
    l.delayTimeMs = 128
    # print(l.delayTimeMs)
    lr.logs._values.append(l)

# print(ll.SerializeToString)

def dataGzip(data):
    s = StringIO.StringIO()
    g = gzip.GzipFile(fileobj=s, mode='w')
    g.write(data)
    g.close()
    gzipped_body = s.getvalue()
    # print('len:',s.len)
    request_body = gzipped_body
    return request_body

def test_zip_json(lr):
    if not isinstance(lr, log_request_pb2.LogRequest):
        return
    s = lr.SerializeToString()
    arg = {
        "application_id":"aa",
        "client_version":"v1.7",
        "device_brand":"b",
        "device_model":"b2",
        "flavor":"b3",
        "sdk_version":"b4",
        "supported_abis":["b5", "b6'"],
        "argument":s,
    }
    arg_str = json.dumps(arg)
    print arg_str
    s = dataGzip(arg_str)
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'gzip')
    # 发送压缩后数据
    resp = requests.post(url, s, headers = req.headers)
    print(resp.content)
    print(resp)

def test_unzip(lr):
    if not isinstance(lr, log_request_pb2.LogRequest):
        return
    s = lr.SerializeToString()
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'ungzip')
    # 发送压缩后数据
    resp = requests.post(url, s, headers = req.headers)
    print(resp.content)
    print(resp)

def test_zip(lr):
    if not isinstance(lr, log_request_pb2.LogRequest):
        return
    s = lr.SerializeToString()
    # arg["argument"] = s
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'gzip')
    # 发送压缩后数据
    print("slenunzip:", len(s))
    s = dataGzip(s)
    print("s:", s)
    print("slenzip:", len(s))

    resp = requests.post(url, s, headers = req.headers)
    print(resp.content)
    pass

def main():
    global lr
    # test_unzip(lr)
    test_zip(lr)
    # test_zip_json(lr)




if __name__ == '__main__':
    main()

#  {
#      [
#          type:"0"
#          logData:"{\"versionCode\": \"1\", \"data\": \"item0\", \"sysVersion\": \"6.0\", \"apkVersion\": \"1.2.3\", \"channelID\": \"843984932\"}"
#          delayTimeMs:1488712159
#
#         type:"1"
#         logData:"{\"versionCode\": \"1\", \"data\": \"item0\", \"sysVersion\": \"6.0\", \"apkVersion\": \"1.2.3\", \"channelID\": \"843984932\"}"
#         delayTimeMs:1488712159
#
#         type:"2"
#         logData:"{\"versionCode\": \"1\", \"data\": \"item0\", \"sysVersion\": \"6.0\", \"apkVersion\": \"1.2.3\", \"channelID\": \"843984932\"}"
#         delayTimeMs:1488712159
#
#         type:"3"
#         logData:"{\"versionCode\": \"1\", \"data\": \"item0\", \"sysVersion\": \"6.0\", \"apkVersion\": \"1.2.3\", \"channelID\": \"843984932\"}"
#         delayTimeMs:1488712159
#
#         type:"4"
#         logData:"{\"versionCode\": \"1\", \"data\": \"item0\", \"sysVersion\": \"6.0\", \"apkVersion\": \"1.2.3\", \"channelID\": \"843984932\"}"
#         delayTimeMs:1488712159
#
#         type:"5"
#         logData:"{\"versionCode\": \"1\", \"data\": \"item0\", \"sysVersion\": \"6.0\", \"apkVersion\": \"1.2.3\", \"channelID\": \"843984932\"}"
#         delayTimeMs:1488712159
#      ]
# }

