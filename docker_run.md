##run

docker run -it -v `pwd`/upload:/upload jujhars13/docker-imagemagick:latest bash
docker run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name abuse-robot -v /home/abuse-robot/conf:/app/conf  maillocal
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit-c -d  --restart always -p 9000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  iimgfitcache 

#####mongod
	docker  run --log-opt max-size=10m --log-opt max-file=3  --restart always -d --name mongod -p 27017:27017  mongo:3.2


##smart-backup
docker run -it --log-opt max-size=10m --log-opt max-file=3 --name smart-backup -v `pwd`/conf:/app/conf -v `pwd`/tmp:/app/tmp  smart_backup bash 
/app/app cron --config conf/crons3v2.json
/app/app cron --config conf/mongdb_dump.json
/app/app run  --config conf/mongdb_dump.json
/app/app run --config conf/pg_dump.json --jobname job_cmd_pg2
/app/app run --config conf/mongdb_dump.json --jobname job_cmd_mongo
/app/app run --config conf/mongdb_dump.json --jobname job_cmd_mongo

docker run -it --log-opt max-size=10m --log-opt max-file=3 --name smart-backup -v `pwd`/conf:/app/conf -v `pwd`/tmp:/app/tmp  smart_backup bash
docker run -it --log-opt max-size=10m --log-opt max-file=3 --name smart-backup-mongo -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:mongo_32_1-  bash
docker run -it --log-opt max-size=10m --log-opt max-file=3 --name smart-backup-pg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_1-  bash

docker run -it --log-opt max-size=10m --log-opt max-file=3 --name smart-backup-mongo -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:mongo_32_master  bash
docker run -it --log-opt max-size=10m --log-opt max-file=3 --name smart-backup-pg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_master sh 
-c "/app/app run --config conf/pg_dump.json --jobname job_cmd_pg2 "
##rm 
docker rm -f smart-backup-mongo
docker rm -f smart-backup-pg


##pull 
docker pull apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_master
docker pull apk.302e.com:3000/apkpure/ops/smart-backup:mongo_32_master

export PGPASSWORD=postgres
export PGUSER=postgres

psql -U testuser -h 172.28.18.51 testdb

##env
2017/04/10 10:29:48 [I] [jobs.go:65] ## ENV:[env1 env2]...os:[HOSTNAME=d64497cf9374 MONGO_VERSION=3.2.12 TERM=xterm MONGO_PACKAGE=mongodb-org PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin GPG_KEYS=DFFA3DCF326E302C4787673A01C4E7FAAAB2461C 	42F3E95A2C4F08279C4960ADD68FA50FEA312927 PWD=/app HOME=/root SHLVL=1 MONGO_MAJOR=3.2 no_proxy=127.0.0.1, localhost GOSU_VERSION=1.7 _=/app/app]


##部署
docker run --log-opt max-size=10m --log-opt max-file=3  --name smart-backup-pg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_email sh -c "/app/app run --config conf/pg_dump.json --jobname job_cmd_pg2"

docker run --log-opt max-size=10m --log-opt max-file=3  --name smart-backup-pg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_email sh -c "/app/app cron --config conf/pg_dump.json "

docker run --log-opt max-size=10m --log-opt max-file=3 --restart always -d --name smart-backup-pg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_master sh -c "/app/app cron --config conf/pg_dump.json "

docker run --log-opt max-size=10m --log-opt max-file=3 --restart always -d --name smart-backup-mongo -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:mongo_32_master sh -c "/app/app cron --config conf/mongdb_dump.json "

#email
docker run --log-opt max-size=10m --log-opt max-file=3 --restart always -d --name smart-backup-mongo -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:mongo_32_email sh -c "/app/app cron --config conf/mongdb_dump.json "

docker run --log-opt max-size=10m --log-opt max-file=3 --restart always -d --name smart-backup-pg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:pg_96_email sh -c "/app/app cron --config conf/pg_dump.json "

docker run --log-opt max-size=10m --log-opt max-file=3 -it --name smart-backup-mg -v `pwd`/conf:/app/conf    apk.302e.com:3000/apkpure/ops/smart-backup:mongo_32_email sh 
##log
docker logs -f smart-backup-mongo
docker logs -f smart-backup-pg

##debug
docker exec -it smart-backup-pg  bash
docker exec -it smart-backup-mongo bash

123.207.174.233

