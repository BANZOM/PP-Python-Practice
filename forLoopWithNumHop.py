'''
For loop for printing natural numbers and its sum upto 'n' with number hop by m

'''
from typing import DefaultDict


def suum(a,b): #for sum of number in range
    sum=0
    for i in range(a,b+1):
        sum= sum+i
    return sum;
    
num= int(input("Enter a number: "))
mum= int ( input ("Enter a mum that is hopped in numbers: "))
sum=0
for i in range (1, num+1,mum):
    print(i,end=" ")
    sum= sum + i
mumsum = suum(1,num)
print("\nThe sum of printed numbers is :",sum)
print(f"The sum of all numbers between 1 to {num} is :{mumsum} ")  
