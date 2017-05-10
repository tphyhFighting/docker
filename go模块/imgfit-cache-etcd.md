#### 使用etcd v3测试

#### step1. etcd 启动
```bash
export ETCDCTL_API=3
etcd --name infra0 --data-dir infra0    --advertise-client-urls=http://127.0.0.1:2379 --listen-client-urls http://0.0.0.0:2379
自行对etcd服务验证.
```

#### step2. imgfit
```bash
[root@test2 imgfit]# cat conf/app.conf
appname = imgfit
httpport = 7000
cachenable = false      #imgfit 不需要开启
cacheport = 9000
cachename = "imgcache"
cachesize = 67108864
cachepeekselfip = "192.168.6.1"
cachepeekselfipprefx = "192."
cacheetcdendpoint = "http://127.0.0.1:2379"
cacheimgfitapi = "http://127.0.0.1:7000"
runmode = dev
autorender = false
copyrequestbody = true
EnableDocs = true
[root@test2 imgfit]#
docker run --name imgfit  -d --restart always  -p 8000:8000   -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache
```
##### 2.1 imgfit test
```bash
在服务器上使用微信图片地址测试:
urlhttps://image.winudf.com/v2/image/Y29tLnRlbmNlbnQubW1faWNvbl8xbWx5aGd2Yw/icon.png?w=130&fakeurl=1&type=.png
urlpath:/v2/image/Y29tLnRlbmNlbnQubW1faWNvbl8xbWx5aGd2Yw/icon.png
[root@test2 ~]# curl  -I -X GET http://localhost:7000/v2/image/imgcache/0002.webp
HTTP/1.1 200 OK
Server: beegoServer:1.8.0
Date: Wed, 10 May 2017 07:32:34 GMT
Content-Type: image/webp
Transfer-Encoding: chunked
[root@test2 ~]#
```

#### step3. imgfit-cache 启动

##### 0.配置文件conf/app.conf
```bash
[root@test2 test]# cat conf/app.conf
appname = imgfit
httpport = 8000
cacheport = 9000
cachenable = true           #imgfit-cache 必须配置为true
cachename = "imgcache"      #注册到etcdkv 中的前缀
cachesize = 67108864        #groupcache 大小
cachepeekselfip = "192.168.6.1" #建议直接指定，如果为空，请使用network=host模式
cachepeekselfipprefx = "192."   #getip()获取根据net.interface()获取前缀为192开头的网络ip
cacheetcdendpoint = "http://192.168.6.1:2379"#etcd的服务地址
cacheimgfitapi = "http://127.0.0.1:8000"     #imgfit图片缩放服务器地址, 如果使用非host网络，自行修改.--link imgfit=imgfit "http://imgfit:7000"
runmode = dev
autorender = false
copyrequestbody = true
```
##### 1.使用--link连接imgfit容器, cacheimgfitapi = "http://imgfit:8000"
```bash
docker run -it --name imgfit-cache -p 9000:9000 --link imgfit:imgfit -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  imgfit bash
```
##### 2.使用--network=host, cacheimgfitapi = "http://127.0.0.1:8000"
```bash
docker run --name imgfit-cache  -d --restart always  --network=host   -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache
```

##### test
```bash
➜  ~ curl -I localhost:9000/health
HTTP/1.1 200 OK
Date: Wed, 10 May 2017 07:04:34 GMT
Content-Type: text/plain; charset=utf-8
➜  ~
```
