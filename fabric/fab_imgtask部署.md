##fabric 部署imgtask app
    1.serve
    (bug):gopath 
    
    2.worker 
    
Sample usage: 
```python
#coding:utf-8
from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm

import systemd
import utils
#ssh要用到的参数
#操作一致的服务器可以放在一组，同一组的执行同一套操作
env.roledefs = {
            'realserver1': ['root@192.168.9.3:22', ],
            'realserver2': ['root@192.168.9.4:22', ]
            }
env.password = 'tplinux'

#app config

app = "imgtask"
app_dir = "/root/go-dev/src/imgtask"
app_dir_local = "/Users/apple/go-dev/src/imgtask"
app_linux_bin = "build/linux-amd64/{}".format(app)
app_make_local = "{}/{}".format(app_dir_local, "Makefile")
__app = 'imgtask'
__description = 'Imgfit, APKPure custom imgfit service'
__version = 'v1.1'
__user = __app
__group = __user
__home_path = '/home/' + __user
__install_path = __home_path + '/' + __app
__upload = __home_path + '/upload'
__bin = __install_path + '/imgtask'
__package = "imgtask-linux-amd64-%s.tar.gz"
__package_loc = "file://package/"
fab_package = "/Users/apple/github/fabric_test/base2/package"
# __package_loc = "https://s3.pureapk.com/public/"

#1.压缩文件--local
def pack():
    with lcd(app_dir_local):
        with settings(warn_only=True):
            if not local("test -f %s" % app_make_local).failed:
                local("make clean")
                local("make docker")
                package = __package % __version
                local("cp {}/build/linux-amd64/{} {}".format(app_dir_local, package, fab_package))

#2.上传---local->remote
@roles('realserver1')
def put_task():
    dst = "{}/{}".format(app_dir, app)
    src = "{}/{}".format(app_dir_local, app_linux_bin)
    print(dst, src)
    with cd(app_dir):
        run("pwd")
        run("ls -l")
        put(src, dst)

#3.更新文件
@roles('realserver1')
def clean_app():
    with cd(app_dir):
        run("pwd")
        run('rm -rf {}'.format(app))
        run('ls -l ')

@roles("realserver1")
def imgtask_run():
    # with cd(app_dir):
    #     with settings(warn_only=True):
    #         if not run("test -f {}".format(app)).failed:
    #             run("./{} worker &".format(app))
    systemd_name = __app
    cmd = [__bin, ' worker']
    systemd.setup_simple(systemd_name,
                         app_run_cmd=' '.join(cmd),
                         work_path=__install_path,
                         run_user=__user,
                         run_group=__group,
                         description=__description,
                         addition_service_setting={'LimitNOFILE': 40960},
                         )
    systemd.restart(systemd_name)
    systemd.status(systemd_name)

@roles('realserver1')
def task():
    pack()
    clean_app
    put_task()
    imgtask_run()

def test():
    execute(task)

########################################
# @task
@roles('realserver1')
def imgtask_up_bin(force_update=True):
    """
    更新二进制文件
    """
    version = utils.get_host_setting('imgfit_version', __version)
    if not force_update:
        with quiet():
            print __bin
            v = run(__bin + " version")
            if v.succeeded and version in v:
                return

    utils.ensure_user(__user, True)
    run('mkdir -p ' + __install_path)
    run('mkdir -p ' + __upload)
    run('chown  %s:%s  %s/* -R '%(__user, __group, __home_path))
    package_file = __package % version

    with cd(__install_path):
        pack()
        clean_app()
        put_task()
        utils.put_file(__package_loc+package_file, package_file)
        run('tar xvf %s ' % package_file)
        run('rm -f ' + package_file)
        run('chmod +x ' + __bin)

# @task
@roles('realserver1')
def imgtask_worker_up():
    """
    启动imgtask
    """
    imgtask_up_bin(False)
    # conf = dict(
    #     AccessKey=utils.get_host_setting('imgfit_s3_accesskey', 'YHGIZY2NY26FAE3DXOM8'),
    #     SecretKey=utils.get_host_setting('imgfit_s3_secretkey', 'FPVPcBLQXRFGB4hfQaNFiZaV2AYSSlUdxJLRKSrU'),
    #     Name=utils.get_host_setting('imgfit_s3_region', 'OVH-BHS'),
    #     Host=utils.get_host_setting('imgfit_s3_host', 'http://127.0.0.1:7480'),
    #     Listen=utils.get_host_setting('imgfit_listen','0.0.0.0:8000'),
    #     BucketAllow=utils.get_host_setting('imgfit_BucketAllow', ["image", "upload"]),
    #     )
    # conf_path = __install_path + "/config.json"
    # utils.put_mem_buf(json.dumps(conf), conf_path)
    systemd_name = __app + "_worker"
    cmd = [__bin, ' worker']

    systemd.setup_simple(systemd_name,
                         app_run_cmd=' '.join(cmd),
                         work_path=__install_path,
                         run_user=__user,
                         run_group=__group,
                         description=__description,
                         addition_service_setting={'LimitNOFILE': 40960},
                         )
    systemd.restart(systemd_name)
    systemd.status(systemd_name)

@roles('realserver1')
def imgtask_serve_up():
    """
    启动imgtask
    """
    imgtask_up_bin(False)
    # conf = dict(
    #     AccessKey=utils.get_host_setting('imgfit_s3_accesskey', 'YHGIZY2NY26FAE3DXOM8'),
    #     SecretKey=utils.get_host_setting('imgfit_s3_secretkey', 'FPVPcBLQXRFGB4hfQaNFiZaV2AYSSlUdxJLRKSrU'),
    #     Name=utils.get_host_setting('imgfit_s3_region', 'OVH-BHS'),
    #     Host=utils.get_host_setting('imgfit_s3_host', 'http://127.0.0.1:7480'),
    #     Listen=utils.get_host_setting('imgfit_listen','0.0.0.0:8000'),
    #     BucketAllow=utils.get_host_setting('imgfit_BucketAllow', ["image", "upload"]),
    #     )
    # conf_path = __install_path + "/config.json"
    # utils.put_mem_buf(json.dumps(conf), conf_path)
    systemd_name = __app + "_serve"
    cmd = [__bin, ' serve']

    systemd.setup_simple(systemd_name,
                         app_run_cmd=' '.join(cmd),
                         work_path=__install_path,
                         run_user=__user,
                         run_group=__group,
                         description=__description,
                         addition_service_setting={'LimitNOFILE': 40960},
                         )
    systemd.restart(systemd_name)
    systemd.status(systemd_name)
```
    
## 部署方法
    fab -f fab_imgtask_real.py imgtask_worker_up
    
    -f: 指定运行的文件
    imgtask_worker_up: 执行程序的入口
    
运行效果:
```concept
base2 git:(master) ✗ fab -f fab_imgtask_real.py imgtask_worker_up
[root@192.168.9.3:22] Executing task 'imgtask_worker_up'
/home/imgtask/imgtask/imgtask
[root@192.168.9.3:22] run: mkdir -p /home/imgtask/imgtask
[root@192.168.9.3:22] run: mkdir -p /home/imgtask/upload
[root@192.168.9.3:22] run: chown  imgtask:imgtask  /home/imgtask/* -R 
[localhost] local: test -f /Users/apple/go-dev/src/imgtask/Makefile
[localhost] local: make clean
go clean -i  ./
rm -f imgtask
rm -rf linux
[localhost] local: make docker
docker run --rm -v "`pwd`":/go/src/imgtask -w /go/src/imgtask golang:latest bash -c "make build && make package"
mkdir -p build/`go env GOHOSTOS`-`go env GOHOSTARCH`
go build -ldflags "-X main.AppVersion=`git describe --tags` -X main.BuildTime=`date '+%Y-%m-%d_%H:%M:%S'`"  -o build/`go env GOHOSTOS`-`go env GOHOSTARCH`/imgtask ./
cd build/`go env GOHOSTOS`-`go env GOHOSTARCH`/ &&  tar zcvf imgtask-`go env GOHOSTOS`-`go env GOHOSTARCH`-`git describe --tags`.tar.gz imgtask
imgtask
[localhost] local: cp /Users/apple/go-dev/src/imgtask/build/linux-amd64/imgtask-linux-amd64-v1.1.tar.gz /Users/apple/github/fabric_test/base2/package
[root@192.168.9.3:22] run: pwd
[root@192.168.9.3:22] out: /root/go-dev/src/imgtask
[root@192.168.9.3:22] out: 
[root@192.168.9.3:22] run: rm -rf imgtask
[root@192.168.9.3:22] run: ls -l 
[root@192.168.9.3:22] out: total 12
[root@192.168.9.3:22] out: drwxr-xr-x. 2 root root 4096 Feb  6 03:45 conf
[root@192.168.9.3:22] out: drwxr-xr-x. 2 root root 4096 Feb  6 03:45 configs
[root@192.168.9.3:22] out: drwxr-xr-x. 2 root root 4096 Feb  6 03:18 tmp
[root@192.168.9.3:22] out: 
('/root/go-dev/src/imgtask/imgtask', '/Users/apple/go-dev/src/imgtask/build/linux-amd64/imgtask')
[root@192.168.9.3:22] run: pwd
[root@192.168.9.3:22] out: /root/go-dev/src/imgtask
[root@192.168.9.3:22] out: 
[root@192.168.9.3:22] run: ls -l
[root@192.168.9.3:22] out: total 12
[root@192.168.9.3:22] out: drwxr-xr-x. 2 root root 4096 Feb  6 03:45 conf
[root@192.168.9.3:22] out: drwxr-xr-x. 2 root root 4096 Feb  6 03:45 configs
[root@192.168.9.3:22] out: drwxr-xr-x. 2 root root 4096 Feb  6 03:18 tmp
[root@192.168.9.3:22] out: 
[root@192.168.9.3:22] put: /Users/apple/go-dev/src/imgtask/build/linux-amd64/imgtask -> /root/go-dev/src/imgtask/imgtask
[root@192.168.9.3:22] put: package/imgtask-linux-amd64-v1.1.tar.gz -> /home/imgtask/imgtask/imgtask-linux-amd64-v1.1.tar.gz
[root@192.168.9.3:22] run: tar xvf imgtask-linux-amd64-v1.1.tar.gz 
[root@192.168.9.3:22] out: imgtask
[root@192.168.9.3:22] out: 
[root@192.168.9.3:22] run: rm -f imgtask-linux-amd64-v1.1.tar.gz
[root@192.168.9.3:22] run: chmod +x /home/imgtask/imgtask/imgtask
[Sending]: /etc/systemd/system/imgtask_worker.service
[root@192.168.9.3:22] run: chmod 644 /etc/systemd/system/imgtask_worker.service
[root@192.168.9.3:22] run: systemctl daemon-reload
[root@192.168.9.3:22] run: systemctl enable imgtask_worker.service
[root@192.168.9.3:22] run: systemctl restart imgtask_worker.service
[root@192.168.9.3:22] run: systemctl status imgtask_worker.service
[root@192.168.9.3:22] out: ● imgtask_worker.service - Imgfit, APKPure custom imgfit service
[root@192.168.9.3:22] out:    Loaded: loaded (/etc/systemd/system/imgtask_worker.service; enabled; vendor preset: disabled)
[root@192.168.9.3:22] out:    Active: active (running) since Mon 2017-02-06 15:45:49 EST; 92ms ago
[root@192.168.9.3:22] out:  Main PID: 7754 (imgtask)
[root@192.168.9.3:22] out:    CGroup: /system.slice/imgtask_worker.service
[root@192.168.9.3:22] out:            └─7754 /home/imgtask/imgtask/imgtask worker
[root@192.168.9.3:22] out: 
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] ReportAddr: 
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] SSDBHost: 
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] DlServAddr: 
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] S3Host: http://192.168.0.18:7380
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] S3AccessKey: UH0YAIEY9O703LJNG97E
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] S3SecretKey: 9oTBmFUGbaXQmAf2OPM8vtN2IzPeXHFfGDRNn4uK
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] S3ImageAccessKey: 
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [configs.go:111] [*] S3ImageSecretKey: 
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [worker.go:50] dlserv(dev) worker start.
[root@192.168.9.3:22] out: Feb 06 15:45:49 c3 imgtask[7754]: 2017/02/06 15:45:49 [I] [ippoll.go:17] iplist:[https://p.xgj.me:27035]
[root@192.168.9.3:22] out: 
Done.
➜  base2 git:(master) ✗ 

```
    
    



## 查看运行状态和log
1.systemctl status imgtask_worker.service
运行效果:
```bash
    [root@c3 imgtask]# systemctl status imgtask_worker.service
    ● imgtask_worker.service - Imgfit, APKPure custom imgfit service
       Loaded: loaded (/etc/systemd/system/imgtask_worker.service; enabled; vendor preset: disabled)
       Active: active (running) since 一 2017-02-06 15:45:49 EST; 14min ago
     Main PID: 7754 (imgtask)
       CGroup: /system.slice/imgtask_worker.service
               └─7754 /home/imgtask/imgtask/imgtask worker
    
    2月 06 15:59:10 c3 imgtask[7754]: 2017/02/06 15:59:10 [D] [worker_common.go:86] Processing dlimg task, id: 77
    2月 06 15:59:20 c3 imgtask[7754]: 2017/02/06 15:59:20 [E] [worker_common_dl_img.go:75] result:{"package":"com.tencent.mobileqqi","context":"","images":{"icon":null,"screenshort":null,"banner":null,"tube":null}}  ...err:403 Forbidden
    2月 06 15:59:20 c3 imgtask[7754]: 2017/02/06 15:59:20 [D] [worker_common.go:88] dlimg task done, id: 77
    2月 06 15:59:20 c3 imgtask[7754]: 2017/02/06 15:59:20 [D] [worker_common.go:86] Processing dlimg task, id: 77
    2月 06 15:59:31 c3 imgtask[7754]: 2017/02/06 15:59:31 [E] [worker_common_dl_img.go:75] result:{"package":"com.tencent.mobileqqi","context":"","images":{"icon":null,"screenshort":null,"banner":null,"tube":null}}  ...err:403 Forbidden
    2月 06 15:59:31 c3 imgtask[7754]: 2017/02/06 15:59:31 [D] [worker_common.go:88] dlimg task done, id: 77
    2月 06 15:59:31 c3 imgtask[7754]: 2017/02/06 15:59:31 [D] [worker_common.go:86] Processing dlimg task, id: 77
    2月 06 15:59:44 c3 imgtask[7754]: 2017/02/06 15:59:44 [E] [worker_common_dl_img.go:75] result:{"package":"com.tencent.mobileqqi","context":"","images":{"icon":null,"screenshort":null,"banner":null,"tube":null}}  ...err:403 Forbidden
    2月 06 15:59:44 c3 imgtask[7754]: 2017/02/06 15:59:44 [D] [worker_common.go:88] dlimg task done, id: 77
    2月 06 15:59:44 c3 imgtask[7754]: 2017/02/06 15:59:44 [D] [worker_common.go:86] Processing dlimg task, id: 77
    Hint: Some lines were ellipsized, use -l to show in full.
    [root@c3 imgtask]# 
```
    
2.journalctl -u imgtask_worker  -f
    (journalctl 配合 systemd 查看log)
```concept
[root@c3 imgtask]# journalctl -u imgtask_worker  -f
-- Logs begin at 一 2017-02-06 01:54:38 EST. --
2月 06 16:01:45 c3 imgtask[7754]: 2017/02/06 16:01:45 [D] [worker_common.go:86] Processing dlimg task, id: 77
2月 06 16:01:49 c3 imgtask[7754]: 2017/02/06 16:01:49 [E] [worker_common_dl_img.go:75] result:{"package":"com.tencent.mobileqqi","context":"","images":{"icon":null,"screenshort":null,"banner":null,"tube":null}}  err:dlImgUrlBase(uploadImg) err:err:uploadImg(w.s3fs.PutFile2)  err:PutFile2(b.PutReader)  err:403 Forbidden  r:0xc4203fa6c0  bucket:image filetype:image/png key:com.tencent.mobileqqi_0_70857c01 size:650772    err1:403 Forbidden  url:https://image.winudf.com/v1/image/YWRtaW5fbmE2dTlteXI/=200.jpg  fid:image_com.tencent.mobileqqi_0_70857c01
2月 06 16:01:49 c3 imgtask[7754]: 2017/02/06 16:01:49 [D] [worker_common.go:88] dlimg task done, id: 77
2月 06 16:01:49 c3 imgtask[7754]: 2017/02/06 16:01:49 [D] [worker_common.go:86] Processing dlimg task, id: 77
2月 06 16:01:53 c3 imgtask[7754]: 2017/02/06 16:01:53 [E] [worker_common_dl_img.go:75] result:{"package":"com.tencent.mobileqqi","context":"","images":{"icon":null,"screenshort":null,"banner":null,"tube":null}}  err:dlImgUrlBase(uploadImg) err:err:uploadImg(w.s3fs.PutFile2)  err:PutFile2(b.PutReader)  err:403 Forbidden  r:0xc4203ca6f0  bucket:image filetype:image/png key:com.tencent.mobileqqi_0_1b51a91a size:650772    err1:403 Forbidden  url:https://image.winudf.com/v1/image/YWRtaW5fbmE2dTlteXI/=200.jpg  fid:image_com.tencent.mobileqqi_0_1b51a91a
```
    
##  bug 处理: 
    serve 运行过程中报错
    修改运行模式dev->prov
```go
[root@c3 imgtask]# ./imgtask serve
dir: /home/imgtask/imgtask
2017/02/06 16:22:55 [I] [root.go:51] Started. log level debug
2017/02/06 16:22:55 [I] [configs.go:111] [*] TmpPath: tmp
2017/02/06 16:22:55 [I] [configs.go:111] [*] WorkCount: 1
2017/02/06 16:22:55 [I] [configs.go:111] [*] LogFile: 
2017/02/06 16:22:55 [I] [configs.go:111] [*] LogToStd: true
2017/02/06 16:22:55 [I] [configs.go:111] [*] LogLevel: debug
2017/02/06 16:22:55 [I] [configs.go:111] [*] ReportAddr: 
2017/02/06 16:22:55 [I] [configs.go:111] [*] SSDBHost: 
2017/02/06 16:22:55 [I] [configs.go:111] [*] DlServAddr: 
2017/02/06 16:22:55 [I] [configs.go:111] [*] S3Host: http://192.168.0.18:7380
2017/02/06 16:22:55 [I] [configs.go:111] [*] S3AccessKey: UH0YAIEY9O703LJNG97E
2017/02/06 16:22:55 [I] [configs.go:111] [*] S3SecretKey: 9oTBmFUGbaXQmAf2OPM8vtN2IzPeXHFfGDRNn4uK
2017/02/06 16:22:55 [I] [configs.go:111] [*] S3ImageAccessKey: 
2017/02/06 16:22:55 [I] [configs.go:111] [*] S3ImageSecretKey: 
2017/02/06 16:22:55 [I] [serve.go:44] dlserv(dev) start.
panic: you are in dev mode. So please set gopath

goroutine 1 [running]:
panic(0x9adda0, 0xc42000f7e0)
	/usr/local/go/src/runtime/panic.go:500 +0x1a1
imgtask/vendor/github.com/astaxie/beego.(*ControllerRegister).Include(0xc4201ac160, 0xc42000f7b0, 0x1, 0x1)
	/go/src/imgtask/vendor/github.com/astaxie/beego/router.go:217 +0x884
imgtask/vendor/github.com/astaxie/beego.(*Namespace).Include(0xc42000d8a0, 0xc42000f7b0, 0x1, 0x1, 0xc42000d8a0)
	/go/src/imgtask/vendor/github.com/astaxie/beego/namespace.go:186 +0x4d
imgtask/vendor/github.com/astaxie/beego.NSInclude.func1(0xc42000d8a0)
	/go/src/imgtask/vendor/github.com/astaxie/beego/namespace.go:303 +0x4c
imgtask/vendor/github.com/astaxie/beego.NewNamespace(0xa7637d, 0x5, 0xc420022170, 0x1, 0x1, 0xc420015001)
	/go/src/imgtask/vendor/github.com/astaxie/beego/namespace.go:42 +0xa9
imgtask/vendor/github.com/astaxie/beego.NSNamespace.func1(0xc42000d880)
	/go/src/imgtask/vendor/github.com/astaxie/beego/namespace.go:387 +0x58
imgtask/vendor/github.com/astaxie/beego.NewNamespace(0xa74bef, 0x3, 0xc4201bfbd8, 0x3, 0x3, 0xc420014fc0)
	/go/src/imgtask/vendor/github.com/astaxie/beego/namespace.go:42 +0xa9
imgtask/routers.InitApiRouter()
	/go/src/imgtask/routers/router.go:38 +0x3d2
imgtask/cmd.serve()
	/go/src/imgtask/cmd/serve.go:51 +0x115
imgtask/cmd.glob..func1(0xf3cfe0, 0xf85a60, 0x0, 0x0)
	/go/src/imgtask/cmd/serve.go:20 +0x14
imgtask/vendor/github.com/spf13/cobra.(*Command).execute(0xf3cfe0, 0xf85a60, 0x0, 0x0, 0xf3cfe0, 0xf85a60)
	/go/src/imgtask/vendor/github.com/spf13/cobra/command.go:636 +0x443
imgtask/vendor/github.com/spf13/cobra.(*Command).ExecuteC(0xf3cdc0, 0x1, 0x15, 0x15)
	/go/src/imgtask/vendor/github.com/spf13/cobra/command.go:722 +0x367
imgtask/vendor/github.com/spf13/cobra.(*Command).Execute(0xf3cdc0, 0x416409, 0xf85968)
	/go/src/imgtask/vendor/github.com/spf13/cobra/command.go:681 +0x2b
imgtask/cmd.Execute()
	/go/src/imgtask/cmd/root.go:29 +0x31
main.main()
	/go/src/imgtask/main.go:11 +0x7f
[root@c3 imgtask]# 
```
## bug2
    beego 部署发现post无法接受数据
    原因是部署时，没有建立conf/app.conf 文件, copyrequestbody 不是true导致post无法接受数据
```go
appname = simpletask
httpport = 8080
runmode = prod
autorender = false
copyrequestbody = true
EnableDocs = true
```


## worker
1.worker 重启状态设置
```go
	models.ResetRunningCommonTaskById(id, types)
	time.Sleep(10*time.Second)          #通过这个延时，可以进行测试，查看状态是否可以更新
```

```sqlite-sql
postgres=# select id, work_id, status, result, err from task_common where id  >= 231;
 id  |   work_id    | status  | result | err 
-----+--------------+---------+--------+-----
 240 | hyhMac.local | RUNNING | {}     | 
(1 row)

postgres=#  当worker 中止重新启动时，会设置RUNNING->QUEUE
postgres=# 
postgres=# select id, work_id, status, result, err from task_common where id  >= 231;
 id  |   work_id    | status | result | err 
-----+--------------+--------+--------+-----
 240 | hyhMac.local | QUEUE  | {}     | 
```


