# '''

# String operation in python

# '''
# str= input("Enter any word or sentence: ")

# print("\n***OPERATIONS ON STRING***")

# #printing of string
# print(f"Your input string is: {str}")

# #printing a particular index of string
# n=int(input("Which index to print: "))
# print(f"the char on given index is : {str[n]}")

# #lenght of string
# print(f"The lenght of the string is : {len(str)}")

# #string slicing
# print("\nSLICING OF STRING:")
# print(str[1:3])
# print(str[6:])
# print(str[:6])

# #count of STRING to check if one string is present in another string
# str2= input("Enter any word or sentence for second string: ")
# common = str.count(str2)
# print(common)

# #find function to check if given string have that another string and return the index of first charactor
# common= str.find(str2)
# print("The index is : ",common)
# print("use case in printing from that index: ",str[common:])
# #return -1 if it cant find that string

# # Replace function to Replace one peice of string with another string
# str = str.replace("a","s")
# #replace all a by s
# print(f"New modified string: *{str}*")


# #upper and lower
# print(f"Lower string: {str.lower()}\nUpper string: {str.upper()}")


'''
Multi line String
'''

str = '''Hello, I am developing multi line string.
This can be done through triple quotes.
This is one of the example.
Visit the code block to get more info.
         
Follow @BANZOM'''
print(str)


# printing the string using loops
for ch in str:
    print(ch, end='')