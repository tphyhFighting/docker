#### docker register 
```bash
文档:
https://docs.docker.com/registry/deploying/#restricting-access
```

#### 1.获取register 镜像
```bash
docker run -d -p 5000:5000 --restart=always --name registry \
  -v `pwd`/data:/var/lib/registry \
  registry:2
```

#### 2.建立certs/ auth/配置目录
```bash
mkdir -p certs
certs/domain.crt
certs/domain.key

mkdir auth
```

#### 3.创建密码
```bash
docker run --entrypoint htpasswd registry:2 -Bbn testuser testpassword >> auth/htpasswd
docker run --entrypoint htpasswd registry:2 -Bbn user1 user1pass1 >> auth/htpasswd
docker run --entrypoint htpasswd registry:2 -Bbn user2 user1pass2 >> auth/htpasswd
```

#### 4.重启register
```bash
docker run -d -p 5000:5000 --restart=always --name registry \
  -v `pwd`/auth:/auth \
  -e "REGISTRY_AUTH=htpasswd" \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd \
  -v `pwd`/certs:/certs \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  registry:2
```

#### 5.登陆/上传镜像
```bash
➜  build git:(imgfit-cache-debug) ✗ docker login tplinux.cn:5000
Username (testuser): huoyinghui
Password:
Login Succeeded
➜  build git:(imgfit-cache-debug) ✗ docker tag e4b5e1f74b7b tplinux.cn:5000/convert:v6.9.6-8_2016-12-26
➜  build git:(imgfit-cache-debug) ✗ docker push tplinux.cn:5000/convert:v6.9.6-8_2016-12-26
The push refers to a repository [tplinux.cn:5000/convert]
58456c5e697d: Pushed
fcad8ad5a40f: Pushed
v6.9.6-8_2016-12-26: digest: sha256:5b84554eba452c660118ea6589fd4f9fccb003c6c52ad13f67e00d29617b6926 size: 2806
➜  build git:(imgfit-cache-debug) ✗
```

#### 6.registry ui
```bash
docker run -it -p 8080:8080 --name registry-web --link registry \
           -e REGISTRY_URL=https://tplinux.cn:5000/v2 \
           -e REGISTRY_TRUST_ANY_SSL=true \
           -e REGISTRY_BASIC_AUTH="YWRtaW46Y2hhbmdlbWU=" \
           -e REGISTRY_NAME=localhost:5000 hyper/docker-registry-web
```
