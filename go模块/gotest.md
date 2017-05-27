##### gotest


##### go test -v imgfit/controllers -run ^TestNewV3Election$
```bash
➜  imgfit git:(10-etcd-leader) ✗ go test -v imgfit/controllers -run ^TestNewV3Election$
logmod:7
2017/04/28 17:35:53 [I] [root.go:61] No cacheable err:parsing "": invalid syntax
2017/04/28 17:35:53 [D] [root.go:67] cacheManager new ok: <nil>
=== RUN   TestNewV3Election
2017/04/28 17:35:53 [D] [etcd_test.go:262] session:&{0xc4200af1e0 0xc42019f800 7587821772257559355 0x41ded30 0xc420228120}
2017/04/28 17:35:53 [D] [etcd_test.go:264] election:&{0xc42021a360 /imgcache/nodes/ele-leader/  0 <nil> <nil>}
2017/04/28 17:35:53 [E] [etcd_test.go:274] Election Is not leader err:election: no leader
2017/04/28 17:35:53 [I] [etcd_test.go:275] Election Campaign...
2017/04/28 17:35:53 [D] [etcd_test.go:287] Election Campaign..Finish
2017/04/28 17:35:53 [D] [etcd_test.go:290] Election is Leader, Campaign Ok resp:&{cluster_id:14841639068965178418 member_id:10276657743932975437 revision:1278 raft_term:2  [key:"/imgcache/nodes/ele-leader/694d5bb32a63033b" create_revision:1278 mod_revision:1278 version:1 value:"192.168.9.41" lease:7587821772257559355 ] false 1}
--- PASS: TestNewV3Election (0.03s)
PASS
ok  	imgfit/controllers	0.101s
➜  imgfit git:(10-etcd-leader) ✗
```
