#!/bin/sh
cd  && cd /home/webgp;
docker run --name webgp -d --restart always -p 5000:5000 -v `pwd`/conf:/app/conf apk.302e.com:3000/huoyinghui/webgp-spider
