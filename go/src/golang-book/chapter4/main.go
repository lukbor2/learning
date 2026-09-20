package main
import "fmt"
func main(){
        fmt.Println("Enter a number: ")
        var input float64
        fmt.Scanf("%f",&input)
        fmt.Println("Conversion from Farenheit to Celsius: ", (input-32)*5/9)
}

