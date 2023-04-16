package main
import "fmt"
func myswap(x *int, y *int){
    temp := *y
    *y = *x
    *x = temp
}

func main(){
    x := 1
    y := 2
    fmt.Println("At the beginning, x = ", x, " and y = ", y)
    myswap(&x, &y)
    fmt.Println("After swap , x = ", x, " and y = ", y)
}
