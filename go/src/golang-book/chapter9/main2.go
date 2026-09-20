

package main

import ("fmt"
        "math")

type Circle struct {
        x, y, r float64
    }

func (c *Circle) area() float64{
    return c.r*c.r*math.Pi   
}

func main(){
    
    c := Circle{0,0,5}
    fmt.Println("My Circle is: ", c.x, c.y, c.r)
    fmt.Println("Area of my Circle is: ", c.area())
}

//In this version the method is written in a different way
//Now it is a real method which can be used with the . notation
