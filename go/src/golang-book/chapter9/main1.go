//First version of struct and method.

//in ch09_02.go the method is written in a different way

package main

import ("fmt"
        "math")


type Circle struct {
        x, y, r float64
    }

func circleArea(c Circle) float64 {
      return c.r*c.r*math.Pi
}


func main(){
    
    c := Circle{0,0,5}
    fmt.Println("My Circle is: ", c.x, c.y, c.r)
    fmt.Println("Area of my Circle is: ", circleArea(c))
}
