#Iterations and Comprehension
import math

def forLoop(l):
   res = []
   for x in l:
       res.append(math.sqrt(x))
   return res


l = [2,4,9,16,25]

print('Running forLoop ', forLoop(l))

print('Running map function ', list(map(math.sqrt, l)))

print('Running list comprehension ', [math.sqrt(x) for x in l])

print('Running generator expression ', list((math.sqrt(x) for x in l)))
