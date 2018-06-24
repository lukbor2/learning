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

class Manager: #in this example we use the composition pattern rather than the inheritance
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay) #the Person object is embedded in the Manager class
    
    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent + bonus)
    
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    
    def __repr__(self):
        return str(self.person)
    
if __name__ == '__main__':
    #this code runs only for test, i.e. when the script runs as a top-level script
    #when it is imported as a module this code will not run
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)
    print('-- All Three --')
    for obj in (bob, sue, tom): #polymorphism in action!
        obj.giveRaise(.10)
        print(obj)
 
    