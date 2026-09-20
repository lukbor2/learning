def f1(a,b): #normal args
    print(a,b)

def f2(a, *b): #positional varargs
    print(a,b)

def f3(a, **b): #keyword varargs
    print(a,b)

def f4(a, *b, **c): #Mixed
    print(a,b,c)

def f5(a, b=2, c=3): #Defaults
    print(a,b,c)

def f6(a, b=2, *c): #Defaults and positional
    print(a,b,c)
    
f1(1,2)
f1(b=2, a=1)

f2(1,2,3)

f3(1, x=2, y=3)

f4(1,2,3,x=2,y=3)

f5(1)
f5(1,4)

f6(1)
f6(1,3,4)