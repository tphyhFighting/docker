FROM postgres:9.6-alpine
WORKDIR /app
RUN mkdir -p /tmp/smart_backup
#RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
RUN apk add --update tzdata
#sendmail x509
RUN apk add --update ca-certificates
ENV TZ=Asia/Shanghai
# Clean APK cache
RUN rm -rf /var/cache/apk/*
CMD [""]
