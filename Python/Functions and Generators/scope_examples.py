#Global Scope
from argparse import Action

X = 99
X2 = 88

def func(Y): # Y and Z are assigned in function --> locals
    #Local Scope
    Z = X + Y # X is a global
    return Z 
def func2():
    X = 100 # Local X hides the global X, which is what we want
def func3():
    global X2 # global X2 outside def:
    X2 = 99

print('Starting....')
print('Global X = ', X)
print('Global X2 = ', X2)
print('Running func...')
print('Z = ',func(1))
print('Running func2...')
func2()
print('Global X is unchanged, X = ', X)
print('Running func3...')
func3()
print('Now global X2 has been changed by func3, X2 =', X2) 

y, z = 1, 2 #Global variables in module
def all_global():
    global x # x is declared global here and it is now global for the entire module
    x = y + z # y and z do not need to be declared as global, they already are
    
print('Running all_global()...')
all_global()
print('x = ', x)

def f1():
    X = 88
    def f2():
        print('X = ', X) # Reference made in nested def
    f2()

print('Running f1()...')
f1()

def f1_ver2():
    X = 888
    def f2():
        print('X = ', X)
    return f2

print('Using the factory pattern...')
action = f1_ver2()
action()

def f1_ver3(): # this is a way to avoid nesting functions
    x = 8888
    f2_ver2(x)
def f2_ver2(x):
    print('x = ', x)
    
print('Running f1_ver3()...')
f1_ver3()

def func4():
    x = 4
    action = (lambda n: x ** n) # use a lambda function
    return action


print('Running func4()...')
x = func4()
print('Using func4() and lambda ... ', x(2))
  