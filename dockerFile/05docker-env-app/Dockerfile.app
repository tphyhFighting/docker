#镜像源还需要换
#依赖于env
#只编译app需要的镜像
FROM tplinux:xx/apkpure/imgfit:env
MAINTAINER huoyinghui "huoyinghui@apkpure.com"
WORKDIR /app
RUN mkdir -p /app/upload
COPY build/linux-amd64/imgfit /app/imgfit
CMD ["/app/imgfit "]
