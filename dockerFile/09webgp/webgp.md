##### webgp run

#####  1.简介
		主功能：
			webgp: 爬虫	
			color: 获取图像色彩值
			imgtask: 任务模块，批量获取颜色信息

##### 2.依赖
		imgtask: ser/work 以来于postgresql
###### 2.1 postgre
```bash
step1: 启动ser
➜  webgp git:(master) ✗ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
5a79dd1b21024310d4f7bab9ff70da6b4b140f151783a72232eb8ca6b9e5151e

step2: 连接容器进行测试
➜  ~ docker run -it --rm --link some-postgres:postgres postgres psql -h postgres -U postgres
Password for user postgres:
psql (9.6.2)
Type "help" for help.

postgres=# \d
No relations found.
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

postgres=#


step3: 导出数据

```

####### 2.2 启动webgp
```bash
docker run --log-opt max-size=10m --log-opt max-file=3  -it --name webgp --link some-postgres:postgres  -v `pwd`/conf:/webgp/conf  webgp bash
docker run --log-opt max-size=10m --log-opt max-file=3  -it --name webgp -v `pwd`/conf:/webgp/conf  apk.302e.com:3000/apkpure/webgp:latest bash
```


docker run --log-opt max-size=10m --log-opt max-file=3  -it --name webgp --link some-postgres:postgres  -v `pwd`/conf:/webgp/conf -v `pwd`/swagger:/webgp/swagger -p 8080:8080 --network=host --ip "192.168.9.41"  webgp bash


docker run --log-opt max-size=10m --log-opt max-file=3  -it --name webgp --link some-postgres:postgres  -v `pwd`/conf:/webgp/conf -v `pwd`/swagger:/webgp/swagger -p 8080:8080 webgp bash