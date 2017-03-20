## supervisor 部署

##0x00 
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
stop <name>		Stop a process
stop <gname>:*		Stop all processes in a group
stop <name> <name>	Stop multiple processes or groups
stop all		Stop all processes
supervisor> stop all
foo: stopped
supervisor> status
foo                              STOPPED   Feb 21 12:08 PM
supervisor> start
Error: start requires a process name
start <name>		Start a process
start <gname>:*		Start all processes in a group
start <name> <name>	Start multiple processes or groups
start all		Start all processes
supervisor> start foo
foo: started
supervisor> status
foo                              RUNNING   pid 18802, uptime 0:00:05
supervisor>
```	

##0x01 部署go
![输入图片说明](https://static.oschina.net/uploads/img/201702/21130703_fyuc.png "在这里输入图片标题")

##0x02 在容器中使用supervisor
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