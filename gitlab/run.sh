## gitlab

    https://hub.docker.com/r/twang2218/gitlab-ce-zh/


##
https://docs.gitlab.com/omnibus/docker/README.html

```
docker run -d --hostname gitlab.example.com \
  -p 3000:3000 \
  -p 3443:443 \
  -p 3022:22 \
  --name gitlab \
  --restart unless-stopped \
  -v /home/gitlab/config:/etc/gitlab \
  -v /home/gitlab/logs:/var/log/gitlab \
  -v /home/gitlab/data:/var/opt/gitlab \
  twang2218/gitlab-ce-zh:latest


 ---
 docker run -d --hostname gitlab.example.com \
   -p 3000:3000 \
   -p 3443:443 \
   -p 3022:22 \
   --name gitlab \
   --restart unless-stopped \
   twang2218/gitlab-ce-zh:latest

----
1.ok
docker run -d  \
    -p 3000:80 \
    -p 3022:22 \
    --name gitlab \
    twang2218/gitlab-ce-zh:8.17.3

docker run -d -p 3000:80 twang2218/gitlab-ce-zh:8.17.3

2.hostname
docker run -d  \
    --hostname gitlab.example.com  \
    -p 3000:80 \
    -p 3022:22 \
    --name gitlab \
    twang2218/gitlab-ce-zh:8.17.3
```


gitlab 部署命令
---------------------

### 运行 gitlab

https://docs.gitlab.com/omnibus/docker/README.html

```
docker run -d --hostname gitlab.example.com \
  -p 3000:3000 \
  -p 3443:443 \
  -p 3022:22 \
  --name gitlab \
  --restart unless-stopped \
  -v /home/gitlab/config:/etc/gitlab \
  -v /home/gitlab/logs:/var/log/gitlab \
  -v /home/gitlab/data:/var/opt/gitlab \
  twang2218/gitlab-ce-zh:latest
```

### 升级 gitlab

```
docker pull twang2218/gitlab-ce-zh:latest
docker stop gitlab
docker rm gitlab
docker run -d --hostname gitlab.example.com \
  -p 3000:3000 \
  -p 3080:80 \
  -p 3443:443 \
  -p 3022:22 \
  --name gitlab \
  --restart unless-stopped \
  -v /home/gitlab/config:/etc/gitlab \
  -v /home/gitlab/logs:/var/log/gitlab \
  -v /home/gitlab/data:/var/opt/gitlab \
  twang2218/gitlab-ce-zh:latest
```

### 查看日志

```
docker logs gitlab -f
```


### 运行 runner

https://docs.gitlab.com/runner/install/docker.html

首先添加 CA 文件到 `/home/gitlab/gitlab-runner/certs/ca.crt`

使用`docker login` 命令登陆相关仓库

```
docker login gitlab.example.com:3000
```

运行 runner

```
docker run -d --name gitlab-runner --restart always \
  --network gitlab-net  \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/gitlab/gitlab-runner:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest
```

```
docker exec -it gitlab-runner bash
```

```
gitlab-ci-multi-runner register -n \
  --url http://gitlab.example.com/ \
  --registration-token S-GfSsvdepxSxeFuaX2u \
  --executor docker \
  --description "Docker Runner" \
  --docker-image "docker:latest" \
  --docker-network gitlab-net  \
  --docker-volumes /var/run/docker.sock:/var/run/docker.sock

```

### 升级 runner

```
docker pull gitlab/gitlab-runner:latest
docker stop gitlab-runner
docker rm gitlab-runner
docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/gitlab/gitlab-runner:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest
```

1.
docker run -d \
    --hostname gitlab.example.com \
    -p 80:80 \
    -p 443:443 \
    -p 22:22 \
    --name gitlab \
    --restart unless-stopped \
    -v gitlab-config:/etc/gitlab \
    -v gitlab-logs:/var/log/gitlab \
    -v gitlab-data:/var/opt/gitlab \
    --network gitlab-net \
    twang2218/gitlab-ce-zh:8.17.3

2.runner

➜  gitlab docker run -d --name gitlab-runner --restart always \
  --network gitlab-net  \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v `pwd`/gitlab-runner:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest
4a169943bba3ac69a8e5b0cdb3017927a44464a4ddad2025a392476323ea5e19
➜  gitlab docker logs -f gitlab-runner



3.
自签名 CA

```
mkdir -p /etc/docker/certs.d/apk.302e.com:3000/
mkdir -p /home/gitlab/gitlab-runner/certs/
cat > /home/gitlab/gitlab-runner/certs/ca.crt << EOL
EOL
```



-------------------
gitlab

# --network gitlab-net \
docker run -d \
    --hostname gitlab.example.com \
    -p 80:80 \
    -p 443:443 \
    -p 22:22 \
    --name gitlab \
    --restart always \
    -v gitlab-config:/etc/gitlab \
    -v gitlab-logs:/var/log/gitlab \
    -v gitlab-data:/var/opt/gitlab \
    twang2218/gitlab-ce-zh:8.17.3


gitlab-ci-runner

docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v `pwd`/gitlab-runner:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest

sudo curl --output /usr/local/bin/gitlab-ci-multi-runner https://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-ci-multi-runner-darwin-amd64


## 使用阿里镜像 docker pull registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh

sudo docker run -d \
    --hostname tplinux.cn \
    -p 10080:80 \
    -p 10022:22 \
    --name gitlab \
    --restart always \
    -v `pwd`/gitlab-config:/etc/gitlab \
    -v `pwd`/gitlab-logs:/var/log/gitlab \
    -v `pwd`/gitlab-data:/var/opt/gitlab \
    twang2218/gitlab-ce-zh