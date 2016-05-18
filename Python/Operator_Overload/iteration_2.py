class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2 

X = Squares(1,5)
for i in X:
    print(i, end=' ')  # run in Python 3
    
print()
print(list(X)) # without creating a new instance of Squares, the instance X is empty now! It's a one shot iteration