X = 11 # Global (module) name/attribute

def f():
    print(X) # Access global X

def g():
    X = 22 # Local (function) variable
    print(X)

class C:
    X = 33 # Class attribute
    def m(self):
        X = 44 # Local attribute in method
        self.X = 55 # Instance attribute


if __name__ == '__main__':
    print(X)
    f()
    g()
    print(X)
    
    obj = C()
    print(obj.X)
    
    obj.m()
    print(obj.X) # Prints 55, it's the instance X
    print(C.X) # Prints 33, the class X