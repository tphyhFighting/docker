##imgfit
docker run --log-opt max-size=10m --log-opt max-file=3 --name imgfit -it -p 8000:8000 -v `pwd`/config.json:/app/config.json -v `pwd`/build/conf:/app/conf  imgfit bash

## etcd

etcd -name etcd0 -initial-advertise-peer-urls http://192.168.9.3:2380 \
  -listen-peer-urls http://192.168.9.3:2380 \
  -listen-client-urls http://192.168.9.3:2379,http://127.0.0.1:2379 \
  -advertise-client-urls http://192.168.9.3:2379 \
  -initial-cluster-token my-etcd-cluster \
  -initial-cluster etcd0=http://192.168.9.3:2380,etcd1=http://192.168.9.99:2380,etcd2=http://192.168.9.41:2380 \
  -initial-cluster-state new



etcd -name etcd2 -initial-advertise-peer-urls http://192.168.9.41:2380 \
    -listen-peer-urls http://192.168.9.41:2380 \
    -listen-client-urls http://192.168.9.41:2379,http://127.0.0.1:2379 \
    -advertise-client-urls http://192.168.9.41:2379 \
    -initial-cluster-token my-etcd-cluster \
    -initial-cluster etcd0=http://192.168.9.3:2380,etcd1=http://192.168.9.99:2380,etcd2=http://192.168.9.41:2380 \
    -initial-cluster-state new


    etcd -name etcd1 -initial-advertise-peer-urls http://192.168.9.99:2380 \
        -listen-peer-urls http://192.168.9.99:2380 \
        -listen-client-urls http://192.168.9.99:2379,http://127.0.0.1:2379 \
        -advertise-client-urls http://192.168.9.99:2379 \
        -initial-cluster-token my-etcd-cluster \
        -initial-cluster etcd0=http://192.168.9.3:2380,etcd1=http://192.168.9.99:2380,etcd2=http://192.168.9.41:2380 \
        -initial-cluster-state new


    etcd -name etcd1 -initial-advertise-peer-urls http://10.0.1.11:2380 \
      -listen-peer-urls http://10.0.1.11:2380 \
      -listen-client-urls http://10.0.1.11:2379,http://127.0.0.1:2379 \
      -advertise-client-urls http://10.0.1.11:2379 \
      -initial-cluster-token my-etcd-cluster \
      -initial-cluster etcd0=http://10.0.1.10:2380,etcd1=http://10.0.1.11:2380,etcd2=http://10.0.1.12:2380 \
      -initial-cluster-state new

firewall-cmd --zone=public --add-port=2379/tcp --permanent
firewall-cmd --zone=public --add-port=2380/tcp --permanent
firewall-cmd --zone=public --add-port=9000/tcp --permanent
firewall-cmd --zone=public --add-port=7000/tcp --permanent
firewall-cmd --reload
