import math

def isPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n

def isFibonacci(n):
    if isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4):
        return True
    else:
        return False

n = int(input("No. of tests: "))
ans = []
while n > 0:
    element = int(input("Enter a number: "))
    if isFibonacci(element):
        ans.append(1)
    else: ans.append(0)
    n -= 1

print(ans)