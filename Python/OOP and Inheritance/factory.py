# Example of a factory which builds classes


def factory(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job
        
obj1 = factory(Spam)
obj2 = factory(Person, "Arthur", "King")
obj3 = factory(Person, name="Brian")

obj1.doit(99)
print(obj2.name, obj2.job)
print(obj3.name, obj3.job)
       