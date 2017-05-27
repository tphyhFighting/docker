#### django docker


#### dockerfile
```bash
FROM python:3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

#工作路径
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

```

#### test
```bash
➜  11dj git:(go) ✗ docker run -it -v `pwd`:/usr/src/app  dj-local sh
# pwd
/usr/src/app
# ls -al
total 16
-rw-r--r-- 1 root root  316 May 27 09:41 Dockerfile.env
-rw-r--r-- 1 root root   12 May 27 09:51 main.py
-rw-r--r-- 1 root root  104 May 27 09:41 require.txt
#
```

#### 创建项目
```bash
➜  11dj git:(go) django-admin.py startproject HelloWorld
➜  11dj git:(go) ✗ ll
total 32
drwxr-xr-x   7 apple  staff  238  5 27 17:56 .
drwxr-xr-x  23 apple  staff  782  5 27 17:40 ..
-rw-r--r--   1 apple  staff  316  5 27 17:41 Dockerfile.env
drwxr-xr-x   4 apple  staff  136  5 27 17:56 HelloWorld
-rw-r--r--   1 apple  staff  691  5 27 17:55 dj.md
-rw-r--r--   1 apple  staff   12  5 27 17:51 main.py
-rw-r--r--   1 apple  staff  104  5 27 17:41 require.txt
➜  11dj git:(go) ✗
➜  11dj git:(go) ✗ cd HelloWorld
➜  HelloWorld git:(go) ✗ pwd
/Users/apple/github/docker/dockerFile/11dj/HelloWorld
➜  HelloWorld git:(go) ✗ ls -al
total 8
drwxr-xr-x  4 apple  staff  136  5 27 17:56 .
drwxr-xr-x  7 apple  staff  238  5 27 17:57 ..
drwxr-xr-x  7 apple  staff  238  5 27 17:58 HelloWorld
-rwxr-xr-x  1 apple  staff  808  5 27 17:56 manage.py
➜  HelloWorld git:(go) ✗ docker run --log-opt max-size=10m --log-opt max-file=3 --name  dj-hello  -it -v `pwd`:/usr/src/app -p 8000:8000 dj-local
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

May 27, 2017 - 10:03:30
Django version 1.11.1, using settings 'HelloWorld.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
[27/May/2017 10:03:50] "GET / HTTP/1.1" 200 1716
Not Found: /favicon.ico
[27/May/2017 10:03:50] "GET /favicon.ico HTTP/1.1" 404 1966
```

#### pg 修正setting.py中数据库为postgresql
```
(dj3.5) ➜  HelloWorld git:(go) ✗ ls
HelloWorld db.sqlite3 manage.py  run.sh
(dj3.5) ➜  HelloWorld git:(go) ✗ python manage.py dbshell
psql (9.6.1)
Type "help" for help.
postgres=# \d you_tube_video_info
                                      Table "public.you_tube_video_info"
       Column       |         Type          |                            Modifiers
--------------------+-----------------------+------------------------------------------------------------------
 id                 | integer               | not null default nextval('you_tube_video_info_id_seq'::regclass)
 video_id           | character varying(11) | not null default ''::character varying
 title              | text                  | not null default ''::text
 length_seconds     | text                  | not null default ''::text
 screen_fid         | text                  | not null default ''::text
 screen_youtube_url | text                  | not null default ''::text
 key_worlds         | text                  | not null default ''::text
 info               | jsonb                 | not null default '{}'::jsonb
 who                | text                  | not null default ''::text
Indexes:
    "you_tube_video_info_pkey" PRIMARY KEY, btree (id)
    "you_tube_video_info_video_id" btree (video_id)

postgres=#
```
