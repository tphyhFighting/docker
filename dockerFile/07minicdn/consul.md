##consul

## ser
1.centos
consul agent -server -bootstrap-expect 2 -data-dir /tmp/consul -node=ns1 -bind=192.168.9.3 -dc=dc1 -config-dir=~/consul/consul_config
<!-- consul agent -server -bootstrap-expect 2 -data-dir /tmp/consul -node=n2 -bind=192.168.9.99 -dc=dc1 -->

2.mac
consul agent -server -bootstrap-expect 2 -data-dir /tmp/consul -node=ns2 -bind=192.168.9.41 -dc=dc1 -ui-dir=/Users/apple/go-dev/bin/consul_0.7.5_web_ui

3.
## cli
启动n3上的client mode agent：
consul agent  -data-dir /tmp/consul -node=nc4 -bind=192.168.9.99  -dc=dc1 -config-dir=~/consul/consul_config -join 192.168.9.41

consul agent -data-dir /tmp/consul -node=service1 -config-dir /etc/consul.d -bind 192.168.9.99 -join 192.168.9.41


## 开启访问端口
```
[root@centos-linux ~]# firewall-cmd --zone=public --add-port=8301/tcp --permanent
success
[root@centos-linux ~]# firewall-cmd --zone=public --add-port=8300/tcp --permanent
success
[root@centos-linux ~]# firewall-cmd --reload
success
[root@centos-linux ~]#
```
