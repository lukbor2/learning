#Using filter

print('*** First example of using filter ***')
print(list(filter((lambda x: x >0), range(-5,5))))

#Like map, filter is close to list comprehension

print('*** Filter is similar to list comprehension ***')

print([x for x in range(-5,5) if x > 0])

#Example with reduce

from functools import reduce

print('Adding elements in a sequence: ', reduce((lambda x,y: x+y), [1,2,3,4]))

print('Multiplying elements in a sequence: ',reduce((lambda x,y: x * y), [1,2,3,4] ))
