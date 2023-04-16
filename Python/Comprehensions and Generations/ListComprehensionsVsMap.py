#The same result can be achieved with a custom function, a map and a list comprehension

#Using a custom Function
res = []
for x in 'spam':
    res.append(ord(x))

print('Function result: ', res)

#Using map

res = list(map(ord, 'spam'))
print('Map result: ', res)

#Using list comprehension

res = [ord(x) for x in 'spam']
print('List comprehension result: ', res)

#Using map with lambda function

res = list(map((lambda x: x**2), range(10)))
print('Map with lambda result: ', res)

#Using list comprehension

res = [x ** 2 for x in range(10)]
print('List comprehension result: ', res)
