#First example of a generator function

def gensquares(N):
    for i in range(N):
        yield i ** 2
        
for i in gensquares(5):
    print(i, end=' : ')
    
#Generators are iterables and can appear in any iteration context, such as tuples and dictionary comprehensions

def ups(line):
    for sub in line.split(','):
        yield sub.upper()

print('\nTuples: ', tuple(ups('aaa, bbb,ccc')))

print('Dictionary Comprehension: ', {i: s for (i,s) in enumerate(ups('aaa,bbb,ccc'))})