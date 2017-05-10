docker run  --name abuse-robot -v /home/abuse-robot/conf:/app/conf   -v /home/abuse-robot/MailMange.py:/app/MailMange.py  registry.pureapk.com/apkpure/abuse-robot:latest

docker run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name abuse-robot -v /home/abuse-robot/conf:/app/conf   -v /home/abuse-robot/MailMange.py:/app/MailMange.py  registry.pureapk.com/apkpure/abuse-robot:latest

docker run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name abuse-robot -v `pwd`/conf:/app/conf   maillocal




CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %               NET I/O             BLOCK I/O           PIDS
857164dbcf29        0.00%               28.77 MiB / 1.952 GiB   1.44%               8.83 MB / 280 kB    1.66 MB / 0 B       2
93bedea73a88        0.00%               12.58 MiB / 1.952 GiB   0.63%               5.79 kB / 1.58 kB   10.9 MB / 0 B       6


## 程序处于休眠状态
[root@fs12t01 ~]# ps -aux | grep 19575 
root      5875  0.0  0.0 112672  2196 pts/0    S+   07:30   0:00 grep --color=auto 19575
root     19575  0.0  0.0 212764 14060 ?        S    02:19   0:09 python MailMange.py



## 程序死于time.sleep

	17.3.19 pycharm 中运行超过12小时正常。可以被调度到
	nohup / docker 12h 后无法被正常调度


docker run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name abuse-robot -v /home/abuse-robot/conf:/app/conf  maillocal