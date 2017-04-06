##minicdn 使用


## 1.ser.  manager
```
➜  minicdn git:(hyh) ✗ ./minicdn -mirror http://localhost:5000 -addr :11000 -log cdn.log
Init Master View:/_ws/ -> WSHandler
View: /  -> FileHandler
2017/03/20 21:23:08 Listening on :11000
```
## 2. slav

➜  minicdn git:(hyh) ✗ ./minicdn -upstream ws://localhost:11000 -addr :8002
2017/03/20 21:52:48 InitSlave
2017/03/20 21:52:48 InitSlave u.Path:/_ws/ conn:&{{0xc4200580e0}}
2017/03/20 21:52:48 Self name: http://::1:8002
2017/03/20 21:52:48 Peer list: [http://::1:8003 http://::1:8001 http://::1:8002]
2017/03/20 21:52:48 Mirror site: http://localhost:5000
Init Master View:/_ws/ -> WSHandler
View: /  -> FileHandler
2017/03/20 21:52:48 Listening on :8002
FileHandler  url:/cdn.log
KEY: /cdn.log
FileHandler  url:/favicon.ico
KEY: /favicon.ico


## 2. slav

➜  minicdn git:(hyh) ✗ ./minicdn -upstream ws://localhost:11000 -addr :8001
2017/03/20 21:52:48 InitSlave
2017/03/20 21:52:48 InitSlave u.Path:/_ws/ conn:&{{0xc4200580e0}}
2017/03/20 21:52:48 Self name: http://::1:8002
2017/03/20 21:52:48 Peer list: [http://::1:8003 http://::1:8001 http://::1:8002]
2017/03/20 21:52:48 Mirror site: http://localhost:5000
Init Master View:/_ws/ -> WSHandler
View: /  -> FileHandler
2017/03/20 21:52:48 Listening on :8002
FileHandler  url:/cdn.log
KEY: /cdn.log
FileHandler  url:/favicon.ico
KEY: /favicon.ico
