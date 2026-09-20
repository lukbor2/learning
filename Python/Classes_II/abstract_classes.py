# This is a more complex way of defining abstract classes. i.e. classes which require methods to be implemented by its sub-classes.

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass
    
# X = Super() will generate an error, class can not be instantiated because the method action has not been defined.

class Sub1(Super):
    pass

# X = Sub1() will generate an error for the same reason

class Sub2(Super):
    def action(self): print('spam')
    
x = Sub2()
x.delegate()