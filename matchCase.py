#The match case statement in Python is more powerful and allows for more complicated pattern matching. 

# Basic Implementation, 25, Jan, 2k23

x = input("Type Something: ")
match x:
    case "Hello":
        print("Hi")
    case "Hi":
        print("Hello")
    case other:
        print("Thank You!")
        
# This can be the alternate of if-elif-else statements