http://www.lining0806.com/docker%E7%A7%81%E6%9C%89%E4%BB%93%E5%BA%93%E4%BD%BF%E7%94%A8%E5%9F%9F%E5%90%8D%E5%92%8C%E9%99%90%E5%88%B6%E7%99%BB%E5%BD%95/


docker run -d --name registry -p 5000:5000 --restart=always -v /Users/apple/opt/data/auth:/auth -e "REGISTRY_AUTH=htpasswd" -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm"  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd registry


docker run -d -p 5000:5000 -v /Users/apple/opt/registry:/var/lib/registry --restart=always --name registry-v2 registry:2.1.1

docker network create --driver bridge bnet

docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit-cache -it --network=host -p 9000:9000 -p 2379:2379 -p 2380:2380 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache bash


docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit-cache2 -it --network=host -p 9000:9000 -p 2379:2379 -p 2380:2380 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache bash


centos:
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit-cache -it --net=host -p 9000:9000 -p 2379:2379 -p 2380:2380 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  apk.302e.com:3000/apkpure/imgfit:imgfit-cache bash



docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit-cache -it --net=host -p 9000:9000 -p 2379:2379 -p 2380:2380 -v `pwd`/:/app/  apk.302e.com:3000/apkpure/imgfit:imgfit-cache bash

➜  imgfit git:(imgfit-cache-debug) docker network ls
NETWORK ID          NAME                        DRIVER              SCOPE
0b612f7b55cf        bnet                        bridge              local
4add43a8233e        bridge                      bridge              local
8dbc1434e632        gitlab-net                  bridge              local
4058bde4406c        host                        host                local
38e3f943e2b9        my-bridge-network-minicdn   bridge              local
a37b10392438        none                        null                local
➜  imgfit git:(imgfit-cache-debug)