'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''


def f1():
    print("First Function\n")


def f2(name):
    print(f"We recognise your name, thank you for tuning in {name}.\n")


def f3(fname, lname):
    print("Your full name is "+fname+" "+lname+"\n")


def f4(child3, child2, child1):
    print("The youngest child is " + child3+"\n")


def f5(**name):
    i = 1
    for key in name.keys():
        print(f"{i}. {name[key]}")
        i += 1
    print()


def f6(num=10):
    print(num)


def f7(list):
    for item in list:
        print(item)
    print()


f1()

# Information can be passed into functions as arguments.
name = input("Enter your name: ")
f2(name)

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
f3(fname, lname)

# We can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
f4(child1="A", child2="B", child3="C")


# If we don't know how many keyword arguments that will be passed into your function, adding ** before the parameter name solves that problem
# This way the function will receive a dictionary of arguments, and can be accessed.
# Arbitrary Kword Arguments
f5(one="Aditya", two="Adi", three="Addy", four="Aadi")

# Default Parameter Value is helpful when no argument is passes to a function
f6()
f6(100)
print()

# Passing any list to a function
L = ['one', 'two', 'three', 'four', 'five']
f7(L)
