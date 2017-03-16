docker run -it -p 8000:8000 -v `pwd`/config.json:/app/config.json lc:v2 bash -c "/app/imgfit -logtostderr"

➜  imgfit git:(2-dockerfile) ✗ docker run -it -p 8000:8000 -v `pwd`/config.json:/app/config.json lc:v2 bash                              
root@0ccf3b6da6c4:/app# convert --version
Version: ImageMagick 6.8.9-9 Q16 x86_64 2017-03-12 http://www.imagemagick.org
Copyright: Copyright (C) 1999-2014 ImageMagick Studio LLC
Features: DPC Modules OpenMP
Delegates: bzlib cairo djvu fftw fontconfig freetype jbig jng jpeg lcms lqr ltdl lzma openexr pangocairo png rsvg tiff wmf x xml zlib
root@0ccf3b6da6c4:/app# 


#每次更新imgfit后，需要重新构建
➜  imgfit git:(master) docker run -it -p 8000:8000 -v `pwd`/config.json:/app/config.json `pwd`/build/linux-amd64 local-imgfit:v1.7 /app/imgfit -logtostderr
➜  imgfit git:(master) docker build -t local-imgfit:v1.7 .
Sending build context to Docker daemon 41.48 MB
Step 1/7 : FROM debian:jessie-slim
 ---> 7d86024f45a4
Step 2/7 : MAINTAINER huoyinghui "huoyinghui@qpkpure.com"
 ---> Using cache
 ---> e5de3748dd9f
Step 3/7 : RUN apt-get update && apt-get install -y imagemagick
 ---> Using cache
 ---> f68384124432
Step 4/7 : WORKDIR /app
 ---> Using cache
 ---> 6de2ce51a7fc
Step 5/7 : RUN mkdir -p /app/upload
 ---> Using cache
 ---> dacc6cee6db2
Step 6/7 : COPY build/linux-amd64/imgfit /app/imgfit
 ---> cff6cd8e8452
Removing intermediate container 1f3931387748
Step 7/7 : CMD /app/imgfit -logtostderr 
 ---> Running in 0b92a303341d
 ---> 9bc182174764
Removing intermediate container 0b92a303341d
Successfully built 9bc182174764
➜  imgfit git:(master) ls                                 
➜  imgfit git:(master) docker run -it -p 8000:8000 -v `pwd`/config.json:/app/config.json local-imgfit:v1.7 /app/imgfit -logtostderr
I0314 08:33:08.847063       1 main.go:110] config-v: {YHGIZY2NY26FAE3DXOM8 FPVPcBLQXRFGB4hfQaNFiZaV2AYSSlUdxJLRKSrU OVH-BHS http://192.168.0.18:7380 0.0.0.0:8000  [image upload] map[image:1 upload:1]}
I0314 08:33:08.847388       1 main.go:153] StartWebSer...start

