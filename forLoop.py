'''
For loop for printing natural numbers and its sum upto 'n'

'''
num= int(input("Enter a number: "))
sum=0
for i in range (1, num+1):
    print(i,end=" ")
    sum= sum + i
print("\nThe sum is :",sum)


fruits = ['apple', 'berry', 'cherry']
for item in fruits:
    print(item);
    
# looping through string
for c in "ABCDEFGHIJKLMOPQRSTUVWXYZ":
    print(f"{c} ",end="");