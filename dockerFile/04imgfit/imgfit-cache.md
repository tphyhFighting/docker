#### imgfit-cache 网络问题

云主机上的网络:
```bash
[root@fs12t01 ~]# docker run --rm  -it --network=host centos bash
[root@fs12t01 /]# yum install -y iproute   #保证我们imgfit-cache镜像中，程序可以获取ip
[root@fs12t01 /]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: bond0: <BROADCAST,MULTICAST,MASTER> mtu 1500 qdisc noop state DOWN qlen 1000
    link/ether 26:15:ac:4c:0d:5b brd ff:ff:ff:ff:ff:ff
3: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN qlen 1000
    link/ether da:be:a3:c3:b6:67 brd ff:ff:ff:ff:ff:ff
4: ifb0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN qlen 32
    link/ether 6a:44:86:9b:89:47 brd ff:ff:ff:ff:ff:ff
5: ifb1: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN qlen 32
    link/ether 3a:60:18:b4:f1:f1 brd ff:ff:ff:ff:ff:ff
6: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 0c:c4:7a:69:ca:b4 brd ff:ff:ff:ff:ff:ff
    inet 167.114.175.4/24 brd 167.114.175.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 2607:5300:60:7604::/64 scope global
       valid_lft forever preferred_lft forever
    inet6 fe80::ec4:7aff:fe69:cab4/64 scope link
       valid_lft forever preferred_lft forever
7: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 0c:c4:7a:69:ca:b5 brd ff:ff:ff:ff:ff:ff
    inet 172.16.2.1/12 brd 172.31.255.255 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::ec4:7aff:fe69:cab5/64 scope link
       valid_lft forever preferred_lft forever
8: eth2: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN qlen 1000
    link/ether 0c:c4:7a:69:ca:b6 brd ff:ff:ff:ff:ff:ff
9: eth3: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN qlen 1000
    link/ether 0c:c4:7a:69:ca:b7 brd ff:ff:ff:ff:ff:ff
10: teql0: <NOARP> mtu 1500 qdisc noop state DOWN qlen 100
    link/void
11: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN qlen 1
    link/ipip 0.0.0.0 brd 0.0.0.0
12: gre0@NONE: <NOARP> mtu 1476 qdisc noop state DOWN qlen 1
    link/gre 0.0.0.0 brd 0.0.0.0
13: gretap0@NONE: <BROADCAST,MULTICAST> mtu 1462 qdisc noop state DOWN qlen 1000
    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff
14: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN qlen 1
    link/sit 0.0.0.0 brd 0.0.0.0
15: ip6tnl0@NONE: <NOARP> mtu 1452 qdisc noop state DOWN qlen 1
    link/tunnel6 :: brd ::
16: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 02:42:9f:c8:c4:05 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.1/20 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:9fff:fec8:c405/64 scope link
       valid_lft forever preferred_lft forever
82: veth282bf32@if81: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP
    link/ether ba:36:f2:98:1f:bf brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::b836:f2ff:fe98:1fbf/64 scope link
       valid_lft forever preferred_lft forever
[root@fs12t01 /]# Connection to 167.114.175.4 closed by remote host.
Connection to 167.114.175.4 closed.
```

内网ip:
172.16.2.1

```bash
[root@VM_103_136_centos /]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 52:54:00:af:1a:8f brd ff:ff:ff:ff:ff:ff
    inet 10.141.103.136/18 brd 10.141.127.255 scope global eth0
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN
    link/ether 76:4d:ea:4b:95:ba brd ff:ff:ff:ff:ff:ff
    inet 172.17.42.1/16 scope global docker0
122: veth600e506: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 76:4d:ea:4b:95:ba brd ff:ff:ff:ff:ff:ff
125: vetha032323: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 8a:4d:87:5c:fc:9c brd ff:ff:ff:ff:ff:ff
[root@VM_103_136_centos /]#
```

docker run --rm -it --name imgfit-cache --network=host -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache  bash

docker run --rm -it --name imgfit-cache -p 9000:9000 --link imgfit:imgfi -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache  bash


docker run --rm -it --name imgfit-cache -p 10000:9000 --link imgfit:imgfit -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache  bash

6.1
docker run --name imgfit-cache  -d --restart always  --network=host   -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache


6.1:
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -d --restart always -p 7000:7000 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf   apk.302e.com:3000/apkpure/imgfit:imgfit-cache

mac:
docker run --rm -it --name imgfit-cache -p 9000:9000  --link imgfit:imgfitk -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache  bash
