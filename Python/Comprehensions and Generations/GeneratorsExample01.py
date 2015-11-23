#Scrambling sequences

L, S = [1,2,3], 'spam'

for i in range(len(S)): 
    S = S[1:] + S[:1]
    print(S, end=' ')
print('\n')

for i in range(len(L)): 
    L = L[1:] + L[:1]
    print( L, end=' ')
print('\n')

for i in range(len(S)): 
    X = S = S[i:] + S[:i]
    print(X, end=' ')
print('\n')

#Simple functions

def scramble(seq): #using a function
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res
print('Using a scramble function: ', scramble('spam'))

def scramble2(seq): #using list comprehension
    return [seq[i:] + seq[:i] for i in range(len(seq))]
print('Using a scramble function with list comprehension: ', scramble2('spam'))

for x in scramble2((1,2,3)):
    print(x, end=' ')
print('\n')

#Generator function

def scramble3(seq): #generator function
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq
print('Using a scramble function with generator function: ', list(scramble3('spam')))
        
def scramble4(seq): #generator function
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]
print('Using a scramble function with generator function: ', list(scramble4('spam')))
print('Using a scramble function with generator function: ', list(scramble4((1,2,3))))
for x in scramble4((1,2,3)):
                   print(x, end=' ')
print('\n')
                   
#Generator expression

S = 'spam'
G = (S[i:] + S[:i] for i in range(len(S)))
print('Using a scramble function with generator expression: ', list(G))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print('Using a scramble function with generator expression: ', list(F(S)))
print('Using a scramble function with generator expression: ', list(F([1,2,3])))

for x in F((1,2,3)):
    print(x, end=' ')
