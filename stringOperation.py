'''

String operation in python

'''
str= input("Enter any word or sentence: ")

print("\n***OPERATIONS ON STRING***")

#printing of string
print(f"Your input string is: {str}")

#printing a particular index of string
n=int(input("Which index to print: "))
print(f"the char on given index is : {str[n]}")

#lenght of string
print(f"The lenght of the string is : {len(str)}")

#string slicing
print("\nSLICING OF STRING:")
print(str[1:3])
print(str[6:])
print(str[:6])

#count of STRING to check if one string is present in another string
str2= input("Enter any word or sentence for second string: ")
common = str.count(str2)
print(common)
