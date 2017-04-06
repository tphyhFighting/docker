package main

import(
  "fmt"
)

func main()  {
  c := make(chan bool)
  defer close(c)

  go func ()  {
    fmt.Println("go..GO")
    c <-true
  }()

  // <-c
  for _, v := range c {
    fmt.Println("v:%v", v)
  }
  return
}
