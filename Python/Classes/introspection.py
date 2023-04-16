class Person:
    def __init__(self,name,job = None,pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self): #example of a method
        return(self.name.split()[-1])
    
    def giveRaise(self, percent): #another example of a method
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self): #method overloading to give a better output when an instance is printed
        return '[Person: %s %s]' % (self.name, self.pay)

#Examples of the Python's introspection tools

bob = Person('Bob Smith')

print(bob)
print(bob.__class__)
print(bob.__class__.__name__)
print(list(bob.__dict__.keys()))

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])
