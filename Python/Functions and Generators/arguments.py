#First example, lack of name aliasing

def f(a):
    a = 99 # a lives only within the function f scope
b = 88
print('**** First example, lack of name aliasing ****')
print('Value of b BEFORE calling the function is: ', b)
f(b)
print('Value of b AFTER calling the function is: ', b)

#passing a mutable object as an argument

def changer(a,b):
    a = 2
    b[0] = 'spam' # the list is mutable, therefore the function changer does change the list
    
X = 1
L = [1,2]
print('**** Example of how a function changes an argument which is a mutable object ****')
print('Values of the arguments BEFORE calling the function')
print('X = ', X)
print('L = ', L)
changer(X,L)
print('Values of the arguments AFTER calling the function')
print('X = ', X)
print('L = ', L)

#Simulating output parameters and Multiple Results

def multiple(x,y):
    x = 2
    y = [3,4]
    return x,y
X = 1
L = [1,2]
print('**** Results are returned from the function called and assigned back to the original arguments ****')
print('Values of the arguments BEFORE calling the function')
print('X = ', X)
print('L = ', L)
X, L = multiple(X, L)
print('Values of the arguments AFTER calling the function')
print('X = ', X)
print('L = ', L)

#Passing arguments by position

def f(a,b,c):
    print(a,b,c) 
print('**** Passing arguments by position ****')
f(1,2,3)

#Keyword Arguments

print('**** Using keyword arguments ****')
f(c=3, a=1, b=2)

#Combining keyword arguments and passing by position
print('**** Combining keyword arguments and passing by position ****')
f(1, c=3, b=2)

#Using defaults

def f(a, b=2, c=3):
    print(a,b,c)

print('**** Using Defaults ****')
print('Calling with one required argument')
f(20)
f(a=30)

print('Calling with two arguments')
f(40,4)

print('Calling with three arguments')
f(50,4,11)

print('Keywords and defaults together')
f(1, c=6)

print('Final example')
def func(spam, eggs, toast=0, ham=0): #first two required, last two with defaults
    print(spam, eggs, toast, ham)

func(1,2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1,2,3,4)

#Arbitrary arguments examples

def f(*args):
    print(args)

print('**** Arbitrary arguments ****')
print('Example 1 - Collecting arguments')
f()
f(1,2,3,4)

def f(**args):
    print(args)
    
print('Example 2 - Collecting arguments in a dictionary')
f()
f(a=1, b=2)

def f(a,*pargs, **kargs):
    print(a,pargs, kargs)

print('Example 3 - Combining all together')
f(1,2,3,x=1,y=2)

#Unpacking arguments
print('**** Unpacking Arguments ****')
def func(a,b,c,d):
    print(a,b,c,d)
args=(1,2)
args += (3,4)

print('Example 1 - Example of unpacking arguments using the * syntax')
func(*args)

print('Example 2 - Example of unpacking arguments using the ** syntax')
args ={'a':11, 'b': 22, 'c': 33}
args['d'] = 44
func(**args)

print('Example 3 - Combining different syntaxes')
func(*(1,2),**{'d':4, 'c':3})
func(1, *(2,3), **{'d':4})
func(1, c=3, *(2,), **{'d':4})
func(1, *(2,3,), d=4)
func(1,*(2,), c=3, **{'d':4})

print('Example 4 - When this technique might be used')

def tracer(func, *pargs, **kargs):
    print('calling: ', func.__name__)
    return func(*pargs, **kargs)

def func(a,b,c,d):
    return a+b+c+d

print(tracer(func, 1,2,c=3, d=4))

#Keyword-Only Arguments

print('**** Using Keyword-Only Arguments (3.x) ****')

print('Example 1 -  How to call the function with keyword-only args')
def kwonly(a,*b, c): #c is keyword-only
    print(a,b,c)

kwonly(1,2,4,5,6,c=3)
kwonly(a=1, c=3)
#kwonly(1,2,3)
#TypeError: kwonly() missing 1 required keyword-only argument: 'c' 

print('Example 2 -  Another example')
def kwonly(a,*,b,c): #b and c are keyword-only
    print(a,b,c)

kwonly(1,c=3, b=2)
kwonly(c=3, b=2, a=1)
#kwonly(1,2,3)
#TypeError: kwonly() takes 1 positional argument but 3 were given
#kwonly(1)
#TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'

print('Example 3 - Using defaults with keyword-only')
def kwonly(a,*, b='spam',c='ham'):
    print(a,b,c)

kwonly(1)
kwonly(1,c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)
#kwonly(1,2)
#TypeError: kwonly() takes 1 positional argument but 2 were given

    