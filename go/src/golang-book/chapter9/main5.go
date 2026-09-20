
//Example of Embedded Types


package main

import ("fmt")

type Person struct{
    name string
}

func (p *Person) Talk(){
    fmt.Println("Hi, my name is ", p.name)
}

type Android struct{
    Person
    Model string
}

func main(){
    a := new(Android)
    a.name = "D3BO"
    a.Talk()
}
