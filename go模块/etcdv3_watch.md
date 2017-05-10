#### etcdv3cli 使用watch监测节点变化, 动态更新groupcache peek

##### 0.关键字
```bash
etcd+groupcache 动态更新peek
```
##### 1.需求
```bash
需要监测/prefix/nodes/下的节点是否有新增或删除。

新增: 查看新增节点是否已经存在.
    若存在，无需更新peek.
    不存在，更新peek, 增加一个节点。
删除: 更新peek, 减少一个节点.

```

##### 2.代码
```go
func (s *ServiceRegistry) Watch(watcherHandler Watcher) {
	key := fmt.Sprintf("/%s/nodes/", s.name)
	logger.Infof("Watch start...:key(%v)", key)
  //用来保存节点状态。
	nodeDict := map[string]bool{}

	rch := s.etcd_client.Watch(context.Background(), key, clientv3.WithPrefix())
	needUpdate := false
	for wresp := range rch {
		for _, ev := range wresp.Events {
			//是否有更新
			if ev.Type == mvccpb.PUT {
				if _, ok := nodeDict[string(ev.Kv.Value)]; ok {
					needUpdate = false
				}else{
					nodeDict[string(ev.Kv.Value)] = true
					needUpdate = true
				}
			} else if ev.Type == mvccpb.DELETE {
				if !strings.HasPrefix(string(ev.Kv.Key), key){
					continue
				}
				key := unhashId(string(ev.Kv.Key)[len(key):])
				delete(nodeDict, key)
				needUpdate = true
			}
			logger.Debugf("CLI V3 WATCH: type(%s) key(%q) : value(%q) , NodeDict:(%v) needUpdate(%v)\n",
				ev.Type, ev.Kv.Key, ev.Kv.Value, nodeDict, needUpdate)

			list, err := s.GetNodes()
			if err != nil {
				continue
			}
			//同步node到自动中
			for _, n := range list{
				if _, ok := nodeDict[n.Url]; !ok {
					logger.Debugf("nodeDict add key:%v", n.Url)
					nodeDict[n.Url] = true
				}
			}
			//添加peek
			if needUpdate{
				watcherHandler(list)
			}
		}
	}
}
```

##### 3.代码逻辑
```bash
1.nodeDict 保存节点状态
2.rch 监听通道。
3.遍历rch, 只处理PUT/DELETE事件
4.needUpdate 是否需要更新
  是：执行watcherHandler, 更新peek列表
  否: 无需重置peek
```
