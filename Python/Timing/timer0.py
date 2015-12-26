"""
another one

"""

import time
def timer(func, *args):
    start = time.clock()
    for i in range(1000): #calling function func 1000 times
        func(*args)
    return time.clock() - start

 