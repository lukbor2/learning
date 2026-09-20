package main
import "fmt"
func oddoreven(x int) (int, bool){
    if x % 2 == 0 {
        return 1, true
    } else {
        return 0, false
    }
}

func main(){
    x, y := oddoreven(10)
    fmt.Println("Is 10 even? ", x,y)
    x, y = oddoreven(5)
    fmt.Println("Is 5 even? ", x, y)

}

