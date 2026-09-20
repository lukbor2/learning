
#The same result can be achieved with a custom function, a filter and a list comprehension

#Using a custom function

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print('Function result: ', res)

#Using a filter

res = list(filter((lambda x: x % 2 == 0), range(5)))
print('Filter result: ', res)

#Using a list comprehension

res = [x for x in range(5) if x % 2 == 0]
print('List comprehension result: ', res)

#for loops can be nested in a list comprehension

res = [x + y for x in [0,1,2] for y in [100,200,300]]
print('List comprehension with nested loops: ', res)

#list comprehensions work on any sequence or iterable type

res = [x + y for x in 'spam' for y in 'SPAM']
print('List comprehension result: ', res)

#each nested loop can have a if clause attached

res = [(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print('List comprehension result: ', res)

#the if clauses work on strings too

res = [x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P','A')]
print('List comprehension result: ', res)

