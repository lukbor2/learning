class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other): # overriding method which is used to subtract
        return Number(self.data - other)

X = Number(5)
Y = X - 2
print(Y.data) # prints 3