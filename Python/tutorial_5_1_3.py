
def f(x):
    return x%3 == 0 or x%5 == 0

def cube(x):
    return x*x*x

a = []
for i in filter(f, range(2,25)):
    a.append(i)

print("Result from the filter function", a)


a = []
for i in map(cube, range(1,11)):
    a.append(i)

print("Result from the map function", a)

