#Example of a recursive function
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print('*** Calling recursive function ***')
print('Result: ', mysum([1,2,3,4,5]))

#Alternative coding using if/else ternary Expression

def mysum1(L):
    return 0 if not L else L[0] + mysum(L[1:])

print('*** Calling recursive function mysum1***')
print('Result: ', mysum1([5,6,7,8,9]))

def mysum2(L):
    return L[0] if len(L) == 1 else L[0] +mysum2(L[1:])

print('*** Calling recursive function mysum2***')
print('Result: ', mysum2([5,6,7,8,9]))

def mysum3(L):
    first, *rest = L #first takes the first value in the tuple L (because this is how it works) then the rest of the tuple is "packed"into rest
    return first if not rest else first + mysum3(rest)

print('*** Calling recursive function mysum3***')
print('Result: ', mysum3([5,6,7,8,9]))
print('Result: ', mysum3(('s','p','a','m')))


#In the example below recursion is used to handle arbitrary structures

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

print('*** Calling recursive function sumtree()***')
L= [1,[2,[3,4],5],6,[7,8]]
print('Result: ', sumtree(L))

        