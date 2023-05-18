'''
check if a given number can be partitioned into two prime numbers

#A1: iterate over all possible pairs of prime numbers and check if their sum equals the given number
'''
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def isPrimePartition(n):
    P = []
    for i in range(2,n+1):
        if isPrime(i):
            P.append(i)
    
    for i in P:
        for j in P:
            if i+j == n:
                return True
    return False

num = int(input("Enter the number: "))
print(isPrimePartition(num))