

res = [x ** 2 for x in range(4)] #list comprehension, builds a list
print('List comprehension: ', res)

res = (x ** 2 for x in range(4)) # generator expression builds an iterable 

print('Generator expression: ', res)

res = list(res) #changing into a printable list
print('Generator expression: ', res)

#Generators expressions vs Maps - Example 1

res = list(map(abs, (-1, -2, 3,4)))
print('Using a map: ', res)

res = list(abs(x) for x in (-1, -2, 3,4))
print('Using a generator expression: ', res)

#Generators expressions vs Maps - Example 2

res =list(map((lambda x: x*2), (1,2,3,4)))
print('Using a map with lambda function: ', res)

res = list(x*2 for x in (1,2,3,4)) #simpler as generator??
print('Using a generator expression: ', res)

#Nested generators

res = [x*2 for x in [abs(x) for x in (-1,-2, 3, 4)]]
print('Nested comprehension: ', res)

res = list(map(lambda x: x*2, map(abs, (-1,-2,3,4))))
print('Nested map: ', res)

res = list(x * 2 for x in (abs(x) for x in (-1,-2,3,4)))
print('Nested Generator: ', res)

#When possible do NOT nested

res = list(abs(x)*2 for x in (-1,-2,3,4))
print('Same result not nested: ', res)

#Generators vs Filters

line = 'aa bbb c'
res = ''.join(x for x in line.split() if len(x) > 1)
print('Generator with if: ', res)

res = ''.join(filter(lambda x: len(x)>1, line.split())) #in this case filter's complexity is very similar to generator
print('Using a filter: ', res)

res = ''.join(x.upper() for x in line.split() if len(x) > 1)
print('Generator with if and a function: ', res)

res = ''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))) #in this case the generator is simpler
print('Using a filter and a map for the same result: ', res)

#Generator Functions vs Generator Expressions

G = (c * 4 for c in 'SPAM') #generator expression
print('Using a generator expression: ', list(G))

def timesfour(S):
    for c in S:
        yield c * 4
G = timesfour('spam')
print('Using a generator function: ', list(G))




