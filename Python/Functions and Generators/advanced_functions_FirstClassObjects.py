#In Python functions are objects so I can do things like this one
print('*** Functions are objects ***')
def echo(message):
    print('Message from echo: ', message)

echo('Direct Call')
x = echo
x('Indirect Call')

#Arguments are passed by assigning objects, therefore I can pass a function as an argument

print('*** Passing a function as an argument ***')

def indirect(func, arg):
    func(arg)

indirect(echo, 'Argument Call')

#Include functions into data structures

print('*** Functions in data structures ***')

schedule = [(echo, 'spam!'),(echo,'ham!')]
for (func, arg) in schedule:
    func(arg)
    
#Functions can be created and returned for use elsewhere

print('*** Returning a function ***')

def make(label):
    def echo(message):
        print(label + ' : ' + message)
    return echo

F = make('Spam')
F('Ham!')
F('Eggs!')
