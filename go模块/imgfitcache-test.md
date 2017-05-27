#### imgfit-cache 服务器测试

```bash
[root@fs12t01 ~]# time wget localhost:9000/v2/image/Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk
--2017-05-25 02:04:31--  http://localhost:9000/v2/image/Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk
正在解析主机 localhost (localhost)... 127.0.0.1
正在连接 localhost (localhost)|127.0.0.1|:9000... 已连接。
已发出 HTTP 请求，正在等待回应... 200 OK
长度：未指定 [image/png]
正在保存至: “Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk”

    [ <=>                                                                                                                                                                                                 ] 338,739     --.-K/s 用时 0.002s

2017-05-25 02:04:34 (143 MB/s) - “Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk” 已保存 [338739]


real	0m2.773s
user	0m0.008s
sys	0m0.012s
[root@fs12t01 ~]# time wget localhost:9000/v2/image/Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk
--2017-05-25 02:04:42--  http://localhost:9000/v2/image/Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk
正在解析主机 localhost (localhost)... 127.0.0.1
正在连接 localhost (localhost)|127.0.0.1|:9000... 已连接。
已发出 HTTP 请求，正在等待回应... 200 OK
长度：未指定 [image/png]
正在保存至: “Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk.1”

    [ <=>                                                                                                                                                                                                 ] 338,739     --.-K/s 用时 0.003s

2017-05-25 02:04:42 (127 MB/s) - “Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk.1” 已保存 [338739]


real	0m0.028s
user	0m0.012s
sys	0m0.008s
[root@fs12t01 ~]# time wget localhost:9000/v2/image/Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk
--2017-05-25 02:06:17--  http://localhost:9000/v2/image/Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk
正在解析主机 localhost (localhost)... 127.0.0.1
正在连接 localhost (localhost)|127.0.0.1|:9000... 已连接。
已发出 HTTP 请求，正在等待回应... 200 OK
长度：未指定 [image/png]
正在保存至: “Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk.2”

    [ <=>                                                                                                                                                                                                 ] 338,739     --.-K/s 用时 0.003s

2017-05-25 02:06:17 (122 MB/s) - “Y29tLm1hamVkYWxyYXNsYW5pLm1hamlkLnJhc2xhbmlfc2NyZWVuXzRfZ21xaHM3MTk.2” 已保存 [338739]


real	0m0.306s
user	0m0.008s
sys	0m0.012s
[root@fs12t01 ~]#
```
