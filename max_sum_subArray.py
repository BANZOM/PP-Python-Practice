# Given an integer array, find the subarray with the largest sum, and return its sum.

array = []
n = int(input("Enter the number of elements: "))

# input the list 
for i in range(0, n):
    ele = int(input())
    array.append(ele) 


minSum = 0
maxSum = array[0]
for i in range (len(array)):
    minSum= minSum + array[i]
    if minSum > maxSum:
        maxSum = minSum
    if minSum < 0:
        minSum = 0

print("The Max Sum of subArray = ", maxSum)