def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    next_num = n + 1
    while True:
        if(isPrime(next_num)):
            return next_num
        next_num += 1
    

n = int(input("Enter a number: "))
print(next_prime(n))