# double factoral of a given number

def double_factorial(num):
    """
    Calculates the double factorial of a given positive integer.

    Args:
        num (int): The positive integer to calculate the double factorial of.

    Returns:
        The double factorial of the given number.
    """

    if num <= 0:
        return 1
    else:
        return num * double_factorial(num - 2)


num = int(input("Enter a number: "))
print("Double factorial of", num, "is", double_factorial(num))
