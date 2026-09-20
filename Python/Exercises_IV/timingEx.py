
import sys, timer
from math import sqrt

reps = 10000
repslist =list(range(reps))

def useSqrt():
    for x in repslist:
        res = sqrt(x)
    return res

def useStar():
    for x in repslist:
        res = x ** 0.5
    return res

def usePow():
    for x in repslist:
        res = pow(x, 0.5)
    return res

print(sys.version)
for test in (useSqrt, useStar, usePow):
	(bestof, (total, result)) = timer.bestoftotal(5,1000,test)
	print('%-9s: %.5f'  % (test.__name__, bestof))
