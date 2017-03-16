#镜像源还需要换
#FROM v4tech/imagemagick
#FROM jess/imagemagick
FROM tplinux.cn:xx/apkpure/imgfit:env
MAINTAINER huoyinghui "huoyinghui@apkpure.com"
WORKDIR /app
RUN mkdir -p /app/upload
#COPY conf /app/conf
COPY build/linux-amd64/imgfit /app/imgfit
CMD ["/app/imgfit"]
