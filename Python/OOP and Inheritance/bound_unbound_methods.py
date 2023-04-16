class Spam:
    def doit(self, message):
        print(message)

obj1 = Spam()
obj1.doit('Hello World')

x = obj1.doit # bound method object: instance + function
x('Hello World')

t = Spam.doit # unbound method object (a function in 3.x)
t(obj1, 'howdy')

class Selfless:
    def __init__(self, data):
        self.data = data
    
    def selfless(arg1, arg2): #a simple function in 3.x
        return arg1 + arg2
    
    def normal(self, arg1, arg2):
        return self.data + arg1 + arg2

X = Selfless(2)
print(X.normal(3, 4)) # instance passed to self automatically


print(Selfless.normal(X, 3, 4)) # self expected by method, pass manually
print(Selfless.selfless(3, 4)) # no instance, works in 3.x

# NOTE that the two calls below will fail

X.selfless(3, 4) # this fails because automatically passes an instance to a method that does NOT expect one
Selfless.normal(3,4) # this fails because it does NOT pass an instance to a method that expects one
