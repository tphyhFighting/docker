docker run -it -p 8000:8000 -v `pwd`/config.json:/app/config.json lc:v2 bash -c "/app/imgfit -logtostderr"

➜  imgfit git:(2-dockerfile) ✗ docker run -it -p 8000:8000 -v `pwd`/config.json:/app/config.json lc:v2 bash                              
root@0ccf3b6da6c4:/app# convert --version
Version: ImageMagick 6.8.9-9 Q16 x86_64 2017-03-12 http://www.imagemagick.org
Copyright: Copyright (C) 1999-2014 ImageMagick Studio LLC
Features: DPC Modules OpenMP
Delegates: bzlib cairo djvu fftw fontconfig freetype jbig jng jpeg lcms lqr ltdl lzma openexr pangocairo png rsvg tiff wmf x xml zlib
root@0ccf3b6da6c4:/app# 
