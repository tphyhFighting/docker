log-collect
-----------------

日志收集与转发服务

# 主要功能

* 为客户端提供日志提交接口
* 保存日志到 Postgresql（暂时）
* 可以对接到一些合作统计平台，可以列队提交数据
* 提供日志查看和简单统计接口


# 一些信息

客户端接口的数据使用 protobuf，结构定义见 

[log_request.proto](https://apk.302e.com:3443/apkpure/proto-define/blob/master/protos/log_request.proto)
```concept
syntax = "proto3";
package protos;
option java_package = "com.apkpure.proto";
option java_outer_classname = "LogRequestProtos";
message Log {
	string type = 1;			// 日志类型
	bytes logData = 2;			// 日志数据
	int32 delayTimeMs = 3; 	// 日志延迟发送时间，
								// 此数据为客户端记录数据到最终发送的时间延迟，
								// 用于明确日志记录时间，单位：毫秒
}
message LogRequest {
	repeated Log logs =1;
}
```

# 资源
https://www.ibm.com/developerworks/cn/linux/l-cn-gpb/

# 工作流程
    1.书写 .proto 文件, 定义msg
    2.


############33
1.chrome://inspect/#devices
2.连接手机启动app
3.Devices /inspect

1	2140043940	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item0"}	on0	
2	2140044378	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item1"}	on1	
3	2140044398	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item2"}	on2	
4	2140044416	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item3"}	on3	
5	2140044437	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item4"}	on4	
6	2140044473	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item5"}	on5	
7	2140044502	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item6"}	on6	
8	2140044526	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item7"}	on7	
9	2140044557	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item8"}	on8	
10	2140044577	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item9"}	on9	
11	2140044583	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item10"}	on10	
12	2140044590	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item11"}	on11	
13	2140044611	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item12"}	on12	
14	2140044647	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item13"}	on13	
15	2140044654	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item14"}	on14	
16	2140044673	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item15"}	on15	
17	2140044704	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item16"}	on16	
18	2140044719	{"sysVersion":"6.0","apkVersion":"1.2.3","channelID":"843984932","versionCode":"1","data":"item17"}

-------------------------------------------