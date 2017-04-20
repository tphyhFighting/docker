##imgfit
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -it -p 8000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/build/conf:/app/conf  imgfit bash
<!-- etcd -name etcd1 -initial-advertise-peer-urls http://10.0.1.11:2380 \
    -listen-peer-urls http://10.0.1.11:2380 \
    -listen-client-urls http://10.0.1.11:2379,http://127.0.0.1:2379 \
    -advertise-client-urls http://10.0.1.11:2379 \
    -initial-cluster-token my-etcd-cluster \
    -initial-cluster etcd0=http://10.0.1.10:2380,etcd1=http://10.0.1.11:2380,etcd2=http://10.0.1.12:2380 \
    -initial-cluster-state new
 -->
firewall-cmd --zone=public --add-port=2379/tcp --permanent
firewall-cmd --zone=public --add-port=2380/tcp --permanent
firewall-cmd --zone=public --add-port=9000/tcp --permanent
firewall-cmd --zone=public --add-port=7000/tcp --permanent
firewall-cmd --reload

## etcd
##### 1.启动三台节点
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

##### 2.查看节点注册
➜  ~ etcdctl member list
4af0a3b2552ca31: name=etcd2 peerURLs=http://192.168.9.41:2380 clientURLs=http://192.168.9.41:2379 isLeader=true
5265a651acb4a72e: name=etcd0 peerURLs=http://192.168.9.37:2380 clientURLs=http://192.168.9.37:2379 isLeader=false
df1c14c0132a3287: name=etcd1 peerURLs=http://192.168.9.99:2380 clientURLs=http://192.168.9.99:2379 isLeader=false
➜  ~


##### 3.启动程序imgfit. 注册k-v
➜  ~ etcdctl ls /imgcache2/nodes
/imgcache2/nodes/4ac2c5092b744b39d26c5050f03329f51734c273
/imgcache2/nodes/75f75e9e5b3691bd3682da2a3b583c36a46c8e4c
/imgcache2/nodes/d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9
➜  ~

####### a.imgfit: watch 监测节点变化, 发现新的节点就会完成peek 注册
```bash
2017/04/19 10:25:58 SUCCESS  ▶ 0017 './imgfit' is running...
logmod:7
2017/04/19 10:25:58 [I] [config.go:75] config-v:{/tmp/imgfit YHGIZY2NY26FAE3DXOM8 FPVPcBLQXRFGB4hfQaNFiZaV2AYSSlUdxJLRKSrU OVH-BHS http://192.168.0.18:7380 0.0.0.0:8000  [image upload] map[image:1 upload:1]}
2017/04/19 10:25:58 [I] [root.go:37] Cache name :   imgcache2
2017/04/19 10:25:58 [I] [root.go:38] Cache size :   67108864
HTTPPool.PickPeer self:http://192.168.9.41:9000 begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
RegisterPeerPicker: start
RegisterPeerPicker: end fn:0x44a7030
HTTPPool.PickPeer self:http://192.168.9.41:9000 end
2017/04/19 10:25:58 [D] [discovery.go:32] NewServiceRegistry cfg:{[http://192.168.9.41:2379] 0x4bb81c0 <nil>   1s 0} start
2017/04/19 10:25:58 [D] [discovery.go:41] NewServiceRegistry sr:{0xc420154820 imgcache2 0xc420010310} end
2017/04/19 10:25:58 [D] [cache.go:37] CacheManager Join enter
2017/04/19 10:25:58 [D] [discovery.go:47] ServiceRegistry Register name:d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 _url:http://192.168.9.41:9000 start
2017/04/19 10:25:58 [D] [discovery.go:49] ServiceRegistry Register name:d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 _url:http://192.168.9.41:9000 end
2017/04/19 10:25:58 [D] [discovery.go:69] GetNodes start: key:/imgcache2/nodes  getResp:&{get {Key: /imgcache2/nodes, CreatedIndex: 9, ModifiedIndex: 9, TTL: 0} <nil> 9 6e3e33f4594fa89a} err:<nil>
2017/04/19 10:25:58 [D] [discovery.go:77] GetNodes end: list:[{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000}]
2017/04/19 10:25:58 [D] [cache.go:103] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc420186a20 map[]} nodes:[{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000}] start
2017/04/19 10:25:58 [D] [cache.go:114] add :http://192.168.9.41:9000
HTTPPool.PickPeer peers:[http://192.168.9.41:9000] begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
Map Add keys:[http://192.168.9.41:9000] m.keys:[] start
Map Add m.keys:[3262421 903639430 2780452827] end
HTTPPool.PickPeer p.httpGetters:map[http://192.168.9.41:9000:0xc4201d05e0] end
2017/04/19 10:25:58 [D] [cache.go:105] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc420103e90 map[http://192.168.9.41:9000:0xc4201d05e0]} end
2017/04/19 10:25:58 [D] [cache.go:39] CacheManager Join end
2017/04/19 10:25:58 [D] [root.go:62] cacheManager new ok: &{0xc4201aa000 0xc4201521e0 http://192.168.9.41:9000 0xc420186b10}
2017/04/19 10:25:58 [I] [router.go:24] EnableMyCacheSer ok
2017/04/19 10:25:58 [D] [cache.go:54] watch: [{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000}]
2017/04/19 10:25:58 [D] [discovery.go:117] Watch start...:/imgcache2/nodes
----------------------------41 这台机器，等待发现节点的其他机器注册


----------------------------41 这台机器，发现37节点的机器注册(192.168.9.37)
2017/04/19 10:29:23 [D] [discovery.go:124] Watch next...:<nil>
2017/04/19 10:29:23 [D] [discovery.go:69] GetNodes start: key:/imgcache2/nodes  getResp:&{get {Key: /imgcache2/nodes, CreatedIndex: 9, ModifiedIndex: 9, TTL: 0} <nil> 10 6e3e33f4594fa89a} err:<nil>
2017/04/19 10:29:23 [D] [discovery.go:77] GetNodes end: list:[{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000} {4ac2c5092b744b39d26c5050f03329f51734c273 http://192.168.9.37:9000}]
2017/04/19 10:29:23 [D] [cache.go:103] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc420103e90 map[http://192.168.9.41:9000:0xc4201d05e0]} nodes:[{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000} {4ac2c5092b744b39d26c5050f03329f51734c273 http://192.168.9.37:9000}] start
2017/04/19 10:29:23 [D] [cache.go:114] add :http://192.168.9.41:9000
2017/04/19 10:29:23 [D] [cache.go:114] add :http://192.168.9.37:9000
HTTPPool.PickPeer peers:[http://192.168.9.41:9000 http://192.168.9.37:9000] begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
Map Add keys:[http://192.168.9.41:9000 http://192.168.9.37:9000] m.keys:[] start
Map Add m.keys:[3262421 332339782 639806485 903639430 2780452827 3057945160] end
HTTPPool.PickPeer p.httpGetters:map[http://192.168.9.41:9000:0xc4201828e0 http://192.168.9.37:9000:0xc420182900] end
2017/04/19 10:29:23 [D] [cache.go:105] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc42017c5d0 map[http://192.168.9.41:9000:0xc4201828e0 http://192.168.9.37:9000:0xc420182900]} end
----------------------------41 peek 添加完成


----------------------------41 这台机器，发现99节点的机器注册(http://192.168.9.99:9000)
2017/04/19 10:32:48 [D] [discovery.go:124] Watch next...:<nil>
2017/04/19 10:32:48 [D] [discovery.go:69] GetNodes start: key:/imgcache2/nodes  getResp:&{get {Key: /imgcache2/nodes, CreatedIndex: 9, ModifiedIndex: 9, TTL: 0} <nil> 11 6e3e33f4594fa89a} err:<nil>
2017/04/19 10:32:48 [D] [discovery.go:77] GetNodes end: list:[{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000} {4ac2c5092b744b39d26c5050f03329f51734c273 http://192.168.9.37:9000} {75f75e9e5b3691bd3682da2a3b583c36a46c8e4c http://192.168.9.99:9000}]
2017/04/19 10:32:48 [D] [cache.go:103] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc42017c5d0 map[http://192.168.9.41:9000:0xc4201828e0 http://192.168.9.37:9000:0xc420182900]} nodes:[{d2f0216c0543adf1ff237e3e6b584b1c61b6c1a9 http://192.168.9.41:9000} {4ac2c5092b744b39d26c5050f03329f51734c273 http://192.168.9.37:9000} {75f75e9e5b3691bd3682da2a3b583c36a46c8e4c http://192.168.9.99:9000}] start
2017/04/19 10:32:48 [D] [cache.go:114] add :http://192.168.9.41:9000
2017/04/19 10:32:48 [D] [cache.go:114] add :http://192.168.9.37:9000
2017/04/19 10:32:48 [D] [cache.go:114] add :http://192.168.9.99:9000
HTTPPool.PickPeer peers:[http://192.168.9.41:9000 http://192.168.9.37:9000 http://192.168.9.99:9000] begin
New replicas:3 fh:<nil> start
New replicas:3 fh:<nil> end
Map Add keys:[http://192.168.9.41:9000 http://192.168.9.37:9000 http://192.168.9.99:9000] m.keys:[] start
Map Add m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] end
HTTPPool.PickPeer p.httpGetters:map[http://192.168.9.41:9000:0xc420183440 http://192.168.9.37:9000:0xc420183460 http://192.168.9.99:9000:0xc420183480] end
2017/04/19 10:32:48 [D] [cache.go:105] addPeers: &{<nil> <nil> http://192.168.9.41:9000 {/_groupcache/ 3 <nil>} {0 0} 0xc42017cb40 map[http://192.168.9.41:9000:0xc420183440 http://192.168.9.37:9000:0xc420183460 http://192.168.9.99:9000:0xc420183480]} end

当前peek(41, 37, 99)
```
###### 4.imgfit 8000 服务器(启动8000端口的图片服务器)
```bash
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -it -p 8000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/build/conf:/app/conf  imgfit bash
```
###### 5.开始测试groupcache, 通信(ok)
```bash
key:/v1/image/gif/001/icon=100x100  --> hashkey: 3262421 ---> http://192.168.9.41:9000

2017/04/19 11:01:53 [D] [root.go:67] URI:/v1/image/gif/001/icon=100x100
2017/04/19 11:01:53 [D] [root.go:69] key:/v1/image/gif/001/icon=100x100 cm:&{0xc4201aa000 0xc4201521e0 http://192.168.9.41:9000 0xc420186b10}
2017/04/19 11:01:53 [I] [cache.go:65] cache get..start, key:/v1/image/gif/001/icon=100x100 ctx:<nil>
Group.Get key:/v1/image/gif/001/icon=100x100..Begin
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 Begin
Group.lookupCache  g.mainCache.get ok:false
Group.lookupCache  g.hotCache.get ok:false
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 End
Group.Get g.lookupCache cacheHit:false
Group load key:/v1/image/gif/001/icon=100x100..Begin
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 Begin
Group.lookupCache  g.mainCache.get ok:false
Group.lookupCache  g.hotCache.get ok:false
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 End
g.loadGroup.Do  key:/v1/image/gif/001/icon=100x100..Begin
REAL WORK traverse pickPeer
HTTPPool.PickPeer key:/v1/image/gif/001/icon=100x100 begin
Map Get key:/v1/image/gif/001/icon=100x100 m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] start
idx:0...hash:3412658533
....v:3262421.......vv:http://192.168.9.41:9000
Map Get m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] end
HTTPPool.PickPeer key:/v1/image/gif/001/icon=100x100 peer == p.self, p.self:http://192.168.9.41:9000
HTTPPool.PickPeer key:/v1/image/gif/001/icon=100x100 end
REAL WORK3. peer get key fail
2017/04/19 11:01:53 [D] [cache.go:72] thumbnail , key:/v1/image/gif/001/icon=100x100
2017/04/19 11:01:53 [D] [cache.go:84] key:/v1/image/gif/001/icon=100x100 begin
2017/04/19 11:01:53 [D] [cache.go:89] url-key:http://192.168.9.41:8000/v1/image/gif/001/icon=100x100 .... u:http://192.168.9.41:8000/v1/image/gif/001/icon=100x100
2017/04/19 11:01:53 [D] [cache.go:92] key:/v1/image/gif/001/icon=100x100 http.get end...StatusCode:200 err:<nil>
REAL WORK4. g.getLocally err:<nil>
Group.populateCache  key:/v1/image/gif/001/icon=100x100..Begin
Group.populateCache  key:/v1/image/gif/001/icon=100x100..End
g.loadGroup.Do key:/v1/image/gif/001/icon=100x100..End
Group load key:/v1/image/gif/001/icon=100x100..End
Group Get g.load destPopulated:true
Group.Get key:/v1/image/gif/001/icon=100x100..End
2017/04/19 11:01:53 [I] [cache.go:67] cache get..end, err:<nil>
2017/04/19 11:01:53 [D] [root.go:71] err:<nil>
2017/04/19 11:01:53 [D] [root.go:83] Get no err
```

key2=key1 , 访问在99节点
```bash
2017/03/29 09:46:39 [D] [root.go:67] URI:/v1/image/gif/001/icon=100x100
2017/03/29 09:46:39 [D] [root.go:69] key:/v1/image/gif/001/icon=100x100 cm:&{0xc4201a4000 0xc420168180 http://192.168.9.99:9000 0xc420014750}
2017/03/29 09:46:39 [I] [cache.go:65] cache get..start, key:/v1/image/gif/001/icon=100x100 ctx:<nil>
Group.Get key:/v1/image/gif/001/icon=100x100..Begin
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 Begin
Group.lookupCache  g.mainCache.get ok:false
Group.lookupCache  g.hotCache.get ok:false
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 End
Group.Get g.lookupCache cacheHit:false
Group load key:/v1/image/gif/001/icon=100x100..Begin
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 Begin
Group.lookupCache  g.mainCache.get ok:false
Group.lookupCache  g.hotCache.get ok:false
Group.lookupCache  key:/v1/image/gif/001/icon=100x100 End
g.loadGroup.Do  key:/v1/image/gif/001/icon=100x100..Begin
REAL WORK traverse pickPeer
HTTPPool.PickPeer key:/v1/image/gif/001/icon=100x100 begin
Map Get key:/v1/image/gif/001/icon=100x100 m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] start
idx:0...hash:3412658533
....v:3262421.......vv:http://192.168.9.41:9000
Map Get m.keys:[3262421 332339782 639806485 675198070 903639430 2377458808 2780452827 3057945160 3092812331] end
HTTPPool.PickPeer key:/v1/image/gif/001/icon=100x100 peer != p.self, peer:http://192.168.9.41:9000 != p.self:http://192.168.9.99:9000
HTTPPool.PickPeer key:/v1/image/gif/001/icon=100x100 end
Group.getFromPeer  key:/v1/image/gif/001/icon=100x100..peer:&{<nil> http://192.168.9.41:9000/_groupcache/} Group:&{imgcache2 0x529460 {{0 0} 1} 0xc420168180 67108864 {{{0 0} 0 0 0 0} 0 <nil> 0 4 0} {{{0 0} 0 0 0 0} 0 <nil> 0 4 0} 0xc42000c560 {2 0 0 0 2 2 0 1 0}} Begin
Group.getFromPeer peer.Get start res: req:group:"imgcache2" key:"/v1/image/gif/001/icon=100x100"  peer:&{<nil> http://192.168.9.41:9000/_groupcache/}
Group.getFromPeer peer.Get end err:server returned: 301 Moved Permanently   res:
Group.getFromPeer  key:/v1/image/gif/001/icon=100x100..peer:&{<nil> http://192.168.9.41:9000/_groupcache/} End
REAL WORK2 peer:&{<nil> http://192.168.9.41:9000/_groupcache/} err:server returned: 301 Moved Permanently key:/v1/image/gif/001/icon=100x100
REAL WORK3. peer get key fail
2017/03/29 09:46:39 [D] [cache.go:72] thumbnail , key:/v1/image/gif/001/icon=100x100
2017/03/29 09:46:39 [D] [cache.go:84] key:/v1/image/gif/001/icon=100x100 begin
2017/03/29 09:46:39 [D] [cache.go:89] url-key:http://192.168.9.41:8000/v1/image/gif/001/icon=100x100 .... u:http://192.168.9.41:8000/v1/image/gif/001/icon=100x100
2017/03/29 09:46:39 [D] [cache.go:92] key:/v1/image/gif/001/icon=100x100 http.get end...StatusCode:200 err:<nil>
REAL WORK4. g.getLocally err:<nil>
Group.populateCache  key:/v1/image/gif/001/icon=100x100..Begin
Group.populateCache  key:/v1/image/gif/001/icon=100x100..End
g.loadGroup.Do key:/v1/image/gif/001/icon=100x100..End
Group load key:/v1/image/gif/001/icon=100x100..End
Group Get g.load destPopulated:true
Group.Get key:/v1/image/gif/001/icon=100x100..End
2017/03/29 09:46:39 [I] [cache.go:67] cache get..end, err:<nil>
2017/03/29 09:46:39 [D] [root.go:71] err:<nil>
2017/03/29 09:46:39 [D] [root.go:83] Get no err
```
    出错分析： 301 (https://github.com/golang/groupcache/issues/18)
    Group.getFromPeer peer.Get start res: req:group:"imgcache2" key:"/v1/image/gif/001/icon=100x100"  peer:&{<nil> http://192.168.9.41:9000/_groupcache/}
    Group.getFromPeer peer.Get end err:server returned: 301 Moved Permanently   res:
    Group.getFromPeer  key:/v1/image/gif/001/icon=100x100..peer:&{<nil> http://192.168.9.41:9000/_groupcache/} End
    REAL WORK2 peer:&{<nil> http://192.168.9.41:9000/_groupcache/} err:server returned: 301 Moved Permanently key:/v1/image/gif/001/icon=100x100
    REAL WORK3. peer get key fail

    

  处理方法: 
      key:/v1/image/gif/001/icon=100x100  --> hashkey: 3262421 ---> http://192.168.9.41:9000
      key:_v1/image/gif/001/icon=100x100  --> hashkey: 3262421 ---> http://192.168.9.41:9000
    
###### 6.finish
