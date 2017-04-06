## docker 中指定ip

## docker 启动各个容器
  0.imgfit: ip 对minicdn-s/m 均可访问
  docker run --rm -d --name imgfit --network=my-bridge-network-minicdn -p 8000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf apk.302e.com:3000/apkpure/imgfit

  1.m :ip 对minicdn-s 可访问
  docker run --rm -d --name minicdn-m --network=my-bridge-network-minicdn  -p 9000:9000  minicdn  /app/minicdn -mirror http://localhost:8000 -addr :9000
  docker run --rm -it --name minicdn-m --network=my-bridge-network-minicdn  -p 9000:9000  minicdn  bash
  docker run --rm -it --name minicdn-m  -p 9000:9000  minicdn  bash
  ./minicdn -mirror http://172.19.0.2:8000 -addr :9000
  ./minicdn -mirror http://192.168.9.41:8000 -addr :9000

  2.s   
  docker run --rm -it --name minicdn-s --network=my-bridge-network-minicdn -p 9001:9001 minicdn bash
  docker run --rm -d --name minicdn-s --network=my-bridge-network-minicdn -p 9001:9001 minicdn /app/minicdn -upstream ws://172.19.0.3:9000 -addr :9001
  ./minicdn -upstream ws://localhost:9000 -addr :9002
  需要连接minicdn-m:ip
  ./minicdn -upstream ws://172.19.0.3:9000 -addr :9002

  3.s1
  docker run --rm -d --name minicdn-s9002 --network=my-bridge-network-minicdn -p 9002:9002 minicdn /app/minicdn -upstream ws://172.19.0.3:9000 -addr :9002
  ./minicdn -upstream ws://localhost:9000 -addr :9002
  需要连接minicdn-m:ip
  ./minicdn -upstream ws://172.19.0.3:9000 -addr :9002

## docker net
```
➜  imgfit git:(panic) ✗ docker network  inspect my-bridge-network-minicdn
[
    {
        "Name": "my-bridge-network-minicdn",
        "Id": "38e3f943e2b9143e3b9a09d16076aac6c3175b7d1ef26d932a86639caae17eef",
        "Created": "2017-03-27T02:53:35.085469457Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.19.0.0/16",
                    "Gateway": "172.19.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Containers": {
            "6faebc186c6e9f0a79d965da2c426b42693d3ef538dfc9080b9e7ead0236e704": {
                "Name": "imgfit",
                "EndpointID": "b8120124236184ec89512c83022d64f223d72fe1c46920d19aef21c1e6885d0f",
                "MacAddress": "02:42:ac:13:00:02",
                "IPv4Address": "172.19.0.2/16",
                "IPv6Address": ""
            },
            "cc9a0340158cff5f7a0fb7c040b52d22cc356e3e935a915f7bec5eabe3409576": {
                "Name": "minicdn-m",
                "EndpointID": "9a8f0dfdcb4e0149aa4b0b4cb5a34838e1a08a5ca189095f4f8bd6659cce459b",
                "MacAddress": "02:42:ac:13:00:03",
                "IPv4Address": "172.19.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
➜  imgfit git:(panic) ✗
```

## net 连接测试
容器1: imgfit
➜  imgfit git:(panic) ✗ docker run --rm -it --name imgfit --network=my-bridge-network-minicdn  -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf apk.302e.com:3000/apkpure/imgfit bash
[root@9d333fa8619f app]# ping minicdn-m
PING minicdn-m (172.19.0.3) 56(84) bytes of data.
64 bytes from minicdn-m.my-bridge-network-minicdn (172.19.0.3): icmp_seq=1 ttl=64 time=0.120 ms
64 bytes from minicdn-m.my-bridge-network-minicdn (172.19.0.3): icmp_seq=2 ttl=64 time=0.070 ms
64 bytes from minicdn-m.my-bridge-network-minicdn (172.19.0.3): icmp_seq=3 ttl=64 time=0.066 ms
[root@9d333fa8619f app]#

容器2: minicdn-m
➜  minicdn git:(hyh) ✗ docker run --rm -it --name minicdn-m --network=my-bridge-network-minicdn  minicdn bash
root@cca373dad169:/app# ping imgfit
PING imgfit (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: icmp_seq=0 ttl=64 time=0.068 ms
64 bytes from 172.19.0.2: icmp_seq=1 ttl=64 time=0.079 ms
64 bytes from 172.19.0.2: icmp_seq=2 ttl=64 time=0.077 ms

容器3: minicdn-s
➜  minicdn git:(hyh) ✗ docker run --rm -it --name minicdn-s --network=my-bridge-network-minicdn  minicdn bash
root@3dfb0f2c84c4:/app# ping minicdn-m
PING minicdn-m (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: icmp_seq=0 ttl=64 time=0.071 ms
64 bytes from 172.19.0.3: icmp_seq=1 ttl=64 time=0.078 ms
root@3dfb0f2c84c4:/app# ping imgfit
PING imgfit (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: icmp_seq=0 ttl=64 time=0.087 ms
64 bytes from 172.19.0.2: icmp_seq=1 ttl=64 time=0.125 ms
root@3dfb0f2c84c4:/app#

容器3: minicdn-s1
➜  minicdn git:(hyh) ✗ docker run --rm -it --name minicdn-s1 --network=my-bridge-network-minicdn  minicdn bash
root@3dfb0f2c84c4:/app# ping minicdn-m
PING minicdn-m (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: icmp_seq=0 ttl=64 time=0.071 ms
64 bytes from 172.19.0.3: icmp_seq=1 ttl=64 time=0.078 ms
root@3dfb0f2c84c4:/app# ping imgfit
PING imgfit (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: icmp_seq=0 ttl=64 time=0.087 ms
64 bytes from 172.19.0.2: icmp_seq=1 ttl=64 time=0.125 ms
root@3dfb0f2c84c4:/app#
