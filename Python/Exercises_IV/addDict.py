"Union of two dictionaries"

"Version 1.0"
def addDict(dict1, dict2):
    keys = list(dict1.keys())
    union = {}
    for k in keys:
        union[k] = dict1[k]
    keys = list(dict2.keys())
    for k in keys:
       if k not in union.keys():
           union[k] = dict2[k] 
    return union

"Version 1.1"

def addDict2(dict1, dict2):
    keys = list(set(list(dict1.keys()) + list(dict2.keys())))
    print('Keys with no duplicates: ', keys)
    union = {}
    for k in keys:
        if k in list(dict1.keys()):
             union[k] = dict1[k]
        else:
            union[k] = dict2[k]
    return union

"Version 1.2 - using standard functions and testing whether the arguments are dict or list"

def addDict3(a1, a2):
    if type(a1) == type(a2) and type(a1) == dict:
        union = a1.copy() 
        union.update(a2)
        return union
    else:
        if type(a1) == type(a2) and type(a1) == list:
            return a1 + a2
    
print(addDict({1: 'a', 2: 'b', 3: 'luca', 4: [1,2,3]}, {1: 'rita', 'one': 'uno', 'two': 'due'}))        
print(addDict2({1: 'a', 2: 'b', 3: 'luca', 4: [1,2,3]}, {1: 'rita', 'one': 'uno', 'two': 'due'}))        
print(addDict3({1: 'a', 2: 'b', 3: 'luca', 4: [1,2,3]}, {1: 'rita', 'one': 'uno', 'two': 'due'}))        
print(addDict3([1,2,3,4], ['a','b', 'c']))        