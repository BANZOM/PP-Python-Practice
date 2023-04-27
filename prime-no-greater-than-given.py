def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nextPrime(n):
    next_num = n + 1
    if next_num % 2 == 0:
        next_num += 1
    while True:
        if isPrime(next_num):
            return next_num
        next_num += 2
    

n = int(input("Enter a number: "))
print(nextPrime(n))