def action2():
    print (1 + []) # Generate TypeError

def action1():
    try:
        action2()
    except TypeError:
        print ('Inner try')

try:
    action1()
except TypeError:
    print ('Outer try')