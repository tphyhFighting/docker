####etcdctl v3


export ETCDCTL_API=3
get
```bash
/ # etcdctl  get --prefix /imgcache/nodes
/imgcache/nodes/ele-leader/694d5beb4bdefe07
192.168.6.1
/imgcache/nodes/http:__192.168.0.41:9000
http://192.168.0.41:9000
/imgcache/nodes/test
192.168.8.2-ttl30
/ #
```

watch
```bash
/ # etcdctl watch --prefix /imgcache/nodes/
PUT
/imgcache/nodes/http:__192.168.0.41:9000
http://192.168.0.41:9000
```

docker run -d --restart always --name imgfit-cache -p 9000:9000   -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache


docker run -d --restart always --name imgfit-cache --network=host   -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache


etcdctl get --prefix=true imgcahe
