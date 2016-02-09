"Sort and print the keys of a dictionary"

D = {
     'name': 'Luca',
     'surname': 'Borghi',
     'age': 45,
     'lived in': ['Modena', 'London', 'San Francisco']
     }

k = list(D.keys())
k.sort()

for x in k:
    print(x, "=>", D[x])

"Another option to do the same thing"
for x in sorted(D.keys()):
    print(x, "=>", D[x])
    
    