#protobuf 使用


##0x01 cli(python)
    python 作为cli 发送gzip压缩后的protobuf给ser
    1.实例msg
    2.赋值
    3.序列化
    4.gzip
    5.post 发送
```python
# coding:utf-8
import time
import urllib2
import json
import requests
import StringIO
import gzip

from protos import log_request_pb2

url = "http://localhost:8080/v1/log/"
l = log_request_pb2.Log()
data = {"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item0"}
l.type = "app"
# l.logData = bytes(data)   #影响 " -> \'
l.logData = json.dumps(data)
# print("logData:", l.logData)
l.delayTimeMs = int(time.time())

def dataGzip(data):
    s = StringIO.StringIO()
    g = gzip.GzipFile(fileobj=s, mode='w')
    g.write(data)
    g.close()
    gzipped_body = s.getvalue()
    request_body = gzipped_body
    return request_body

def test_unzip(l):
    if not isinstance(l, log_request_pb2.Log):
        return
    s = l.SerializeToString()
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'ungzip')
    resp = requests.post(url, s, headers = req.headers)
    # resp = requests.post(url, s)
    print(resp)

def test_zip(l):
    if not isinstance(l, log_request_pb2.Log):
        return
    s = l.SerializeToString()
    req = urllib2.Request(url)
    req.add_header('Accept-encoding', 'gzip')
    # req.add_header('Content-Type', 'application/json')
    # 发送压缩后数据
    s = dataGzip(s)
    resp = requests.post(url, s, headers = req.headers)
    print(resp.content)
    pass

def main():
    global l
    # test_unzip(l)
    test_zip(l)



if __name__ == '__main__':
    main()
    
```

##0x02 ser(go)


