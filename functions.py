'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''


def f1():
    print("First Function\n")


def f2(name):
    print(f"We recognise your name, thank you for tuning in {name}.\n")

def f3(fname,lname):
    print("Your full name is "+fname+" "+lname+"\n")

f1()

# Information can be passed into functions as arguments.
name = input("Enter your name: ")
f2(name)

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
f3(fname, lname)

