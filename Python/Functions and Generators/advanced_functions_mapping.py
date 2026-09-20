#First example of map
print('*** First example of map ***')
def inc(x): return x + 10

counters = [1,2,3,4]
print(list(map(inc, counters)))

#Using lambda and map
print('*** Using lambda and map ***')

print(list(map((lambda x: x + 3),counters)))

#Map taking multiple sequences and sending them to the function mapped

print('*** Map with multiple sequences ***')

print(list(map(pow, [1,2,3],[2,3,4]))) #1**2, 2**3, 3**4 

#Map is similar to list comprehension expressions

print('*** Map similar to list comprehensions ***')

print(list(map(inc, [1,2,3,4])))
print([inc(x) for x in [1,2,3,4]])

