class Indexer:
    data = [5,6,7,8,9]
    def __getitem__(self, index): # called for index or slice
        print('getitem: ', index)
        return self.data[index] # perform index or slice

X = Indexer()
print(X[0]) # prints 5
print(X[1]) # prints 6
print(X[-1]) # prints 9

# when called for slicing the method receives a slice object
# run with Python 3
print(X[2:4])
print(X[1:])
print(X[:-1])
print(X[::2])