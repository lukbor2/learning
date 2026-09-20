
package main

import ("fmt"; "math")


type Circle struct {
        x, y, r float64
    }

type Rectangle struct{
    x1, y1, x2, y2 float64
}

func distance(x1, y1, x2, y2 float64) float64 {
    a := x2 - x1
    b := y2 - y1
    return math.Sqrt(a*a + b*b)
}

func (c *Circle) area() float64{
    return c.r*c.r*math.Pi
}

func (r *Rectangle) area() float64{
    l:= distance(r.x1, r.y1, r.x1, r.y2)
    w:= distance(r.x1, r.y1, r.x2, r.y1)
    return l*w
}

func main(){

    c := Circle{0,0,5}
    fmt.Println("My Circle is: ", c.x, c.y, c.r)
    fmt.Println("Area of my Circle is: ", c.area())
 
    r := Rectangle{0,0,10,10}
    fmt.Println("My Rectangle is: ", r.x1, r.y1, r.x2, r.y2)
    fmt.Println("Area of my Rectangle is: ", r.area())

}
