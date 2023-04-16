from trace import Wrapper

x = Wrapper([1,2,3]) #wrapping a list object
x.append(4)
print(x.wrapped)

x = Wrapper({'a': 1, 'b': 2}) #wrapping a dictionary object
print(list(x.keys()))