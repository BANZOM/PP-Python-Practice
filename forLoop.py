'''
For loop for printing natural numbers and its sum upto 'n'

'''
num = int(input("Enter a number: "))
sum = 0
# range(start_from, end_comes_before, incremented_by (default is 1))
for i in range(1, num+1):
    print(i, end=" ")
    sum = sum + i
print("\nThe sum is :", sum)

print("\n")

fruits = ['apple', 'berry', 'cherry']
for item in fruits:
    print(item)
    
print("\n")

# looping through string
for c in "ABCDEFGHIJKLMOPQRSTUVWXYZ":
    print(f"{c} ", end="")
    
print("\n")
# break statements
for c in fruits:
    if c == "cherry":
        break
    print(c)
    
# for loops cannot be empty,
# "IndentationError: expected an indented block after 'for' statement on line", the error
for x in fruits:
    pass
