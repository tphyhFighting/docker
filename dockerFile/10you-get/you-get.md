#### you-get 下载youtube视频
[you-get](https://github.com/soimort/you-get)

#### 0x00 需求
>评论后台需要支持分享youtube视频功能，需要根据视频id获取视频信息.
<br>
>example:<br>
>view-source:<br>http://www.youtube.com/watch?v=2EuTs1Yo-Bo
><br>
>id:2EuTs1Yo-Bo
>video_info:
><br>
>title:【刺客教條：大革命】- PC特效全開中文劇情電影60FPS - 第七集 - Episode 7 - Assassin's Creed：Unity - 刺客信條 ： 大革命 - 最強無損畫質影片

#### 0x01 you-get 运行流程

- step1: get_video_info
 >https://www.youtube.com/get_video_info?video_id=2EuTs1Yo-Bo
 >title: 【刺客教條：大革命】- PC特效全開中文劇情電影60FPS - 第七集 -  Episode 7 - Assassin's Creed：Unity - 刺客信條 ： 大革命 - 最強無損畫質影片
- step2: get_video_page
>https://www.youtube.com/watch?v=%s
- step3(dep step2 html page): html5player >https://www.youtube.com/yts/jsbin/player-vflxXnk_G/en_US/base.js
>site:                YouTube
>title:               【刺客教條：大革命】- PC特效全開中文劇情電影60FPS - 第七集 - Episode 7 - Assassin's Creed：Unity - 刺客信條 ： 大革命 - 最強無損畫質影片
>url:         http://www.youtube.com/watch?v=2EuTs1Yo-Bo
>stream:
      itag:          22
      container:     mp4
      quality:       hd720
      size:          397.7 MiB (417010490 bytes)
      download-with: you-get --itag=22 [URL]
      download-with: src: --format=['https://r11---sn-a5m7ln7y.googlevideo.com/videoplayback?mv=m&mt=1494903803&ms=au&ei=SWwaWZPgB_LU-APmy4n4Bg&ip=168.235.94.49&pl=27&mn=sn-a5m7ln7y&mm=31&id=o-AOGCwZ7oVBjn5VHHODklZSiCRKRpaxLp_J5KftPCyS0T&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2Fmp4&initcwndbps=12017500&ipbits=0&dur=1903.200&source=youtube&lmt=1471920205727707&requiressl=yes&signature=4F9AA3883B4F832F0E35C32D1E1F5568CAA51282.4E9EAFE14909CF0EE0826613181914C853C574C9&key=yt6&itag=22&expire=1494925481&upn=pQkdHj6mbtI&ratebypass=yes'] [URL]
      download-with: url: --format=https://r11---sn-a5m7ln7y.googlevideo.com/videoplayback?mv=m&mt=1494903803&ms=au&ei=SWwaWZPgB_LU-APmy4n4Bg&ip=168.235.94.49&pl=27&mn=sn-a5m7ln7y&mm=31&id=o-AOGCwZ7oVBjn5VHHODklZSiCRKRpaxLp_J5KftPCyS0T&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&mime=video%2Fmp4&initcwndbps=12017500&ipbits=0&dur=1903.200&source=youtube&lmt=1471920205727707&requiressl=yes&signature=4F9AA3883B4F832F0E35C32D1E1F5568CAA51282.4E9EAFE14909CF0EE0826613181914C853C574C9&key=yt6&itag=22&expire=1494925481&upn=pQkdHj6mbtI&ratebypass=yes [URL]

默认选择质量最高的进行下载。
self.streams_sorted中存放排序后的视频流数据。

##### 0x02 folder get_video_metadat程

>Request URL:
><br>
[get_video_metadata](https://www.youtube.com/get_video_metadata?video_id=NpZOpd1CC5M&html5=1&page_subscribe=0&authuser=0)
>
Request Method: GET
Status Code: 200
Query Url
video_id: NpZOpd1CC5M
html5: 1
page_subscribe: 0
authuser: 0

>resp:
>

#### 0x02 get_video_info
>Request URL:
><br>
[get_video_info](
https://www.youtube.com/get_video_info?html5=1&video_id=2EuTs1Yo-Bo
&cpn=Z8hSrNWndaXepglx&eurl&el=adunit&hl=zh_CN&agcid=183933493088&aqi=1HYaWdajMImM-gOM47HYCw&sts=17295&lact=611&c=WEB&cver=1.20170511&cplayer=UNIPLAYER&cbr=Chrome&cbrver=57.0.2987.133&cos=Macintosh&cosver=10_12_3&adformat=15_2_1&iv_load_policy=1&autoplay=1&width=640&height=360&content_v=R9ifMMnH7C8&authuser=0&ei=1HYaWefGIMGi-APElpiwCw&vis=3)

#### 0x03 分析解析过程
```bash
video_info = parse.parse_qs(get_content('https://www.youtube.com/get_video_info?video_id={}'.format(self.vid)))
```
- get_content
  >
- parse.parse_qs
