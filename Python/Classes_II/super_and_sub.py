"""
In this example class Sub replaces the method of the class Super, but still calls the default one of the parent class.
It can be used in some cases with constructors for example.
"""


class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')
        
x = Sub()
x.method()