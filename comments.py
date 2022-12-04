# A comment is a part of the coding file that the programmer does not want to execute,
# rather the programmer uses it to either explain a block of code or to avoid the execution
# of a specific part of code while testing.

# this is a single line comment.

'''
This is a multi line comment.
    """
    This is also a multi line comment
    """
'''

"""
\n is a escape sequence character 
"""
'''
print("Here I'm developing this "code block"")

print("Here I'm developing this "code block"")                                ^
SyntaxError: invalid syntax
'''

# Valid line
print("Here I'm developing this \"code block\"")

# Printing multiple values in print
print("hello",5,8,6,"world")

# Using seperator
print("hello",5,8,6,"world", sep='')
print("hello",5,8,6,"world", sep='*')
print("hello",5,8,6,"world", sep='-')
# hello586world
# hello*5*8*6*world
# hello-5-8-6-world


# using end
print("hello",5,8,6,"world", sep='',end='+')
print("hello",5,8,6,"world", sep='*',end='|')
print("hello",5,8,6,"world", sep='-',end='=\n')
# hello586world+hello*5*8*6*world|hello-5-8-6-world=