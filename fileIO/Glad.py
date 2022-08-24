'''

Writing appriciation into a file

'''

F = open("sample.txt" , "wb")
name= (input("Enter Your Name: "))
name=name.capitalize()


glad = '''Thank you so much for all your assistance. Your help and insight were greatly appreciated as we stepped through the process.
I'm so glad to have you. In the time you have been here, you have helped me to make things run smoothly and made our organization more efficient.
I genuinely appreciate your willingness for wherever is needed. This kind of flexibility and dedication will help me to grow to my full potential.

Sincerely,

Aditya
'''


F.write(bytearray (f"Dear {name},\n", "UTF-8"))
F = open("sample.txt" , "ab")


F.write(bytearray(f"{glad}", "UTF-8"))
F.close()
print("We have something for you in the file named as %s"%(F.name))