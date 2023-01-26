'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''


def f1():
    print("First Function\n")


def f2(name):
    print(f"We recognise your name, thank you for tuning in {name}.")


f1()

# Information can be passed into functions as arguments.
name = input("Enter your name: ")
f2(name)
