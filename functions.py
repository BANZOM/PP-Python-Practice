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


# f1()

# # Information can be passed into functions as arguments.
# name = input("Enter your name: ")
# f2(name)

# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# f3(fname, lname)

# We can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
# f4(child1 = "A", child2 = "B", child3 = "C")



f5(one="Aditya", two="Adi", three="Addy", four="Aadi")
