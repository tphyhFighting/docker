## 编解码

```
Python 2.7.10 (default, Jul 30 2016, 19:40:32) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> pirnt "http://apkpure.com/ほっくーnavi/jp.co.hokuyobank.hokkunavi"
  File "<stdin>", line 1
    pirnt "http://apkpure.com/ほっくーnavi/jp.co.hokuyobank.hokkunavi"
                                                                         ^
SyntaxError: invalid syntax
>>> pirnt u"http://apkpure.com/ほっくーnavi/jp.co.hokuyobank.hokkunavi"
  File "<stdin>", line 1
    pirnt u"http://apkpure.com/ほっくーnavi/jp.co.hokuyobank.hokkunavi"
                                                                          ^
SyntaxError: invalid syntax
>>> s = "http://apkpure.com/ほっくーnavi/jp.co.hokuyobank.hokkunavi"
>>> s
'http://apkpure.com/\xe3\x81\xbb\xe3\x81\xa3\xe3\x81\x8f\xe3\x83\xbcnavi/jp.co.hokuyobank.hokkunavi'
>>> type(s)
<type 'str'>
>>> 
```
