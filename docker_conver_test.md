##conver 不同版本对500图片处理结果

##0x01 v6.9 成功
```concept
➜  imgfit git:(2-imgfit-docker-convert) ✗ docker run -v `pwd`/:/opt  --rm -it v4tech/imagemagick /bin/sh
/ # cd /opt/
/opt # convert --version
Version: ImageMagick 6.9.6-8 Q16 x86_64 2016-12-26 http://www.imagemagick.org
Copyright: Copyright 1999-2017 ImageMagick Studio LLC
License: http://www.imagemagick.org/script/license.php
Features: Cipher Modules 
Delegates (built-in): fontconfig freetype jng jpeg lcms ltdl png tiff webp zlib
/opt # sh run.sh 
      488       488     39026
/opt # cat run.sh 
#!/bin/sh
# for f in /upload/*
# for f in /Users/apple/go-dev/src/imgfit/upload/*
for f in ./upload/*
do
	if test -f $f
		then
		# echo $f
		cmd="convert -resize  x200 ${f} ${f}_x200.jpg"
		`$cmd`
	fi
done
ls ./upload/*.jpg | wc
rm ./upload/*.jpg
/opt # %                                                                                                                                                                                                            ➜  imgfit git:(2-imgfit-docker-convert) ✗ ls upload | wc
     488     488   30242
```
##0x02 v7.0 成功
```concept
➜  imgfit git:(2-imgfit-docker-convert) ✗ sh run.sh 
     488     488   39026
➜  imgfit git:(2-imgfit-docker-convert) ✗ convert --version
Version: ImageMagick 7.0.4-4 Q16 x86_64 2017-01-15 http://www.imagemagick.org
Copyright: © 1999-2017 ImageMagick Studio LLC
License: http://www.imagemagick.org/script/license.php
Features: Cipher DPC HDRI Modules 
Delegates (built-in): bzlib freetype jng jpeg ltdl lzma png tiff xml zlib
➜  imgfit git:(2-imgfit-docker-convert) ✗ 
```

##0x03 v6.7.8 服务器版本(测试失败, 测试文件均来自服务器处理失败的文件)
```concept
➜  serv-ops git:(local) ✗ fab -H fs12t01  hyh_convert_version
['hyh_convert_version']
Found host by [name], fs12t01: root@167.114.175.4:4550
[root@167.114.175.4:4550] Executing task 'hyh_convert_version'
[root@167.114.175.4:4550] run: convert --version
[root@167.114.175.4:4550] out: Version: ImageMagick 6.7.8-9 2016-06-16 Q16 http://www.imagemagick.org
[root@167.114.175.4:4550] out: Copyright: Copyright (C) 1999-2012 ImageMagick Studio LLC
[root@167.114.175.4:4550] out: Features: OpenMP    
[root@167.114.175.4:4550] out: 
[root@167.114.175.4:4550] out: 
```

##0x04 v6.
