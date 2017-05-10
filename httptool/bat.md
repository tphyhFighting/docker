#### bat --> beego

```bash
➜  ~ bat localhost:9000/health
GET /health HTTP/1.1
Host: localhost:9000
Accept: application/json
Accept-Encoding: gzip, deflate
User-Agent: bat/0.1.0


HTTP/1.1 200 OK
Date : Wed, 10 May 2017 07:03:59 GMT
Content-Length : 0
Content-Type : text/plain; charset=utf-8

➜  ~ curl -I localhost:9000/health
HTTP/1.1 200 OK
Date: Wed, 10 May 2017 07:04:34 GMT
Content-Type: text/plain; charset=utf-8
➜  ~

➜  ~ curl -I -X GET localhost:9000/health
HTTP/1.1 200 OK
Date: Wed, 10 May 2017 07:04:34 GMT
Content-Type: text/plain; charset=utf-8
```
