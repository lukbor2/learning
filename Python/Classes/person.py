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

class Manager(Person): #sub-class
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay) #like in giveRaise we re-use the method of the super-class and do NOT re-write the code
        
    def giveRaise(self, percent, bonus = 0.10): #we re-use the giveRaise method of the super-class by explicitly calling it Person.giveRaise. We don't re-write the entire code.
        Person.giveRaise(self, percent + bonus)
    


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
        