docker run --name imgfit -it --network host -v /home/imgfit/config.json:/app/congfig.json   -v /home/imgfit/conf/:/app/conf/ registry.pureapk.com/apkpure/imgfit


1.ok
docker run -it -p 8001:8001 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 


2.ok.  路径没有问题
docker run -it -p 8001:8001 -v /home/imgfit/config.json:/app/config.json -v /home/imgfit/conf:/app/conf  registry.pureapk.com/apkpure/imgfit   

3.ok
docker run --name imgfit -it -p 8001:8001 -v /home/imgfit/config.json:/app/config.json -v /home/imgfit/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 


4.ok
docker run --name imgfit  --network host  -it -p 8001:8001 -v /home/imgfit/config.json:/app/config.json -v /home/imgfit/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 


5.ok -it 在--network 后
docker run --name imgfit  --network host  -it -v /home/imgfit/config.json:/app/config.json -v /home/imgfit/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 

6.

docker run --name imgfit  -it --network host -v /home/imgfit/config.json:/app/config.json -v /home/imgfit/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 


7. 
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -d  --restart always --network host -v /home/imgfit/config.json:/app/config.json -v /home/imgfit/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 


8.
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -d  --restart always --network host -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 


docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -d  --restart always -p 8001:8001 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  registry.pureapk.com/apkpure/imgfit 



docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -d  --restart always -p 8001:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  imgfit 


==================================
170329
ser:
make docker
docker build --no-cache   -t imgfit  -f Dockerfile.app .
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -d  --restart always -p 8001:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/build/conf:/app/conf  imgfit

docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -it -p 8000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/build/conf:/app/conf  imgfit bash

cache-s: 9000
make docker
docker build --no-cache   -t imgfitcache  -f Dockerfile.app .
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit-c -d  --restart always -p 9000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/conf:/app/conf  iimgfitcache 
