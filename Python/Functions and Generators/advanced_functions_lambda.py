#Simple lambda

f = lambda x,y,z: x + y + z
print('Simpla lambda result', f(2,3,4))

#Defaults work like with def

x = (lambda a='fee', b='fie', c='foe': a+b+c)
print('Lambda with defaults', x('wee'))

#Scope in lambda functions

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights()
msg = act('Robin')
print('Scope in lambda functions: ', msg)

#Lambda are used in lists or dictionaries of actions

L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

print('Lambda in lists of actions')

for f in L:
    print(f(2))
    
#Nested lambdas

print('Nested lambda')
def action(x):
    return (lambda y: x+y) #the lambda function has access to x

act = action(99)
print(act(2))