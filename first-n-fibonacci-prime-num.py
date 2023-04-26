n = int(input("Enter a number: "))

def isPrime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True
        

f1 = 1
f2 = 1
list = []
while n-2 > 0:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if isPrime(f3):
        list.append(f3)
    n -= 1

print(list)