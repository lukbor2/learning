"First version just adding three arguments with keywords and default values"

def adder(good = 'one', bad = 'two', ugly = 'three'):
   return good + bad + ugly

print(adder('luca','rita','lorenzo'))
print(adder('luca','rita'))
print(adder('luca'))
print(adder())

print(adder(good='franca', bad = 'gianni'))

"Second version accepting any number of keywords arguments"

def adder2(**args):
    keys = list(args.keys())
    result = args[keys[0]]
    for k in keys[1:]:
       result += args[k]
    return result
    
print(adder2(good= 'this',bad = 'is',ugly = 'very', something = 'good'))
print(adder2( a = 1, b = 2, c = 3))