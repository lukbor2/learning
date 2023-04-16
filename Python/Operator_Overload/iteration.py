# overloading __getitem__ can be used to implement iteration, list comprehension, map calls too
# to implement iteration remember __iter__ is the preferred way, rather than __getitem__
# run in Python 3


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = "Spam"

print(X[1])
for item in X:
    print(item, end=' ') # run in Python 3

print()    
print('p' in X)
print([c for c in X]) # list comprehension
print(list(map(str.upper, X))) # map calls

(a,b,c,d) = X # Sequence assignments
print(a,c,d)

# ... and so on
print(list(X))
print(tuple(X))
print(''.join(X))