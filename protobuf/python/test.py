# coding:utf-8
import time
import urllib
import urllib2
import json
import requests
import StringIO
import gzip
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from protos import log_request_pb2

# register_openers()
# datagen, headers = multipart_encode()
# print datagen, headers

url = "http://192.168.9.41:8080/m/v1/log/"
lr = log_request_pb2.LogRequest()
# data = {"sysVersion": "6.0", "apkVersion": "1.2.3",
#         "channelID": "843984932", "versionCode": "1", "data": "item0"}
data = "item2"
arg = {
    "application_id": "com.apkpure.aegon",
    "client_version": int(883),
    "device_brand": "google",
    "device_model": "Nexus 5",
    "flavor": "aa",
    "sdk_version": int(23),
    # "supported_abis[]": ["armeabi-v7a", "armeabi"]
    # "supported_abis": ["armeabi-v7a", "armeabi", "22", "33"]
}


def dataGzip(data):
    s = StringIO.StringIO()
    g = gzip.GzipFile(fileobj=s, mode='w')
    g.write(data)
    g.close()
    gzipped_body = s.getvalue()
    # print('len:',s.len)
    request_body = gzipped_body
    return request_body


def init():
    global lr
    for i in range(0, 20):
        l = log_request_pb2.Log()
        l.type = str(i)
        # l.logData = json.dumps(data)
        l.logData = str(data)
        # l.delayTimeMs = int(time.time())
        l.delayTimeMs = int(10)
        # l.delayTimeMs = 128
        # print(l.delayTimeMs)
        lr.logs._values.append(l)


def test_zip(lr):
    if not isinstance(lr, log_request_pb2.LogRequest):
        return
    s = lr.SerializeToString()
    # arg["argument"] = s
    global url
    url = url + "?" + urllib.urlencode(arg)
    print("url:", url)
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'gzip')
    # 发送压缩后数据
    print("slenunzip:", len(s))
    s = dataGzip(s)
    print("s:", s)
    print("slenzip:", len(s))
    resp = requests.post(url, s, headers=req.headers)
    print(resp.content)
    print(resp)


def test_zip_arg(lr):
    if not isinstance(lr, log_request_pb2.LogRequest):
        return
    s = lr.SerializeToString()
    global url
    url = url + "?" + urllib.urlencode(arg)
    url = "http://localhost:8080/m/v1/log/?" \
          "application_id=com.apkpure.aegon&device_model=Nexus%205&" \
          "supported_abis=%27armeabi-v7a%27&supported_abis=%20%27armeabi%27&supported_abis=%20%2722%27&" \
          "sdk_version=23&device_brand=google&client_version=111&flavor=aa"
    req = urllib2.Request(url)
    print("url:", url)
    req.add_header('Accept-encoding', 'gzip')
    s = dataGzip(s)
    resp = requests.post(url, s, headers=req.headers)
    print(resp.content)
    print(resp)


def test_zip_arg_json(lr):
    if not isinstance(lr, log_request_pb2.LogRequest):
        return
    # delay time
    # for l in lr.logs._values:
    #
    s = lr.SerializeToString()
    global url
    # url = "{}?arg={}".format(url,json.dumps(arg))
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'gzip')
    # 发送压缩后数据
    s = dataGzip(s)
    resp = requests.post(url, s, headers=req.headers)
    print(resp.content)
    print(resp)
    pass


def main():
    global lr
    init()
    # test_zip(lr)
    test_zip_arg(lr)
    # test_zip_arg_son(lr)

if __name__ == '__main__':
    main()
