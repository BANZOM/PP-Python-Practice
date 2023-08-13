def sum_of_factorials(n):
    factorial = 1
    sum_of_factorials = 0
    for i in range(1, n+1):
        factorial *= i
        sum_of_factorials += factorial
    return sum_of_factorials

n = int(input("Enter a number: "))
print("Sum of first",n,"factorials is", sum_of_factorials(n))