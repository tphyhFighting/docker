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