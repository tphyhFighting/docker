docker run  --name abuse-robot -v /home/abuse-robot/conf:/app/conf   -v /home/abuse-robot/MailMange.py:/app/MailMange.py  registry.pureapk.com/apkpure/abuse-robot:latest

docker run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name abuse-robot -v /home/abuse-robot/conf:/app/conf   -v /home/abuse-robot/MailMange.py:/app/MailMange.py  registry.pureapk.com/apkpure/abuse-robot:latest

docker run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name abuse-robot -v `pwd`/conf:/app/conf   maillocal




CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %               NET I/O             BLOCK I/O           PIDS
857164dbcf29        0.00%               28.77 MiB / 1.952 GiB   1.44%               8.83 MB / 280 kB    1.66 MB / 0 B       2
93bedea73a88        0.00%               12.58 MiB / 1.952 GiB   0.63%               5.79 kB / 1.58 kB   10.9 MB / 0 B       6
