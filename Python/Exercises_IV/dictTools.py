"Making a copy of a dictionary"

def copyDict(dict):
    keys = list(dict.keys())
    copy = {}
    for k in keys:
        copy[k] = dict[k]
    return copy

def copyDict2(dict):
    return dict.copy() #there is a standard copy function....

print(copyDict({1: 'a', 2: 'b', 3: 'luca', 4: [1,2,3]}))        
print(copyDict2({1: 'c', 2: 'd', 3: 'rita', 4: [4,5,6]}))        