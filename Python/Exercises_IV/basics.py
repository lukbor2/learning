"Function which prints its argument"

def print_argument(arg):
    print("Printing argument ...")
    print(arg)
    

print_argument('luca')
print_argument(100)
print_argument([1,2,3])
print_argument({ 'name': 'Bob', 'age': '45'})

" print_argument() --> Not passing any argument triggers an error"

" print_argument(100, 'luca') --> Passing two arguments is an error too"

