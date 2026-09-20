
def adder(*args):
    result = args[0]
    for x in args[1:]:
        result += x
    return result

print(adder(1,2,3))
print(adder(2,2,2,2,2))
print(adder('molta', 'cacca','da','fare'))
print(adder([1,2,3],[4,5,6],[7,8,9]))

# print(adder(1,'luca')) this does NOT work. Can not add different types
        