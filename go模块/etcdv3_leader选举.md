#### etcdv3cli 对客户端选举leader

##### 0.关键字
```bash
etcd+health 动态选主，主节点进行健康检查
```

#### 1.需求
```bash
在etcd多个节点中，需要选择一个作为leader,完成health检查.
```
#### 2.代码
```bash
func IsLeaderV3(endpoints []string)  (bool){
	cli, err := clientv3.New(clientv3.Config{
		Endpoints: endpoints,
	})
	if err != nil {
		logger.Errorf("err:%v", err)
		return false
	}
	defer cli.Close()
	s, err := concurrency.NewSession(cli)
	if err != nil {
		logger.Errorf("err:%v", err)
		return false
	}
	key := "/imgcache/nodes/ele-leader"

	leaderValue, err := getMyIp()
	if err != nil {
		logger.Errorf("err:%v", err)
		return false
	}

	e := concurrency.NewElection(s, key)
	resp, err := e.Leader(context.TODO())
	if err == nil {
		//是leader
		logger.Debugf("Election Exists resp:%v", resp)
		for _, ev := range resp.Kvs {
			if string(ev.Value) == leaderValue {
				return true
			}
		}
		return false
	}

	logger.Info("Election Campaign...")
	err = e.Campaign(context.TODO(), leaderValue)
	if err != nil {
		logger.Errorf("err:%v", err)
		return false
	}

	logger.Debugf("Election Campaign..Finish")
	resp, err = e.Leader(context.TODO())
	if err != nil {
		logger.Errorf("err:%v", err)
		return false
	}
	logger.Debugf("Election is Leader, Campaign Ok resp:%v", resp)
	return true
}
```
#### 3.代码逻辑
```bash
同时在多个节点上运行程序，同一个时间只有一个会被选为leader
1.当前是否有leader.
  无:参加竞选,
    竞选成功，就是leader->返回true
    竞选失败，返回false
  有:进行2
2.当前节点是不是leader.
  是:返回true
  否:返回false
if IsLeaderV3() {
  DoHealth()
}
```
