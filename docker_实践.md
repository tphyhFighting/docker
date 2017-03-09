## docker 实践



#0x00 docker 概念
    
    0.资源
    http://www.docker.org.cn/book/docker/docker-download-image-7.html
    https://yeasy.gitbooks.io/docker_practice/content/appendix/faq/
    
    1.安装
    http://wiki.jikexueyuan.com/project/docker/installation/mac.html
    
    
    2.
    为获得访问Docker权限可以直接在命令前加sudo，或者采取以下步骤授予权限：：
        # 如果还没有docker group就添加一个：
        $ sudo groupadd docker
        # 将用户加入该group内。然后退出并重新登录即可生效。
        $ sudo gpasswd -a ${USER} docker
        # 重启docker
        $ sudo service docker restart
    
#0x01 docker 常用命令
    1.docker login
    (hyhlinux)
    
    2.搜索镜像 (可以直接登陆到官网进行搜索)
    docker search hyhlinux
    docker search tutorial #搜索到该镜像后可以查看其描述
    
    3.下载容器镜像
    docker pull learn/tutorial
    
    4.docker --help
```concept
[root@centos-linux-1 ~]# docker
Usage: docker [OPTIONS] COMMAND [arg...]
       docker [ --help | -v | --version ]
A self-sufficient runtime for containers.
Options:
  --config=~/.docker              Location of client config files
  -D, --debug                     Enable debug mode
  -H, --host=[]                   Daemon socket(s) to connect to
  -h, --help                      Print usage
  -l, --log-level=info            Set the logging level
  --tls                           Use TLS; implied by --tlsverify
  --tlscacert=~/.docker/ca.pem    Trust certs signed only by this CA
  --tlscert=~/.docker/cert.pem    Path to TLS certificate file
  --tlskey=~/.docker/key.pem      Path to TLS key file
  --tlsverify                     Use TLS and verify the remote
  -v, --version                   Print version information and quit
Commands:
    attach    Attach to a running container
    build     Build an image from a Dockerfile
    commit    Create a new image from a container's changes
    cp        Copy files/folders between a container and the local filesystem
    create    Create a new container
    diff      Inspect changes on a container's filesystem
    events    Get real time events from the server
    exec      Run a command in a running container
    export    Export a container's filesystem as a tar archive
    history   Show the history of an image
    images    List images
    import    Import the contents from a tarball to create a filesystem image
    info      Display system-wide information
    inspect   Return low-level information on a container, image or task
    kill      Kill one or more running containers
    load      Load an image from a tar archive or STDIN
    login     Log in to a Docker registry.
    logout    Log out from a Docker registry.
    logs      Fetch the logs of a container
    network   Manage Docker networks
    node      Manage Docker Swarm nodes
    pause     Pause all processes within one or more containers
    port      List port mappings or a specific mapping for the container
    ps        List containers
    pull      Pull an image or a repository from a registry
    push      Push an image or a repository to a registry
    rename    Rename a container
    restart   Restart a container
    rm        Remove one or more containers
    rmi       Remove one or more images
    run       Run a command in a new container
    save      Save one or more images to a tar archive (streamed to STDOUT by default)
    search    Search the Docker Hub for images
    service   Manage Docker services
    start     Start one or more stopped containers
    stats     Display a live stream of container(s) resource usage statistics
    stop      Stop one or more running containers
    swarm     Manage Docker Swarm
    tag       Tag an image into a repository
    top       Display the running processes of a container
    unpause   Unpause all processes within one or more containers
    update    Update configuration of one or more containers
    version   Show the Docker version information
    volume    Manage Docker volumes
    wait      Block until a container stops, then print its exit code
Run 'docker COMMAND --help' for more information on a command.
[root@centos-linux-1 ~]# 
docker run --help
```   
    
#0x02 docker 基本使用

   1.在docker容器中运行hello world!
   
    docker run命令有两个参数，一个是镜像名，一个是要在镜像中运行的命令
    docker run learn/tutorial echo "hello word"
   
   2.在容器中安装新的程序
   
    docker run learn/tutorial apt-get install -y ping
    
    
   3.保存对容器的修改
    
    首先使用docker ps -l命令获得安装完ping命令之后容器的id。然后把这个镜像保存为learn/ping。
    
    提示：
    1. 运行docker commit，可以查看该命令的参数列表。
    2. 你需要指定要提交保存容器的ID。(译者按：通过docker ps -l 命令获得id值)
    3. 无需拷贝完整的id，通常来讲最开始的三至四个字母即可区分。（译者按：非常类似git里面的版本号)
    正确的命令：
    $docker commit 698 learn/ping    #注意镜像的名字已经更新，可以在deocker官网登陆查看
   
   4.运行新的镜像
   
    提示：
    一定要使用新的镜像名learn/ping来运行ping命令。(译者按：最开始下载的learn/tutorial镜像中是没有ping命令的)
    docker run lean/ping ping www.google.com

  5.检查运行中的镜像    
  
    使用docker ps命令可以查看所有正在运行中的容器列表，
    使用docker inspect命令我们可以查看更详细的关于某一个容器的信息。
    
    
    目标：
        docker ps ->获取id
        docker inspect id
        查找某一个运行中容器的id，然后使用docker inspect命令查看容器的信息。
        
    提示：
        可以使用镜像id的前面部分，不需要完整的id。
    正确的命令：
    $ docker inspect id
    
  6.发布自己的镜像  
   
    现在我们已经验证了新镜像可以正常工作，下一步我们可以将其发布到官方的索引网站。
    还记得我们最开始下载的learn/tutorial镜像吧，我们也可以把我们自己编译的镜像发布到索引页面，
    一方面可以自己重用，另一方面也可以分享给其他人使用。
    目标：
        把learn/ping镜像发布到docker的index网站。
    提示：
        1. docker images命令可以列出所有安装过的镜像。
        2. docker push命令可以将某一个镜像发布到官方网站。
        3. 你只能将镜像发布到自己的空间下面。这个模拟器登录的是learn帐号。
        
    docker push learn/ping
    原文地址：
    http://www.docker.org.cn/book/docker/docker-push-image-13.html

#0x03 运行
     sudo docker run -t -i ubuntu:14.04 /bin/bash
```concept
ubuntu@VM-103-136-ubuntu:~$ sudo docker run -t -i ubuntu:14.04 /bin/bash
root@ba936d84c4cc:/# pwd
/
root@ba936d84c4cc:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@ba936d84c4cc:/# ipaddr
bash: ipaddr: command not found
root@ba936d84c4cc:/# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
20: eth0: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:09 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.9/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:9/64 scope link 
       valid_lft forever preferred_lft forever
root@ba936d84c4cc:/# 
```
     
#0x03 docker 使用案例
    1.redis
```concept
ubuntu@VM-103-136-ubuntu:~$ sudo docker run -t -i ubuntu:14.04 /bin/bash
root@998f7fdcf75d:/# apt-get update 
root@998f7fdcf75d:/# apt-get install redis-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
libjemalloc1 redis-tools
The following NEW packages will be installed:
libjemalloc1 redis-server redis-tools
0 upgraded, 3 newly installed, 0 to remove and 5 not upgraded.
Need to get 410 kB of archives.
After this operation, 1272 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu/ trusty/universe libjemalloc1 amd64 3.5.1-2 [76.8 kB]
Get:2 http://archive.ubuntu.com/ubuntu/ trusty/universe redis-tools amd64 2:2.8.4-2 [65.7 kB]
Get:3 http://archive.ubuntu.com/ubuntu/ trusty/universe redis-server amd64 2:2.8.4-2 [267 kB]
Fetched 410 kB in 2s (163 kB/s)   
root@998f7fdcf75d:/# exit
ubuntu@VM-103-136-ubuntu:~$ sudo docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
998f7fdcf75d        ubuntu:14.04        "/bin/bash"         2 minutes ago       Exited (0) 32 seconds ago                       backstabbing_poincare   
ubuntu@VM-103-136-ubuntu:~$ 
ubuntu@VM-103-136-ubuntu:~$ sudo docker commit 998 hyhlinux/redis
2efb23b095b77161f86d9f37d4a474fe10f2fc7332b2955feaa4f46d2856e1dd
ubuntu@VM-103-136-ubuntu:~$
ubuntu@VM-103-136-ubuntu:~$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
hyhlinux/redis      latest              2efb23b095b7        44 seconds ago      212.5 MB
ubuntu              14.04               bea27a731213        2 weeks ago         188 MB
``` 
    2.go 跨平台开发
     https://hub.docker.com/r/library/golang/
     参考golang 的使用说明:
     docker run --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang:1.6 go build -v
    
    3. 直接在docker 进行测试
 ```concept
 image: golang:latest
 before_script:
 - go version
 - go env
 - mkdir -p $GOPATH/src
 - ln -s $(pwd) $GOPATH/src/imgfit
 - cd $GOPATH/src/imgfit        #解决编译环境问题
 stages:
 #  - test
   - build
 #  - deploy
 build:
   stage: build
   script:
 #  - pwd
 #  - ls -la
 #  - ls -la $GOPATH
 #  - ls -la $GOPATH/src/imgfit/
   - make build
   - ls -la build/linux-amd64
 #  - build/linux-amd64/imgfit version
 #   only:
 #   - master
   artifacts:
     name: "${CI_BUILD_NAME}_${CI_BUILD_REF_NAME}"
     paths:
     - build/linux-amd64/imgfit
     expire_in: 1 week

```   
## 0x04
 imgfit :ci 测试失败
 解决：目录问题
 /go/src/imgfit  下编译ok
```concept
➜  imgfit git:(ci) docker run --rm -it -v "`pwd`":/builds/apkpure/imgfit  golang:latest bash 
root@f821c304a5d2:/go# 
root@f821c304a5d2:/go# ls -l /builds/
total 4
drwxr-xr-x 3 root root 4096 Feb 14 03:06 apkpure
root@f821c304a5d2:/go# ls -l /builds/apkpure/
total 0
drwxr-xr-x 15 root root 510 Feb 14 02:57 imgfit
root@f821c304a5d2:/go# ls -l /builds/apkpure/imgfit/
total 32
-rw-r--r-- 1 root root   914 Feb 14 02:46 Makefile
drwxr-xr-x 4 root root   136 Jan 16 13:14 build
-rw-r--r-- 1 root root   258 Jan 16 13:17 config.json
-rw-r--r-- 1 root root   762 Jan 16 13:12 glide.lock
-rw-r--r-- 1 root root   159 Jan 16 13:12 glide.yaml
-rw-r--r-- 1 root root 11806 Feb 10 09:20 main.go
-rw-r--r-- 1 root root  1994 Jan 16 13:12 main_test.go
drwxr--r-- 2 root root    68 Feb 10 09:59 upload
drwxr-xr-x 4 root root   136 Jan 16 13:12 vendor
root@f821c304a5d2:/go# go env
GOARCH="amd64"
GOBIN=""
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOOS="linux"
GOPATH="/go"
GORACE=""
GOROOT="/usr/local/go"
GOTOOLDIR="/usr/local/go/pkg/tool/linux_amd64"
CC="gcc"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build765616323=/tmp/go-build -gno-record-gcc-switches"
CXX="g++"
CGO_ENABLED="1"
root@f821c304a5d2:/go# mkdir -p $GOPATH/src
root@f821c304a5d2:/go# ls -l $GOPATH/src
total 0
root@f821c304a5d2:/go# ls -l $GOPATH/   
total 8
drwxrwxrwx 2 root root 4096 Dec 13 23:25 bin
drwxrwxrwx 2 root root 4096 Dec 13 23:25 src
root@f821c304a5d2:/go# cd /builds/apkpure/imgfit/
root@f821c304a5d2:/builds/apkpure/imgfit# pwd
/builds/apkpure/imgfit
root@f821c304a5d2:/builds/apkpure/imgfit# ln -s $(pwd) $GOPATH/src/imgfit
root@f821c304a5d2:/builds/apkpure/imgfit# pwd
/builds/apkpure/imgfit
root@f821c304a5d2:/builds/apkpure/imgfit# ls -la
total 56
drwxr-xr-x 15 root root   510 Feb 14 02:57 .
drwxr-xr-x  3 root root  4096 Feb 14 03:06 ..
-rw-r--r--  1 root root 10244 Jan 20 04:25 .DS_Store
drwxr-xr-x 16 root root   544 Feb 14 03:06 .git
-rw-r--r--  1 root root   336 Jan 16 13:12 .gitignore
-rw-r--r--  1 root root   490 Feb 14 02:57 .gitlab-ci.yml
-rw-r--r--  1 root root   914 Feb 14 02:46 Makefile
drwxr-xr-x  4 root root   136 Jan 16 13:14 build
-rw-r--r--  1 root root   258 Jan 16 13:17 config.json
-rw-r--r--  1 root root   762 Jan 16 13:12 glide.lock
-rw-r--r--  1 root root   159 Jan 16 13:12 glide.yaml
-rw-r--r--  1 root root 11806 Feb 10 09:20 main.go
-rw-r--r--  1 root root  1994 Jan 16 13:12 main_test.go
drwxr--r--  2 root root    68 Feb 10 09:59 upload
drwxr-xr-x  4 root root   136 Jan 16 13:12 vendor
root@f821c304a5d2:/builds/apkpure/imgfit# make build
mkdir -p build/`go env GOHOSTOS`-`go env GOHOSTARCH`
go build -ldflags "-X main.AppVersion=`git describe --tags` -X main.BuildTime=`date '+%Y-%m-%d_%H:%M:%S'`"  -o build/`go env GOHOSTOS`-`go env GOHOSTARCH`/imgfit ./
main.go:15:2: cannot find package "github.com/chai2010/webp" in any of:
	/usr/local/go/src/github.com/chai2010/webp (from $GOROOT)
	/go/src/github.com/chai2010/webp (from $GOPATH)
main.go:16:2: cannot find package "github.com/disintegration/imaging" in any of:
	/usr/local/go/src/github.com/disintegration/imaging (from $GOROOT)
	/go/src/github.com/disintegration/imaging (from $GOPATH)
main.go:17:2: cannot find package "github.com/goamz/goamz/aws" in any of:
	/usr/local/go/src/github.com/goamz/goamz/aws (from $GOROOT)
	/go/src/github.com/goamz/goamz/aws (from $GOPATH)
main.go:18:2: cannot find package "github.com/goamz/goamz/s3" in any of:
	/usr/local/go/src/github.com/goamz/goamz/s3 (from $GOROOT)
	/go/src/github.com/goamz/goamz/s3 (from $GOPATH)
main.go:19:2: cannot find package "github.com/golang/glog" in any of:
	/usr/local/go/src/github.com/golang/glog (from $GOROOT)
	/go/src/github.com/golang/glog (from $GOPATH)
main.go:24:2: cannot find package "golang.org/x/image/bmp" in any of:
	/usr/local/go/src/golang.org/x/image/bmp (from $GOROOT)
	/go/src/golang.org/x/image/bmp (from $GOPATH)
Makefile:26: recipe for target 'build' failed
make: *** [build] Error 1
root@f821c304a5d2:/builds/apkpure/imgfit# ls -la $GOPATH/
bin/ src/ 
root@f821c304a5d2:/builds/apkpure/imgfit# ls -la $GOPATH/
bin/ src/ 
root@f821c304a5d2:/builds/apkpure/imgfit# ls -la $GOPATH/src/imgfit
lrwxrwxrwx 1 root root 22 Feb 14 03:08 /go/src/imgfit -> /builds/apkpure/imgfit
root@f821c304a5d2:/builds/apkpure/imgfit# ls -la $GOPATH/src/imgfit/
total 56
drwxr-xr-x 15 root root   510 Feb 14 02:57 .
drwxr-xr-x  3 root root  4096 Feb 14 03:06 ..
-rw-r--r--  1 root root 10244 Jan 20 04:25 .DS_Store
drwxr-xr-x 16 root root   544 Feb 14 03:06 .git
-rw-r--r--  1 root root   336 Jan 16 13:12 .gitignore
-rw-r--r--  1 root root   490 Feb 14 02:57 .gitlab-ci.yml
-rw-r--r--  1 root root   914 Feb 14 02:46 Makefile
drwxr-xr-x  4 root root   136 Jan 16 13:14 build
-rw-r--r--  1 root root   258 Jan 16 13:17 config.json
-rw-r--r--  1 root root   762 Jan 16 13:12 glide.lock
-rw-r--r--  1 root root   159 Jan 16 13:12 glide.yaml
-rw-r--r--  1 root root 11806 Feb 10 09:20 main.go
-rw-r--r--  1 root root  1994 Jan 16 13:12 main_test.go
drwxr--r--  2 root root    68 Feb 10 09:59 upload
drwxr-xr-x  4 root root   136 Jan 16 13:12 vendor
root@f821c304a5d2:/builds/apkpure/imgfit# go build
main.go:15:2: cannot find package "github.com/chai2010/webp" in any of:
	/usr/local/go/src/github.com/chai2010/webp (from $GOROOT)
	/go/src/github.com/chai2010/webp (from $GOPATH)
main.go:16:2: cannot find package "github.com/disintegration/imaging" in any of:
	/usr/local/go/src/github.com/disintegration/imaging (from $GOROOT)
	/go/src/github.com/disintegration/imaging (from $GOPATH)
main.go:17:2: cannot find package "github.com/goamz/goamz/aws" in any of:
	/usr/local/go/src/github.com/goamz/goamz/aws (from $GOROOT)
	/go/src/github.com/goamz/goamz/aws (from $GOPATH)
main.go:18:2: cannot find package "github.com/goamz/goamz/s3" in any of:
	/usr/local/go/src/github.com/goamz/goamz/s3 (from $GOROOT)
	/go/src/github.com/goamz/goamz/s3 (from $GOPATH)
main.go:19:2: cannot find package "github.com/golang/glog" in any of:
	/usr/local/go/src/github.com/golang/glog (from $GOROOT)
	/go/src/github.com/golang/glog (from $GOPATH)
main.go:24:2: cannot find package "golang.org/x/image/bmp" in any of:
	/usr/local/go/src/golang.org/x/image/bmp (from $GOROOT)
	/go/src/golang.org/x/image/bmp (from $GOPATH)
root@f821c304a5d2:/builds/apkpure/imgfit# env
GOLANG_VERSION=1.7.4
HOSTNAME=f821c304a5d2
TERM=xterm
PATH=/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/builds/apkpure/imgfit
GOLANG_DOWNLOAD_SHA256=47fda42e46b4c3ec93fa5d4d4cc6a748aa3f9411a2a2b7e08e3a6d80d753ec8b
SHLVL=1
HOME=/root
no_proxy=127.0.0.1, localhost
GOPATH=/go
GOLANG_DOWNLOAD_URL=https://golang.org/dl/go1.7.4.linux-amd64.tar.gz
_=/usr/bin/env
OLDPWD=/go
root@f821c304a5d2:/builds/apkpure/imgfit# ll vendor/
bash: ll: command not found
root@f821c304a5d2:/builds/apkpure/imgfit# ll vendor/^C
root@f821c304a5d2:/builds/apkpure/imgfit# ls -l vendor/
total 0
drwxr-xr-x 7 root root 238 Jan 16 13:12 github.com
drwxr-xr-x 3 root root 102 Jan 16 13:12 golang.org
root@f821c304a5d2:/builds/apkpure/imgfit# cd $GOPATH/src/imgfit/
root@f821c304a5d2:/go/src/imgfit# ll
bash: ll: command not found
root@f821c304a5d2:/go/src/imgfit# pwd
/go/src/imgfit
root@f821c304a5d2:/go/src/imgfit# ls
Makefile  build  config.json  glide.lock  glide.yaml  main.go  main_test.go  upload  vendor
root@f821c304a5d2:/go/src/imgfit# go build
root@f821c304a5d2:/go/src/imgfit# 
root@f821c304a5d2:/go/src/imgfit# 

```
##0x05 docker python 
```concept
➜  abuse-robot git:(m_hyh_ci) ✗ docker run --rm -it -v "`pwd`":/abuse-robot/  python:2.7.13 bash -c "cd /abuse-robot/ && pip install -r requirements.txt && python main.py"
Collecting redis==2.10.5 (from -r requirements.txt (line 1))
  Downloading redis-2.10.5-py2.py3-none-any.whl (60kB)
    100% |████████████████████████████████| 61kB 40kB/s 
Installing collected packages: redis
Successfully installed redis-2.10.5
main test
➜  abuse-robot git:(m_hyh_ci) ✗ 
```


##0x06 ci
```concept
Running with gitlab-ci-multi-runner 1.10.4 (b32125f)
Using Docker executor with image docker:latest ...
Pulling docker image docker:latest ...
Running on runner-0d787024-project-43-concurrent-0 via a1bcddf5301d...
Fetching changes...
HEAD is now at 718cc4a abuse-robot: add build-images/run
From https://apk.302e.com:3443/apkpure/abuse-robot
 + 718cc4a...59377fc m_hyh_ci   -> origin/m_hyh_ci  (forced update)
Checking out 59377fcf as m_hyh_ci...
Skipping Git submodules setup
$ docker login -u gitlab-ci-token -p $CI_BUILD_TOKEN apk.302e.com:3000
Login Succeeded
$ docker build --pull -t $CONTAINER_TEST_IMAGE .
Sending build context to Docker daemon 180.2 kB

Step 1/6 : FROM python:2.7.13
2.7.13: Pulling from library/python
Digest: sha256:d23845e4757f13266b42877c25b845e455127b85ec12e5d551bec5d8162e7cd4
Status: Image is up to date for python:2.7.13
 ---> b4b107fcc777
Step 2/6 : ADD . /abuse-robot
 ---> 1bda4ebe038b
Removing intermediate container 4c2416ad17ac
Step 3/6 : WORKDIR /abuse-robot
 ---> c349872f21c2
Removing intermediate container 8948344c2ab9
Step 4/6 : RUN apt-get update --fix-missing && apt-get -y install redis-server && pip install -r requirements.txt
 ---> Running in ff948f736363
Get:1 http://security.debian.org jessie/updates InRelease [63.1 kB]
Get:2 http://security.debian.org jessie/updates/main amd64 Packages [438 kB]
Ign http://deb.debian.org jessie InRelease
Get:3 http://deb.debian.org jessie-updates InRelease [145 kB]
Get:4 http://deb.debian.org jessie Release.gpg [2373 B]
Get:5 http://deb.debian.org jessie Release [148 kB]
Get:6 http://deb.debian.org jessie-updates/main amd64 Packages [17.6 kB]
Get:7 http://deb.debian.org jessie/main amd64 Packages [9049 kB]
Fetched 9863 kB in 12s (779 kB/s)
Reading package lists...
Reading package lists...
Building dependency tree...
Reading state information...
The following extra packages will be installed:
  init-system-helpers libjemalloc1 redis-tools
The following NEW packages will be installed:
  init-system-helpers libjemalloc1 redis-server redis-tools
0 upgraded, 4 newly installed, 0 to remove and 9 not upgraded.
Need to get 491 kB of archives.
After this operation, 1526 kB of additional disk space will be used.
Get:1 http://deb.debian.org/debian/ jessie/main libjemalloc1 amd64 3.6.0-3 [89.1 kB]
Get:2 http://deb.debian.org/debian/ jessie/main init-system-helpers all 1.22 [14.0 kB]
Get:3 http://deb.debian.org/debian/ jessie/main redis-tools amd64 2:2.8.17-1+deb8u5 [79.6 kB]
Get:4 http://deb.debian.org/debian/ jessie/main redis-server amd64 2:2.8.17-1+deb8u5 [308 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 491 kB in 3s (139 kB/s)
Selecting previously unselected package libjemalloc1.
(Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 21599 files and directories currently installed.)
Preparing to unpack .../libjemalloc1_3.6.0-3_amd64.deb ...
Unpacking libjemalloc1 (3.6.0-3) ...
Selecting previously unselected package init-system-helpers.
Preparing to unpack .../init-system-helpers_1.22_all.deb ...
Unpacking init-system-helpers (1.22) ...
Selecting previously unselected package redis-tools.
Preparing to unpack .../redis-tools_2%3a2.8.17-1+deb8u5_amd64.deb ...
Unpacking redis-tools (2:2.8.17-1+deb8u5) ...
Selecting previously unselected package redis-server.
Preparing to unpack .../redis-server_2%3a2.8.17-1+deb8u5_amd64.deb ...
Unpacking redis-server (2:2.8.17-1+deb8u5) ...
Processing triggers for systemd (215-17+deb8u6) ...
Setting up libjemalloc1 (3.6.0-3) ...
Setting up init-system-helpers (1.22) ...
Setting up redis-tools (2:2.8.17-1+deb8u5) ...
Setting up redis-server (2:2.8.17-1+deb8u5) ...
adduser: Warning: The home directory `/var/lib/redis' does not belong to the user you are currently creating.
invoke-rc.d: policy-rc.d denied execution of start.
Processing triggers for libc-bin (2.19-18+deb8u7) ...
Processing triggers for systemd (215-17+deb8u6) ...
Collecting redis==2.10.5 (from -r requirements.txt (line 1))
  Downloading redis-2.10.5-py2.py3-none-any.whl (60kB)
Installing collected packages: redis
Successfully installed redis-2.10.5
 ---> 5a169402f023
Removing intermediate container ff948f736363
Step 5/6 : EXPOSE 6379
 ---> Running in 23992cfb37d3
 ---> c6e4b4bec1a5
Removing intermediate container 23992cfb37d3
Step 6/6 : CMD sh run.sh
 ---> Running in 1323e4a3598f
 ---> 2a31fce65cb9
Removing intermediate container 1323e4a3598f
Successfully built 2a31fce65cb9
$ docker push $CONTAINER_TEST_IMAGE
The push refers to a repository [apk.302e.com:3000/apkpure/abuse-robot]
5ac651d92e9c: Preparing
f3d82424ae1c: Preparing
1e0ea159a3a9: Preparing
46d1cfdcff17: Preparing
bd7dcb3e1bc1: Preparing
98816c9818bb: Preparing
30339f20ced0: Preparing
0eb22bfb707d: Preparing
a2ae92ffcd29: Preparing
98816c9818bb: Waiting
30339f20ced0: Waiting
0eb22bfb707d: Waiting
a2ae92ffcd29: Waiting
bd7dcb3e1bc1: Layer already exists
46d1cfdcff17: Layer already exists
1e0ea159a3a9: Layer already exists
98816c9818bb: Layer already exists
30339f20ced0: Layer already exists
0eb22bfb707d: Layer already exists
a2ae92ffcd29: Layer already exists
f3d82424ae1c: Pushed
5ac651d92e9c: Pushed
m_hyh_ci: digest: sha256:ac624bf794da861200a57d2d56172d0dc731d2358fa5f3f0a87a8aa97d64e781 size: 2221
$ docker images
REPOSITORY                              TAG                 IMAGE ID            CREATED             SIZE
apk.302e.com:3000/apkpure/abuse-robot   m_hyh_ci            2a31fce65cb9        3 seconds ago       692 MB
apk.302e.com:3000/apkpure/abuse-robot   <none>              a4bbf1cee0c1        3 minutes ago       692 MB
apk.302e.com:3000/apkpure/abuse-robot   <none>              f860b1203fe3        14 minutes ago      692 MB
twang2218/gitlab-ce-zh                  latest              0575b61be32b        2 days ago          1.2 GB
apk.302e.com:3000/apkpure/wapol         latest              004452cdee33        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         master              004452cdee33        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         v0.7                54387e7f3e9f        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              bb8bfe586696        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         _v0.8               126f073b83c8        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         ci-test             21465e0aa654        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              97e3915247ca        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              25659902ba4e        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              b492242ebe95        3 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         _v0.7               92c4415c85b9        4 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              0b12f8d73311        4 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         _ci-test            b2d045d97350        4 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         dev-v0.7            1a880abb101a        4 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              8fd1b152fec5        4 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         dev-ci-test         c3d310044e6f        4 days ago          91.8 MB
apk.302e.com:3000/apkpure/wapol         <none>              3a1f4f0f2c85        4 days ago          91.8 MB
<none>                                  <none>              84de69d495a6        4 days ago          91.8 MB
<none>                                  <none>              a86ea2ed9433        4 days ago          91.8 MB
<none>                                  <none>              416c5701fe8c        4 days ago          91.8 MB
192.168.0.18:5000/android-sdk           25.0.2              694fc60cdd87        9 days ago          2.5 GB
tnextday/android-sdk                    25.0.2              694fc60cdd87        9 days ago          2.5 GB
python                                  2.7.13              b4b107fcc777        10 days ago         679 MB
docker                                  latest              5ab87264167a        10 days ago         93.8 MB
gitlab/gitlab-runner-helper             x86_64-b32125f      c3fe4ae90c41        13 days ago         38.8 MB
gitlab/gitlab-runner                    latest              7017969b6fd6        2 weeks ago         402 MB
golang                                  1.7                 7afbc2b03b9e        3 weeks ago         675 MB
golang                                  latest              7afbc2b03b9e        3 weeks ago         675 MB
twang2218/gitlab-ce-zh                  <none>              a132c5e7f5e1        3 weeks ago         1.18 GB
docker                                  dind                7d6978320b24        4 weeks ago         99 MB
docker                                  <none>              9aa3005db491        4 weeks ago         93.7 MB
debian                                  jessie-slim         7d86024f45a4        4 weeks ago         79.9 MB
gitlab/gitlab-runner-helper             x86_64-ade6572      bd808d1fffdb        5 weeks ago         39.8 MB
docker                                  <none>              2102ff6d9b43        5 weeks ago         110 MB
docker                                  <none>              46d1f5d13fa8        5 weeks ago         105 MB
twang2218/gitlab-ce-zh                  8.15.3              2da6c300c31f        6 weeks ago         1.22 GB
twang2218/gitlab-ce-zh                  8.15                01b9d15a7a01        6 weeks ago         1.22 GB
gitlab/gitlab-runner                    <none>              879ee844b4a0        6 weeks ago         421 MB
golang                                  <none>              6639f812dbc7        2 months ago        674 MB
snowdream/android                       25                  1371bb44a3ae        2 months ago        2.27 GB
registry                                latest              c6c14b3960bd        6 months ago        33.3 MB
Build succeeded

```
##0x06 目录映射
    1.-v 目录映射
    2.-w 设置工作路径 
    3.-it 终端tty 运行
    
➜  abuse-robot git:(4-docker-ci) ✗ docker run  -it -v `pwd`:/abuse-robot  -w /abuse-robot mail:v1.0 bash
root@eebe05815303:/abuse-robot# 



##0x07 登陆私有的docker 仓库 (gitlab 公司)
Status: Downloaded newer image for python:2.7-slim
➜  test docker login apk.302e.com:3000
Username (xxx): 
Password: 
Login Succeeded
➜  test docker run -it apk.302e.com:3000/apkpure/abuse-robot:4-docker-ci bash


##0x08 删除镜像 rmi 
```concept
    先停止
➜  abuse-robot git:(4-docker-ci) ✗ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS                          PORTS               NAMES
9085e276b69f        3f14dc7c29da        "bash"              About a minute ago   Exited (0) About a minute ago                       quirky_chandrasekhar
3721c0ed8f75        3f14dc7c29da        "bash"              About a minute ago   Exited (0) About a minute ago                       cocky_bose
d583512d22d1        3f14dc7c29da        "bash"              5 minutes ago        Exited (0) 5 minutes ago                            competent_curran
-------------- 获取运行的dockerid
➜  abuse-robot git:(4-docker-ci) ✗ docker ps -qa
d509aaae76e8
65e8b4b4ead9
--------------
➜  abuse-robot git:(4-docker-ci) ✗ docker rm -f $(docker ps -qa)
9085e276b69f
3721c0ed8f75
d583512d22d1
➜  abuse-robot git:(4-docker-ci) ✗ docker ps -a                 
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
➜  abuse-robot git:(4-docker-ci) ✗

➜  abuse-robot git:(4-docker-ci) ✗ docker images                                                               
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              dbd338c7df49        3 days ago          690 MB
<none>              <none>              4b9275878b18        3 days ago          690 MB
python              latest              3984f3aafbc9        10 days ago         690 MB
python              2.7.13              b4b107fcc777        10 days ago         679 MB
docker              latest              5ab87264167a        10 days ago         93.8 MB
buildpack-deps      jessie              e560c65477a1        10 days ago         616 MB
python              2.7-slim            3f14dc7c29da        4 weeks ago         181 MB
debian              jessie              e5599115b6a6        4 weeks ago         123 MB
golang              latest              6639f812dbc7        2 months ago        674 MB
➜  abuse-robot git:(4-docker-ci) ✗ docker rmi dbd338c7df49 4b9275878b18 
Deleted: sha256:dbd338c7df49f2dc8f6858174f0d630bea77243b43ae3036aaa972d72367080f
Deleted: sha256:600d4987a2572225b7d924bb3ac2ace4de9ee9b578709842fc9888cf295f9e55
Deleted: sha256:01e1ab4384a2e236bef30184a0aee819e2ab8a67b8015da8b195b40e53ef0e5a
Deleted: sha256:68c34c8f90f2b973df691aca668e41bd2adaf499d9b08d683b3527176b19c477
Deleted: sha256:4b9275878b186e89539e18663aa0e124c6b53b24ecb394218a30a8ef42a4a31a
Deleted: sha256:c1630da9e652f8825ca806966a5af0e4e91bfc79f99ea15368b9dd4ec0633fee
Deleted: sha256:6fc4e176a9eda544cd15100c2ac9405ce75f555ef306263b7c9b0373597cc097
Deleted: sha256:c457da778308a6ce870271db462b38176527d01023a5c5bd941848ed65e9e29a
➜  abuse-robot git:(4-docker-ci) ✗ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
python              latest              3984f3aafbc9        10 days ago         690 MB
python              2.7.13              b4b107fcc777        10 days ago         679 MB
docker              latest              5ab87264167a        10 days ago         93.8 MB
buildpack-deps      jessie              e560c65477a1        10 days ago         616 MB
python              2.7-slim            3f14dc7c29da        4 weeks ago         181 MB
debian              jessie              e5599115b6a6        4 weeks ago         123 MB
golang              latest              6639f812dbc7        2 months ago        674 MB
➜  abuse-robot git:(4-docker-ci) ✗ 

```

##0x09  上传镜像
```concept
1.docker login
2.使用dockerfile 编译出本地镜像
docker build -t abuse-rotbot:v170222 .
3.修改本地镜像名&上传
➜  abuse-robot git:(4-docker-ci) ✗ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
abuse-robot         v2.0                d254f0c001c4        10 hours ago        228 MB
abuse-robot         v1.0                fb5681c0e348        11 hours ago        228 MB
python              latest              3984f3aafbc9        10 days ago         690 MB
python              2.7.13              b4b107fcc777        10 days ago         679 MB
docker              latest              5ab87264167a        11 days ago         93.8 MB
buildpack-deps      jessie              e560c65477a1        11 days ago         616 MB
python              2.7-slim            3f14dc7c29da        4 weeks ago         181 MB
python              2.7.13-slim         3f14dc7c29da        4 weeks ago         181 MB
debian              jessie              e5599115b6a6        5 weeks ago         123 MB
golang              latest              6639f812dbc7        2 months ago        674 MB
➜  abuse-robot git:(4-docker-ci) ✗ docker tag d254f0c001c4 hyhlinux/abuse-robot:v170223
➜  abuse-robot git:(4-docker-ci) ✗ docker images
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
abuse-robot            v2.0                d254f0c001c4        10 hours ago        228 MB
hyhlinux/abuse-robot   v170223             d254f0c001c4        10 hours ago        228 MB
abuse-robot            v1.0                fb5681c0e348        11 hours ago        228 MB
python                 latest              3984f3aafbc9        10 days ago         690 MB
python                 2.7.13              b4b107fcc777        10 days ago         679 MB
docker                 latest              5ab87264167a        11 days ago         93.8 MB
buildpack-deps         jessie              e560c65477a1        11 days ago         616 MB
python                 2.7-slim            3f14dc7c29da        4 weeks ago         181 MB
python                 2.7.13-slim         3f14dc7c29da        4 weeks ago         181 MB
debian                 jessie              e5599115b6a6        5 weeks ago         123 MB
golang                 latest              6639f812dbc7        2 months ago        674 MB
➜  abuse-robot git:(4-docker-ci) ✗ docker push hyhlinux/abuse-robot:v170223
The push refers to a repository [docker.io/hyhlinux/abuse-robot]
1c216da5c1c2: Pushed 
ea8568d6166b: Pushing [========>                                          ] 7.683 MB/46.66 MB
15f622595b7c: Pushed 
cfa53b6c8298: Pushed 
74790b8c949f: Mounted from library/python 
593e094824d2: Mounted from library/python 
a2ae92ffcd29: Mounted from library/python 
```

##0x0a  部署supervisor, docker 的主进程不能退出
```
FROM python:2.7.13-slim
ADD . /abuse-robot
ADD requirements.txt /abuse-robot/requirements.txt
EXPOSE      6379  9001
WORKDIR /abuse-robot
RUN apt-get update --fix-missing \
  && apt-get -y install redis-server \
  && apt-get -y install supervisor \
  && pip install -r requirements.txt \
  && mkdir -p /var/log/supervisor

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD /usr/bin/supervisord -n -c supervisord.conf
```

## supervisor 部署

##0x0a-1 
```
1.创建supervisor.conf
➜  webgp git:(master) ✗ echo_supervisord_conf > supervisor.conf
➜  webgp git:(master) ✗ vi supervisor.conf
add:
[program:foo] 
command=/bin/cat

mod: (web界面查看 / supervisorctl 命令行)
[inet_http_server]         ; inet (TCP) server disabled by default
port=127.0.0.1:9001        ; (ip_address:port specifier, *:port for all iface)
username=user              ; (default is no username (open server))
password=123               ; (default is no password (open server))


2.
➜  webgp git:(master) ✗ sudo supervisord -c supervisor.conf
Unlinking stale socket /tmp/supervisor.sock
➜  webgp git:(master) ✗ supervisorctl 
Server requires authentication
Username:user
Password:

foo                              RUNNING   pid 18794, uptime 0:00:14
supervisor> status
foo                              RUNNING   pid 18794, uptime 0:00:19
supervisor> stop 
Error: stop requires a process name
stop <name>   Stop a process
stop <gname>:*    Stop all processes in a group
stop <name> <name>  Stop multiple processes or groups
stop all    Stop all processes
supervisor> stop all
foo: stopped
supervisor> status
foo                              STOPPED   Feb 21 12:08 PM
supervisor> start
Error: start requires a process name
start <name>    Start a process
start <gname>:*   Start all processes in a group
start <name> <name> Start multiple processes or groups
start all   Start all processes
supervisor> start foo
foo: started
supervisor> status
foo                              RUNNING   pid 18802, uptime 0:00:05
supervisor>
``` 

##0x0a-2 部署go
![输入图片说明](https://static.oschina.net/uploads/img/201702/21130703_fyuc.png "在这里输入图片标题")

##0x0a-3 在容器中使用supervisor
```concept
-n: supervisor 在前台运行，这样容器的主进程就不会退出
➜  abuse-robot git:(4-docker-ci) docker run --rm -p 9002:9001 -it -v "`pwd`":/abuse-robot/ abuse-robot:v5.0 /usr/bin/supervisord -n -c supervisord.conf
2017-02-21 08:24:05,414 CRIT Supervisor running as root (no user in config file)
2017-02-21 08:24:05,430 INFO RPC interface 'supervisor' initialized
2017-02-21 08:24:05,430 INFO RPC interface 'supervisor' initialized
2017-02-21 08:24:05,431 CRIT Server 'unix_http_server' running without any HTTP authentication checking
2017-02-21 08:24:05,431 INFO supervisord started with pid 1
2017-02-21 08:24:06,439 INFO spawned: 'redis-server' with pid 7
2017-02-21 08:24:06,445 INFO spawned: 'abuse-robot' with pid 8
2017-02-21 08:24:06,451 INFO exited: redis-server (exit status 0; not expected)
2017-02-21 08:24:07,730 INFO spawned: 'redis-server' with pid 13
2017-02-21 08:24:07,731 INFO success: abuse-robot entered RUNNING state, process has stayed up for > than 1 seconds (startsecs)
2017-02-21 08:24:07,739 INFO exited: redis-server (exit status 0; not expected)
2017-02-21 08:24:07,741 CRIT reaped unknown pid 14)
```

