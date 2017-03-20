##abuse-robot

170214 abuse-robot
--------------

此服务用户自动扫描相关邮箱，根据相关规则对于下架请求的邮件进行自动下架操作

# 执行流程

1. 定时扫描指定邮箱
2. 根据规则过滤邮件，过滤出下架请求的邮件
3. 请求相关 API，进行下架操作


# 过滤条件
优先级从上到下

1. 抄送人或收件人包含主机或域名服务商
2. 能解析出我们的 url 地址
3. 排除个人邮箱，outlook.com ,gmail.com, yahoo.com等

# 资源zhangxin: Zhang Xin wrote:
    (1)This URL is infringing upon our clients copyright and trademark content.
    URL: https://apkpure.com/south-indian-bank-2fa/otl.snkl.SnorkelOTP
    
    (2)Infringing Application Name: App for All Taxi Cabs India APK
    Developer Name: Cabsguru
    Application Store Link: hxxps://apkpure[dot]com/app-for-all-taxi-cabs-india/com.cabsguru
    目前就这两种比较常见

# imaplib 

	理解imaplib 协议
	1.https://docs.python.org/2/library/imaplib.html#
	2.http://james.apache.org/server/rfclist/imap4/rfc2060.txt
	3.http://blog.csdn.net/qqnnhhbb/article/details/6428681	

        '''
        # 1.获取当前时间戳,
        now = datetime.datetime.now()
        nowBefor2 = now - datetime.timedelta(days=2)
        wantDay = nowBefor2.strftime("%d-%m-%Y")
        wantDay = wantDay.split("-")
        wantDay[1] = MyDateMonDict[wantDay[1]]
        # typ, data = rml.mail.search(None, "SINCE", "24-Feb-2017")
        typ, data = self.mail.search(None, "SINCE", "{}-{}-{}".format(*wantDay))
        if typ != 'OK':
            return

        # mailIdList 依赖的是邮件顺序id不同与uid
        mailIdList = data[0].split()[-1]
        if not mailIdList:
            return


'''
SENTBEFORE <date>
[RFC-2822]Date: header（忽视时间和时区）早于指定日期的邮件。
SENTON <date>
[RFC-2822]Date: header （忽视时间和时区）在指定日期的邮件。
SENTSINCE <date>
[RFC-2822]Date: header （忽视时间和时区）在指定日期或者晚于指定日期的邮件。
SINCE <date>
实际日期（忽视时间和时区）在指定日期或者晚于指定日期的邮件。
'''
'''
dockerfile
  1 FROM python:2.7.13-slim
  2 RUN apt-get -y update \                                                                                                                                                                                                                 
  3     && apt-get -y install supervisor \
  4     && mkdir -p /var/log/supervisor
  5 
  6 WORKDIR /abuse-robot
  7 #ADD requirements.txt /abuse-robot/requirements.txt
  8 #RUN pip install -r requirements.txt 
  9 #ADD redis.conf /etc/redis/redis.conf
 10 ADD . /abuse-robot
 11 CMD /usr/bin/supervisord -n -c supervisord.conf
'''
~                                                                                                                                                                                                                                           
~                                                                                                                                                                                                                                           
~                                                                                                                                                                                                                                           
~                                                                     