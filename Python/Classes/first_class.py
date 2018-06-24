# defining a class with two methods
# when an instance uses setdata, the attribute data becomes available too

class FirstClass: 
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)    

x = FirstClass()
y = FirstClass()

# notice we can store different types in the data attribute.
# like with variables we don't need to define the type in advance.
x.setdata('King Arthur')
y.setdata(3.14159)

x.display()
y.display()

x.data = 'New Value' # another way to access the data attribute
x.display()