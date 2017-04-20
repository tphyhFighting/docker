##### 构想
```bash
9000: 缓存服务器.
ser-cache-> ip1:9000
ser-cache-> ip2:9000
ser-cache-> ip3:9000

8000: 图片缩放服务器.
ser-imgfit-> ip1:8000
ser-imgfit-> ip2:8000
ser-imgfit-> ip3:8000

etcd:管理节点注册服务.
groupcache:分布式缓存

                        cli 请求K
                            | 
                           | | 
    ===============================================
    ip1:9000            ip2:9000            ip3:9000
       ||                  ||                 ||
       ||                  ||                 ||
                    1.查本地cache, hint返回.
      ------            --------            --------
      LRU1              LRU2                LRU3
      kp11              kp21                kp31
      kp12              kp22                kp32
      ...               ...                 ...
      ------            --------            --------
       ||                  ||                 ||
       ||                  ||                 ||
      ----------------------------------------------
                    2.通过一致性Hash，找到存储K的节点.
                        H(K)-->p1/2/3
      ----------------------------------------------
                    2.1 查本节点cache, hint返回数据.
                    2.2 如果本节点hint失败，回调getter，访问8000, 获取数据
                    2.3 缓存数据在当前节点
                    2.4 拿到数据后返回
      ----------------------------------------------
       ||                  ||                 ||
       ||                  ||                 ||
    ip1:8000            ip2:8000         ip3:8000
    
所有节点直接可以正常访问。 所有节点都可以访问本节点的图像服务.

```

#### step1.开启虚拟机的特定端口
```bash
firewall-cmd --zone=public --add-port=2379/tcp --permanent
firewall-cmd --zone=public --add-port=2380/tcp --permanent
firewall-cmd --zone=public --add-port=9000/tcp --permanent
firewall-cmd --zone=public --add-port=8000/tcp --permanent
firewall-cmd --reload
```


#### step2.启动ip1/2/3, 上的imgfit图像缩放服务
```bash
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -it -p 8000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/build/conf:/app/conf  imgfit bash
```

#### step3 etcd部署
##### 3.1 启动三台节点
```bash
ip1-->etcd0=http://192.168.9.37:2380
ip2-->etcd1=http://192.168.9.99:2380
ip3-->etcd2=http://192.168.9.41:2380 

启动脚本:
etcd -name etcd0 -initial-advertise-peer-urls http://192.168.9.37:2380 \
  -listen-peer-urls http://192.168.9.37:2380 \
  -listen-client-urls http://192.168.9.37:2379,http://127.0.0.1:2379 \
  -advertise-client-urls http://192.168.9.37:2379 \
  -initial-cluster-token my-etcd-cluster \
  -initial-cluster etcd0=http://192.168.9.37:2380,etcd1=http://192.168.9.99:2380,etcd2=http://192.168.9.41:2380 \
  -initial-cluster-state new

etcd -name etcd2 -initial-advertise-peer-urls http://192.168.9.41:2380 \
    -listen-peer-urls http://192.168.9.41:2380 \
    -listen-client-urls http://192.168.9.41:2379,http://127.0.0.1:2379 \
    -advertise-client-urls http://192.168.9.41:2379 \
    -initial-cluster-token my-etcd-cluster \
    -initial-cluster etcd0=http://192.168.9.37:2380,etcd1=http://192.168.9.99:2380,etcd2=http://192.168.9.41:2380 \
    -initial-cluster-state new

etcd -name etcd1 -initial-advertise-peer-urls http://192.168.9.99:2380 \
    -listen-peer-urls http://192.168.9.99:2380 \
    -listen-client-urls http://192.168.9.99:2379,http://127.0.0.1:2379 \
    -advertise-client-urls http://192.168.9.99:2379 \
    -initial-cluster-token my-etcd-cluster \
    -initial-cluster etcd0=http://192.168.9.37:2380,etcd1=http://192.168.9.99:2380,etcd2=http://192.168.9.41:2380 \
    -initial-cluster-state new
```
##### 3.2 查看节点成员
```bash
➜  ~ etcdctl member list
4af0a3b2552ca31: name=etcd2 peerURLs=http://192.168.9.41:2380 clientURLs=http://192.168.9.41:2379 isLeader=true
5265a651acb4a72e: name=etcd0 peerURLs=http://192.168.9.37:2380 clientURLs=http://192.168.9.37:2379 isLeader=false
df1c14c0132a3287: name=etcd1 peerURLs=http://192.168.9.99:2380 clientURLs=http://192.168.9.99:2379 isLeader=false
➜  ~
```
##### 3.3 启动程序imgfit-cache. 使用etcd的clientapi完成节点注册.
```bash
k: ip:9000
v: ip:9000

➜  ~ etcdctl ls /imgcache2/nodes
/imgcache2/nodes/http:__192.168.9.37:9000
/imgcache2/nodes/http:__192.168.9.99:9000
/imgcache2/nodes/http:__192.168.9.41:9000
➜  ~ etcdctl get /imgcache2/nodes/http:__192.168.9.41:9000
http://192.168.9.41:9000
➜  ~
➜  ~ etcdctl get /imgcache2/nodes/http:__192.168.9.39:9000
http://192.168.9.39:9000
➜  ~ etcdctl get /imgcache2/nodes/http:__192.168.9.99:9000
http://192.168.9.99:9000

每个节点注册后，通过getNodes获取到v列表，加入到peek中。
```

###### 3.4 imgfit-cache: 开启一个go程， watch 监测etcd节点变化, 发现新的节点就会完成peek注册
```bash
2017/04/20 19:20:07 [I] [root.go:37] Cache name : 	imgcache2
2017/04/20 19:20:07 [I] [root.go:38] Cache size : 	67108864
HTTPPool.PickPeer self:http://192.168.9.41:9000 begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
RegisterPeerPicker: start
RegisterPeerPicker: end fn:0x44a7260
HTTPPool.PickPeer self:http://192.168.9.41:9000 end
2017/04/20 19:20:07 [D] [discovery.go:47] NewServiceRegistry sr:{0xc420174780 imgcache2 0xc420070230} cfg:{[http://192.168.9.41:2379] 0x4bb91e0 <nil>   1s 0} end
2017/04/20 19:20:07 [D] [cache.go:137] add :http://192.168.9.41:9000
HTTPPool.PickPeer peers:[http://192.168.9.41:9000] begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
Map Add keys:[http://192.168.9.41:9000] m.keys:[] start
Map Add m.keys:[3262421 903639430 2780452827] end
HTTPPool.PickPeer p.httpGetters:map[http://192.168.9.41:9000:0xc42020e060] end
2017/04/20 19:20:07 [D] [cache.go:128] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc42011dd10 map[http://192.168.9.41:9000:0xc42020e060]} end
2017/04/20 19:20:07 [D] [root.go:64] cacheManager new ok: &{0xc4201c2000 0xc4201721e0 http://192.168.9.41:9000 0xc4201a0b10}
2017/04/20 19:20:07 [I] [cache.go:56] Watch nodes:[{http:__192.168.9.41:9000 http://192.168.9.41:9000}]
2017/04/20 19:20:07 [I] [discovery.go:176] Watch start...:/imgcache2/nodes
2017/04/20 19:20:07 [I] [router.go:24] EnableMyCacheSer ok
2017/04/20 19:20:43 [D] [discovery.go:183] Watch next...:<nil>
2017/04/20 19:20:43 [D] [cache.go:137] add :http://192.168.9.41:9000
2017/04/20 19:20:43 [D] [cache.go:137] add :http://192.168.9.37:9000
HTTPPool.PickPeer peers:[http://192.168.9.41:9000 http://192.168.9.37:9000] begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
Map Add keys:[http://192.168.9.41:9000 http://192.168.9.37:9000] m.keys:[] start
Map Add m.keys:[3262421 332339782 639806485 903639430 2780452827 3057945160] end
-----
-----
-----
2017/04/20 19:23:07 [D] [discovery.go:69] Health checkHealthCntMap:map[http://192.168.9.37:9000:0 http://192.168.9.99:9000:0 http://192.168.9.41:9000:0]
2017/04/20 19:24:07 [D] [discovery.go:69] Health checkHealthCntMap:map[http://192.168.9.37:9000:0 http://192.168.9.41:9000:0]
----------------------------41 这台机器，等待发现节点的其他机器注册


----------------------------41 这台机器，发现37/99节点的机器注册(192.168.9.37/99)
017/04/20 19:20:47 [D] [discovery.go:183] Watch next...:<nil>
2017/04/20 19:20:47 [D] [cache.go:137] add :http://192.168.9.41:9000
2017/04/20 19:20:47 [D] [cache.go:137] add :http://192.168.9.37:9000
2017/04/20 19:20:47 [D] [cache.go:137] add :http://192.168.9.99:9000
HTTPPool.PickPeer peers:[http://192.168.9.41:9000 http://192.168.9.37:9000 http://192.168.9.99:9000] begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
Map Add keys:[http://192.168.9.41:9000 http://192.168.9.37:9000 http://192.168.9.99:9000] m.keys:[] start
Map Add m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] end
HTTPPool.PickPeer p.httpGetters:map[http://192.168.9.99:9000:0xc42025a6a0 http://192.168.9.41:9000:0xc42025a660 http://192.168.9.37:9000:0xc42025a680] end
2017/04/20 19:20:47 [D] [cache.go:128] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc420256390 
map[
    http://192.168.9.41:9000:0xc42025a660 
    http://192.168.9.37:9000:0xc42025a680 
    http://192.168.9.99:9000:0xc42025a6a0
]} end
```
###### 3.5 301错误分析： 
```concept
    301 (https://github.com/golang/groupcache/issues/18)
    Group.getFromPeer peer.Get start res: req:group:"imgcache2" key:"/v1/image/gif/001/icon=100x100"  peer:&{<nil> http://192.168.9.41:9000/_groupcache/}
    Group.getFromPeer peer.Get end err:server returned: 301 Moved Permanently   res:
    Group.getFromPeer  key:/v1/image/gif/001/icon=100x100..peer:&{<nil> http://192.168.9.41:9000/_groupcache/} End
    REAL WORK2 peer:&{<nil> http://192.168.9.41:9000/_groupcache/} err:server returned: 301 Moved Permanently key:/v1/image/gif/001/icon=100x100
    REAL WORK3. peer get key fail
    
  处理方法: 
      key:/v1/image/gif/001/icon=100x100  --> hashkey: 3262421 ---> http://192.168.9.41:9000
      key:_v1/image/gif/001/icon=100x100  --> hashkey: 3262421 ---> http://192.168.9.41:9000
```

###### 4. LRU 真正缓存数据的地方
```concept
41:
LRU c.cache: map[
  _v2/image/png/001?w=850&type=.jpg:0xc420103f50 
  _v2/image/png/003?w=850&h=200&type=.webp:0xc4201020f0 
  _v2/image/png/004?w=850&type=.png:0xc42021c180 
  <!-- _v2/image/png/002?w=850:0xc420019d70 -->
  ]
99:
LRU c.cache: map[_v2/image/png/002?w=850:0xc420131f20]
99:断开后 002-->41节点的LRU。（由于H(002)->99, 从99节点获取002失败，所以从41访问8000/002）
LRU c.cache: map[
  _v2/image/png/001?w=850&type=.jpg:0xc420103f50 
  _v2/image/png/003?w=850&h=200&type=.webp:0xc4201020f0 
  _v2/image/png/004?w=850&type=.png:0xc42021c180 
  _v2/image/png/002?w=850:0xc420019d70
  ]
99:重启后.
从任务一节点访问002: H(002)->99, 99节点LRU存储002
```

###### 5.总结
```concept
               P1() ---> LRU(kp11, kp12, kp13...)
    H(k)  ---> P2() ---> LRU(kp21, kp22, kp23...)
               P3() ---> LRU(kp31, kp32, kp33...)
  一致性hash: 解决了key-->P的问题
  cache: 数据缓存在LRU中, 使用map使缓存数据在o(1)时间复杂度内获取.

ipn:节点ip
1.请求key时，如ipn:key 
2.ipn节点在本地的cache中查看是否已经缓存了key.
      hit: 直接返回
      unhit:执行地三步
3.H(key). 通过一致性hash, 计算出key-->peek, 如计算后得到p2节点
    3.1 p2节点在本节点 cache中查看.
        hit: 返回
        uhit: 执行getter回调， 执行用户注册groupcache时的回调函数，获取到数据
              getter: 获取数据失败，返回err

    3.2 p2节点返回数据。

4.p2正常返回数据。-->ipn节点拿到数据返回给cli
  p2返回错误(超时错误, p2挂掉了)。 -->ipn自己请求数据，并把数据缓存在本节点.
```
### bug
```concept

  1.ip3如果访问异常, 不跟新peek, 会导致P3->LRU3中的数据，会缓存到LRU1/2, 导致数据副本增多
    例如:
    ip1:kp31 --->LRU3(kp31)访问超时 ---> LRU1(kp31)
    ip2:kp31 --->LRU3(kp31)访问超时 ---> LRU2(kp31)

    peek3:长时间不可访问，由于peek没有跟新，H()的值域无法跟新，kp3x这些属于LRU3的key，都将被多次缓存


  2.超过deadtime, 就需要跟新peek, 缩小H()的值域(HP1, HP2)
    go func(){
            select {
                  1.监控health.
                  2.超时，跟新peek, 移除自己在etcd 注册的key
            }
    }()

  3.处理url拼接问题.
```

###### 部分运行时log
```concept

(41 非本节点访问, unhit)H(k)-->41
HTTPPool.ServeHTTP start
HTTPPool.ServeHTTP group:&{imgcache2 0x4635260 {{0 0} 1} 0xc4201721e0 67108864 {{{0 0} 0 0 0 0} 106224 0xc420436740 8 12 0} {{{0 0} 0 0 0 0} 0 <nil> 0 4 0} 0xc4201a25a0 {10 8 0 0 2 2 2 0 5}} key:_v2/image/png/004?w=850&type=.png
Group.Get key:_v2/image/png/004?w=850&type=.png..Begin
Group.lookupCache  key:_v2/image/png/004?w=850&type=.png Begin
Group.lookupCache  g.mainCache.get ok:false
Group.lookupCache  g.hotCache.get ok:false
Group.lookupCache  key:_v2/image/png/004?w=850&type=.png End
Group.Get g.lookupCache cacheHit:false
Group load key:_v2/image/png/004?w=850&type=.png..Begin
Group.lookupCache  key:_v2/image/png/004?w=850&type=.png Begin
Group.lookupCache  g.mainCache.get ok:false
Group.lookupCache  g.hotCache.get ok:false
Group.lookupCache  key:_v2/image/png/004?w=850&type=.png End
g.loadGroup.Do  key:_v2/image/png/004?w=850&type=.png..Begin
REAL WORK traverse pickPeer
HTTPPool.PickPeer key:_v2/image/png/004?w=850&type=.png begin
Map Get key:_v2/image/png/004?w=850&type=.png m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] start
idx:0...hash:4015934057
....v:3262421.......vv:http://192.168.9.41:9000
Map Get m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] end
HTTPPool.PickPeer key:_v2/image/png/004?w=850&type=.png peer == p.self, p.self:http://192.168.9.41:9000
HTTPPool.PickPeer key:_v2/image/png/004?w=850&type=.png end
REAL WORK3. peer get key fail
Group.getLocally  key:_v2/image/png/004?w=850&type=.png..g:&{imgcache2 0x4635260 {{0 0} 1} 0xc4201721e0 67108864 {{{0 0} 0 0 0 0} 106224 0xc420436740 8 14 0} {{{0 0} 0 0 0 0} 0 <nil> 0 6 0} 0xc4201a25a0 {11 8 0 0 3 3 2 0 6}} ctx:<nil> dst:&{0xc42000c980 {[] }}Begin
2017/04/20 19:44:25 [D] [cache.go:86] getter , key:_v2/image/png/004?w=850&type=.png
2017/04/20 19:44:25 [D] [cache.go:98] key:_v2/image/png/004?w=850&type=.png begin
2017/04/20 19:44:26 [D] [cache.go:115] key:/v2/image/png/004?w=850&type=.png http.get end...StatusCode:200 err:<nil>
Group.getLocally  key:_v2/image/png/004?w=850&type=.png. End
REAL WORK4. g.getLocally err:<nil>
Group.populateCache  key:_v2/image/png/004?w=850&type=.png..Begin
LRU c.cache:   从这里看到， 41节点缓存了 001/003/004
    map[
    _v2/image/png/001?w=850&type=.jpg:0xc420409020 
    _v2/image/png/003?w=850&h=200&type=.webp:0xc420018450 
    _v2/image/png/004?w=850&type=.png:0xc4201a1710]
Group.populateCache  key:_v2/image/png/004?w=850&type=.png..End
g.loadGroup.Do key:_v2/image/png/004?w=850&type=.png..End
Group load key:_v2/image/png/004?w=850&type=.png..End
Group Get g.load destPopulated:true
Group.Get key:_v2/image/png/004?w=850&type=.png..End
HTTPPool.ServeHTTP group.Get key end err:<nil>
HTTPPool.ServeHTTP end
---
---
---
(41 来非自本节点, hint)
HTTPPool.ServeHTTP start
HTTPPool.ServeHTTP group:&{imgcache2 0x4635260 {{0 0} 1} 0xc4201721e0 67108864 {{{0 0} 0 0 0 0} 106224 0xc420436740 4 8 0} {{{0 0} 0 0 0 0} 0 <nil> 0 4 0} 0xc4201a25a0 {6 4 0 0 2 2 2 0 3}} key:_v2/image/png/001?w=850&type=.jpg
Group.Get key:_v2/image/png/001?w=850&type=.jpg..Begin
Group.lookupCache  key:_v2/image/png/001?w=850&type=.jpg Begin
Group.lookupCache  g.mainCache.get ok:true
Group.lookupCache  key:_v2/image/png/001?w=850&type=.jpg End
Group.Get g.lookupCache cacheHit:true
Group.Get key:_v2/image/png/001?w=850&type=.jpg..End
HTTPPool.ServeHTTP group.Get key end err:<nil>
HTTPPool.ServeHTTP end
---
---
---
(41 来自本节点)
2017/04/20 19:44:05 [D] [root.go:69] URI:/v2/image/png/003?w=850&h=200&type=.webp
2017/04/20 19:44:05 [D] [root.go:71] key:/v2/image/png/003?w=850&h=200&type=.webp cm:&{0xc4201c2000 0xc4201721e0 http://192.168.9.41:9000 0xc4201a0b10}
Group.Get key:_v2/image/png/003?w=850&h=200&type=.webp..Begin
Group.lookupCache  key:_v2/image/png/003?w=850&h=200&type=.webp Begin
Group.lookupCache  g.mainCache.get ok:true
Group.lookupCache  key:_v2/image/png/003?w=850&h=200&type=.webp End
Group.Get g.lookupCache cacheHit:true
Group.Get key:_v2/image/png/003?w=850&h=200&type=.webp..End
2017/04/20 19:44:05 [D] [root.go:73] err:<nil>
2017/04/20 19:44:05 [D] [root.go:85] Get no err
```













