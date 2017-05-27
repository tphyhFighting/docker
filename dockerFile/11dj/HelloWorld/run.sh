docker run --log-opt max-size=10m --log-opt max-file=3 --name  dj-hello  -d  --restart always -v `pwd`:/usr/src/app -p 8000:8000 dj-local
