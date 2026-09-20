class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3

x = Number(2)
y = Number(3)
z = Number(4)

print(x.double()) # normal immediate call

acts = [x.double, y.double, y.triple, z.double] # List of bound methods
for act in acts:
    print(act()) # call as functions