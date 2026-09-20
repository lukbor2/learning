class NextClass:
    def printer(self, text):
        self.message = text # even if defined inside a method, message becomes and attribute of the class.
        print(self.message)
        

x = NextClass()
x.printer('instance call')
print(x.message)