## groupcache 源码学习



## 1.sinagleflight
```
singleflight.go
// call is an in-flight or completed Do call
type call struct {
	wg  sync.WaitGroup
	val interface{}
	err error
}

// Group represents a class of work and forms a namespace in which
// units of work can be executed with duplicate suppression.
type Group struct {
	mu sync.Mutex       // protects m
	m  map[string]*call // lazily initialized
}

// Do executes and returns the results of the given function, making
// sure that only one execution is in-flight for a given key at a
// time. If a duplicate comes in, the duplicate caller waits for the
// original to complete and receives the same results.
func (g *Group) Do(key string, fn func() (interface{}, error)) (interface{}, error) {
	g.mu.Lock()
	if g.m == nil {
		g.m = make(map[string]*call)
	}
	if c, ok := g.m[key]; ok {//后来者等果实
		g.mu.Unlock()         //放开锁，让后来的人可以进来等
		c.wg.Wait()           //等待第一个人的果实
		return c.val, c.err   //拿到果实，返回
	}
	c := new(call)
	c.wg.Add(1)               //
	g.m[key] = c              //第一个工作者，占位完毕
	g.mu.Unlock()             //已经成功占位，可以让别人进来了

	c.val, c.err = fn()       //执行任务
	c.wg.Done()               //共享果实

	g.mu.Lock()
	delete(g.m, key)
	g.mu.Unlock()

	return c.val, c.err
}
```
	1.Group struct 锁+字典
	2.call 使用WaitGrop, 一人工作，果实共享, 避免重复劳动
	3.DO
		1.第一个执行DO("key", ) 的人会进行工作，其他后来者，调用wait()等待果实. 
		2.在第一个人执行delete后，key从字典中被删除，本次果实消耗完毕。
		3.再来的Do("key"), 重新获取工作获取果实

## 2.testDemo
	1.10 个go程同时do('key'), 第一个占位成功的go程执行fn, 从通道中读数据，被阻塞; 其他的go程wait()
	2.主go程会写入"bar" 给通道, 唤醒读端
	3.第一占位成功的go程，读取到通道中数据后返回，wg.done().
	4.其他go程读取结果。 

```
func TestDoDupSuppress(t *testing.T) {
	var g Group
	c := make(chan string)
	var calls int32
	fn := func() (interface{}, error) {
		atomic.AddInt32(&calls, 1)
		t.Logf("only once")                    //只会被第一个占位成功的go程执行
		return <-c, nil
	}

	const n = 10
	var wg sync.WaitGroup
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func() {
			v, err := g.Do("key", fn)
			if err != nil {
				t.Errorf("Do error: %v", err)
			}
			if v.(string) != "bar" {
				t.Errorf("got %q; want %q", v, "bar")
			}
			t.Logf("v:%v", v)
			wg.Done()
		}()
	}
	time.Sleep(100 * time.Millisecond) // let goroutines above block
	c <- "bar"
	wg.Wait()
	if got := atomic.LoadInt32(&calls); got != 1 {
		t.Errorf("number of calls = %d; want 1", got)
	}
}
```
运行结果:
```
/usr/local/Cellar/go/1.7.4_1/libexec/bin/go test -v imgfit/vendor/github.com/golang/groupcache/singleflight -run ^TestDoDupSuppress$
	singleflight_test.go:61: only once
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
	singleflight_test.go:77: v:bar
ok  	imgfit/vendor/github.com/golang/groupcache/singleflight	0.110s
```
