# ubuntu:14.04
FROM debian:jessie-slim
MAINTAINER huoyinghui "huoyinghui@qpkpure.com" 
RUN apt-get update
RUN apt-get install -y nginx
ONBUILD COPY index.html /usr/share/nginx/html
EXPOSE 80
eNTRYPOINT ["/usr/bin/nginx"]
