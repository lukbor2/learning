import manynames

X = 66
print(X) #66 global
print(manynames.X) #11, global becomes attribute after import

manynames.f() #11
manynames.g() #22

print(manynames.C.X) #33
I = manynames.C()
print(I.X) #33 still from class
I.m()
print(I.X) #55




