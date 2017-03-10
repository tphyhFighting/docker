FROM debian:jessie-slim
MAINTAINER huoyinghui "huoyinghui@apkpure.com"
WORKDIR /app
RUN mkdir -p /app/conf
# 需要解压时使用ADD
#ADD conf /app/conf
#ADD build/linux-amd64/log-collect /app/log-collect
COPY conf /app/conf
COPY build/linux-amd64/log-collect /app/log-collect
CMD ["/app/log-collect"]
