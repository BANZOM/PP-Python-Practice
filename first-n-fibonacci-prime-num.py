import math


def isPrime(n):
    if n <= 1:
        return False
    x = int(math.sqrt(n))+1
    for i in range(2, x):
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
f1 = 0
f2 = 1
fibonacci_primes = []

while n > 1:
    if isPrime(f2):
        fibonacci_primes.append(f2)
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    n -= 1

print(fibonacci_primes)
