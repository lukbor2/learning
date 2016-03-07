
def countdown(x):
    if x >= 1:
        print(x)
        countdown(x-1)
    else:
        print('stop')

countdown(5)

countdown(20)
    