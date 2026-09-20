def isPrime(y):
    if y <= 1: #by definition prime numbers are integers > 1
        print(y, ' not prime')
    else:
        x = y // 2 
        while x > 1:
            if y % x == 0:
                print(y, ' has factor ', x)
                break
            x -= 1
        else:
            print(y, ' is prime')

isPrime(13)
isPrime(13.0)
isPrime(15)
isPrime(15.0)
isPrime(0)
isPrime(1)
isPrime(-13)
isPrime(-15)