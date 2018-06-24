"Print the ASCII codes of all characters in a string"
"Then print the sum of the ASCII codes"
"Then build a list with the ASCII codes"

s = 'luca'
tot = 0
l = []

for x in s:
    print("Character %s has ASCII code = %d" % (x, ord(x)))
    tot += ord(x)
    l.append(ord(x))

print("Sum of ASCII codes = %d" %(tot))
print("List of ASCII codes: %s"  %(l))

"Alternative 1 - Using list compositions to build the list"
l2 = [ord(c) for c in s] 
print("List of ASCII codes: %s"  %(l2))


"Alternative 2 - Using list map to build the list"
l3 = list(map(ord, s))
print("List of ASCII codes: %s"  %(l3))
