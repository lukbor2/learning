X = 11 #global in module

def g1():
    print(X) # 11, reference to global

def g2():
    global X
    X = 22 #Change global in module

def h1():
    X = 33
    def nested():
        print(X) #33, reference local
    nested()

def h2():
    X = 33
    def nested():
        nonlocal X #Python 3.x only
        X = 44 #Change local
        print(X)
    nested()
        

if __name__ == '__main__':
    g1()
    g2()
    g1()
    h1()
    h2()
    