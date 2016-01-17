# Example of how to use OOP to customize (specialize) the behavior of a class

class FirstClass: 
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)    

class SecondClass(FirstClass):
    def display(self): #changing the display method of the superclass
        print('Current Value = "%s"' % self.data)
        
z = SecondClass()
z.setdata(42)
z.display()