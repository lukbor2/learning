from _functools import reduce
from math import factorial
import timeit

def factRecursive(n):
    if n > 1:
        return (factRecursive(n-1) * n)
    else:
        return 1
    
def factRecursive2(n):
    return n if n == 1 else n * factRecursive2(n-1)

def factReduce(n):
   l = list(range(1,n+1)) #I don't want the 0 in the range and I want n included 
   #print(l)
   return reduce(lambda x, y: x * y, l)
    
def factLoop(n):
    res = n
    while n > 1:
        res = res * (n-1)
        n -= 1
    return res
            
def factMath(n):
    return factorial(n)

print('Running factRecursive: ', factRecursive(6))
print('Running factRecursive2: ', factRecursive2(6))
print('Running factReduce: ', factReduce(6))
print('Running factLoop: ', factLoop(6))
print('Running math factorial: ', factMath(6))

print("Testing .... ", factRecursive(500) == factRecursive2(500) == factReduce(500) == factLoop(500) == factMath(500))

for test in (factRecursive, factRecursive2, factReduce, factLoop, factMath):
    print(test.__name__, min(timeit.repeat(stmt=lambda: test(500), repeat = 3, number = 20)))