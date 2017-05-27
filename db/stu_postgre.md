#### step1: pg dockerfile
[介绍](https://hub.docker.com/_/postgres/)
```bash
➜  ~ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
7889b84d92992547af52af72371f773254ef3e406f53553df0ae758665640c57
```

#### step2: 连接pg
```bash
➜  ~ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
7889b84d9299        postgres            "docker-entrypoint..."   5 seconds ago       Up 4 seconds        5432/tcp                   some-postgres
22771bdd010c        mongo:3.2           "docker-entrypoint..."   2 weeks ago         Up About an hour    0.0.0.0:27017->27017/tcp   mongod
➜  ~ docker run -it --rm --link some-postgres:postgres postgres psql -h postgres -U postgres
Password for user postgres:
psql: FATAL:  password authentication failed for user "postgres"
➜  ~ docker run -it --rm --link some-postgres:postgres postgres psql -h postgres -U postgres
Password for user postgres:
psql (9.6.2)
Type "help" for help.

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
```
#### step3: phppgadmin
```bash
docker run -d -p 12345:80 --link some-postgres:postgres-db -e "DB_HOST=postgres-db" -e "DB_PORT=5432" --name=postg zhajor/docker-phppgadmin
```

#### step4:切换数据库
```bash
postgres=# \c youtube
You are now connected to database "youtube" as user "postgres".
youtube=# \d
        List of relations
 Schema | Name | Type  |  Owner
--------+------+-------+----------
 public | test | table | postgres
(1 row)
youtube=#
```
