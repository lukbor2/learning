X = 1
def nester():
    X = 2 # Hides global
    print(X)
    class C:
        X = 3 
        print(X) # Local: 3
        def method1(self):
            print(X) # In enclosing def (not 3 in clas): 2
            print(self.X) # Inherited class local: 3
        def method2(self):
            X = 4
            print(X) # Local: 4
            self.X = 5 # Hides class
            print(self.X) # Located in instance: 5
    I = C()
    I.method1()
    I.method2()

print(X)
nester() # Result: 2,3,2,3,4,5
print("-"*40)