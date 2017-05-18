### grpc-cli
main.go
```go
package main

import(
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "grpc-cli/protos"
	"grpc-cli/logger"
)

const (
	address = "192.168.6.1:5001"
	deflink = "https://www.youtube.com/watch?v=PTmeAWqhDBx&spfreload=10"
)

func main()  {
	conn, err := grpc.Dial(address, grpc.WithInsecure())
	if err != nil {
		panic(err)
	}

	defer conn.Close()
	c := pb.NewGreeterClient(conn)
	r, err := c.YoutubeWatch(context.Background(), &pb.YoutubeWatchRequest{
		Link:deflink,
	})

	if err != nil {
		logger.Errorf("err:%v", err)
	}
	logger.Debugf("err:%v", err)
	logger.Debugf("id:%v", r.Id)
	logger.Debugf("fid:%v", r.ThumbnailFid)
	logger.Debugf("thubnailimgfitapi:%v", r.ThumbnailImgFitApi)
	logger.Debugf("thubnailurl:%v", r.ThumbnailUrl)
	logger.Debugf("thubnaillengthseconds:%v", r.LengthSeconds)
}
```
#### 测试效果:
```bash
➜  grpc-cli git:(master) ✗ ./grpc-cli
logmod:7
2017/05/18 15:08:30 [D] [main.go:30] err:<nil>
2017/05/18 15:08:30 [D] [main.go:31] id:PTmeAWqhDBU
2017/05/18 15:08:30 [D] [main.go:32] fid:youtube/PTmeAWqhDBU
2017/05/18 15:08:30 [D] [main.go:33] thubnailimgfitapi:/v2/user/youtube/PTmeAWqhDBU
2017/05/18 15:08:30 [D] [main.go:34] thubnailurl:https://i.ytimg.com/vi/PTmeAWqhDBU/default.jpg
2017/05/18 15:08:30 [D] [main.go:35] thubnaillengthseconds:1540
```
