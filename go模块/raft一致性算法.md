##### raft

#### 1.raft理论
- [raft官网](https://raft.github.io/)
- [raft-介绍](http://www.infoq.com/cn/articles/raft-paper)
- [raft论文](https://ramcloud.atlassian.net/wiki/download/attachments/6586375/raft.pdf)

#### 2.raft 实现
- python
  - py-raft
- go
  - etcd/raft

#### 3.raft 概念
- 领导选取（leader selection）
- 日志复制（log replication
- Raft 使用随机定时器来选取领导者。这种方式仅仅是在所有算法都需要实现的心跳机制上增加了一点变化，它使得在解决冲突时更简单和快速
- 安全性（safety）

##### 3.1实际系统的一致性算法一般有以下特性
- 确保安全性.即使出现异常时，也不会返回一个错误的结果.
- 高可用性.只要集群中的大部分机器都能运行，可以互相通信并且可以和客户端通信，这个集群就可用.
- 不依赖时序保证一致性.
##### 3.2 Paxos 算法的不足
