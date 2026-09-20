"Part a"

L = []

for x in range(6):
    L.append(2 ** x) #I could have used a map function or a list comprehension to create the list
    
" L = list(map(lambda x: 2**x, range(7))) or  [2**x for x in range(7)]"


X = 5 
i = 0

while i < len(L):
    if (2 ** X) == L[i]:
        print('at index ',i)
        break
    i += 1    
else:
    print(X, 'not found')
    
"Part b"

for x in L:
    if (2 ** X) == x:
        print('at index ', L.index(x))
        break
else:
    print(X, 'not found')
        
"Part c"

if (2 ** X) in L:
    print('at index ', L.index(2 ** X))
else:
    print(X, 'not found')

"Part e"



