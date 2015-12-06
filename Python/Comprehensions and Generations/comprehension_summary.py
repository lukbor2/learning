#List comprehension
l = [x for x in range(10)]
print('List comprehension: ', l)

#Generator expression
l = (x*x for x in range(10))
print('Generator expression: ', l)
print('Generator expression: ', list(l))

s = {x * x for x in range(10)}
print('Set comprehension: ', s)

s = set(x * x for x in range(10))
print('Generator expression: ', s)

d = {x: x * x for x in range(10)}
print('Dictionary comprehension: ', d)
d = dict((x, x * x) for x in range(10))
print('Generator expression: ', d)

#Nested if statement
l = [x * x for x in range(10) if x % 2 == 0] #collect squares of even numbers. Lists are ordered.
print('List comprehension with nested if: ', l)

s = {x * x for x in range(10) if x % 2 == 0} #Sets are not ordered.
print('Set comprehension with nested if: ', s)

d = {x: x * x for x in range(10) if x % 2 == 0} #Dictionary keys are not ordered
print('Dictionary comprehension with nested if: ', d)

#Nested for loops work too
l = [x + y for x in [1,2,3] for y in [4,5,6]] #Lists keep duplicates
print('List comprehension with nested for: ', l)

s = {x + y for x in [1,2,3] for y in [4,5,6]} #Sets do NOT keep duplicates
print('Set comprehension with nested for: ', s)

d = {x: y for x in [1,2,3] for y in [4,5,6]} #No duplicated keys in the dictionary
print('Dictionary comprehension with nested for: ', d)

#Temporary loop variable names in comprehension are local to the expression
#BUT the for loop works differently
X = 99
print([X for X in range(5)])
print('X : ', X)

Y = 99
for Y in range(5) : pass
print('Y : ', Y)




