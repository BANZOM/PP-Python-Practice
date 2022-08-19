'''
For loop for printing natural numbers and its sum upto 'n' with number hop by m

'''
num= int(input("Enter a number: "))
mum= int ( input ("Enter a mum that is hopped in numbers: "))
sum=0
for i in range (1, num+1,mum):
    print(i,end=",")
    mumsum = sum+i+mum
    sum= sum + i
    
print("\nThe sum of printed numbers is :",sum)
print(f"\nThe sum of all numbers between 1 to {num} is :{mumsum} ")