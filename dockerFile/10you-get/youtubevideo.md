### python pafy
[github](https://github.com/mps-youtube/pafy)

### 0x00 ipython 运行过程
不想处理编码，所以直接用py3
>(py3.5) ➜  abuse-robot git:(upadet_laod_config) ✗ pip install pafy
><br>
>Collecting pafy
><br>
>Installing collected packages: pafy
><br>
Successfully installed pafy-0.5.3.1
><br>
(py3.5) ➜  abuse-robot git:(upadet_laod_config) ✗ pip install youtube_dl
><br>
Collecting youtube_dl
><br>
  Using cached youtube_dl-2017.5.14-py2.py3-none-any.whl
><br>
Installing collected packages: youtube-dl
><br>
Successfully installed youtube-dl-2017.5.14
><br>
(py3.5) ➜  abuse-robot git:(upadet_laod_config) ✗ ipython
><br>
Python 3.5.0 (default, Feb 13 2017, 12:06:45)
><br>
Type "copyright", "credits" or "license" for more information.
><br>

```bash
IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
In [1]: import pafy
In [2]: url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
In [3]: video = pafy.new(url)
In [4]: video.title
Out[4]: 'Richard Jones: Introduction to game programming - PyCon 2014'
In [5]: url = "http://www.youtube.com/watch?v=2EuTs1Yo-Bo"
In [6]: video = pafy.new(url)
In [7]: video.title
Out[7]: "【刺客教條：大革命】- PC特效全開中文劇情電影60FPS - 第七集 -  Episode 7 - Assassin's Creed：Unity - 刺客信條 ： 大革命 - 最強無損畫質影片"
In [8]:
```
