## 整理docker 之痛


##0x01 时区
    https://tommy.net.cn/2015/02/05/config-timezone-in-docker/
```
首先通过下面的命令进入对应的 container:
1# docker exec -ti container bash
然后在 container 里面执行如下的命令：
1# echo "Asia/Shanghai" > /etc/timezone
2# dpkg-reconfigure -f noninteractive tzdata
1RUN echo "Asia/Shanghai" > /etc/timezone
2RUN dpkg-reconfigure -f noninteractive tzdata
```


##0x02 docker pull  
    "Repository ubuntu already being pulled by another client. Waiting."
    处理方法:
    service docker restart

##0x03
