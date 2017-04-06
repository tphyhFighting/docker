package main

import(
  "fmt"
)

func main()  {
  //1.无缓存
  c := make(chan bool)
  defer close(c)

  go func ()  {
    fmt.Println("go..GO")
    <-c
  }()

 //阻塞，知道 c 被读取
  c <-true
  return
}
