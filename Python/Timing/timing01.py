from timer0 import timer

time = timer(pow, 2, 1000)
print('Timing pow function: ', time)

time = timer(str.upper, 'spam')
print('Timing str.upper function: ', time)