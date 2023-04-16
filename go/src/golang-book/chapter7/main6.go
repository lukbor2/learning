package main
import "fmt"

func mymin(args ...int) int{
        min := args[0]
        for _, v := range args{
            if v <= min {
                min = v
            }
        }
        return min
}

func mymax(args ...int)int{
        max := args[0]
        for _, v:= range args{
            if v >= max {
                max = v
            }
        }
        return max
}

func main(){
        set := []int{10,5,22,90,1}
       fmt.Println("Set is: ", set)
       fmt.Println("Min is: ", mymin(set...))
       fmt.Println("Max is: ", mymax(set...))
}
