package main

import(
  "fmt"
  "time"
)

func main()  {
  // Go()
  go Go()
  time.Sleep(2*time.Second)

}

func Go()  {
  fmt.Println("Go ..go")
}
