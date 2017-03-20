## gitlab ci 使用

    安装教程
    https://docs.gitlab.com/runner/install/
    https://docs.gitlab.com/runner/install/docker.html
    
由于公司gitlab 已经配置好runner, 只需要在项目中编写ci 配置文件
```concept
➜  stu_ci git:(master) ✗ ll
total 24
drwxr-xr-x   7 apple  staff  238 Feb  8 09:40 .
drwxr-xr-x  19 apple  staff  646 Feb  7 21:43 ..
drwxr-xr-x  14 apple  staff  476 Feb  8 09:42 .git
-rw-r--r--   1 apple  staff  420 Feb  7 21:47 .gitlab-ci.yml    #ci 配置文件
-rw-r--r--   1 apple  staff  914 Feb  7 21:49 Makefile          #makefile
drwxr-xr-x   4 apple  staff  136 Feb  8 09:30 build
-rw-r--r--   1 apple  staff   66 Feb  8 09:40 main.go           #主程序
➜  stu_ci git:(master) 

```

ci 配置文件
```concept
image: golang:latest

before_script:
- go version
- go env
- mkdir -p $GOPATH/src
- ln -s $(pwd) $GOPATH/src/stu_ci

stages:
#  - test
  - build
#  - deploy

build:
  stage: build
  script:
  - make build
  - ls -la build/linux-amd64
  - build/linux-amd64/stu_ci version
#   only:
#   - master
  artifacts:
    name: "${CI_BUILD_NAME}_${CI_BUILD_REF_NAME}"
    paths:
    - build/linux-amd64/stu_ci
    expire_in: 1 week
```

## 运行效果

