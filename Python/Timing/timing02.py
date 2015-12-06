import timer

t = timer.total(1000, pow, 2, 1000)[0]
print("Total time to run pow function: ", t)

t = timer.total(1000, str.upper, 'spam')
print("Total time to run str function: ", t)


t = timer.bestof(1000,pow, 2, 1000000)[0] 
print("Bestof pow function: ", t)

t = timer.bestof(1000, str.upper, 'spam')
print("Bestof str function: ", t)

t = timer.bestof(50, timer.total, 1000, str.upper, 'spam')
print("Bestoftotal str function: ", t)

t = timer.bestoftotal(50, 1000, str.upper, 'spam')
print("Bestoftotal str function: ", t)