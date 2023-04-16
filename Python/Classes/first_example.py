class C2:
    pass

class C3:
    pass

# class C1 has C2 and C3 as super-classes

class C1(C2, C3):
    def setname (self, who):
        self.name = who # In this case the attribute name does not exist until the function setname is called

class C4(C2, C3):
    def __init__(self,who):
        self.name = who # By defining a constructor the attribute name will be created when an instance of this class is created

I1 = C1()
I2 = C1()

I1.setname('bob')
I2.setname('sue')

print(I1.name)
print(I2.name)

I3 = C4('john')
print(I3.name)
