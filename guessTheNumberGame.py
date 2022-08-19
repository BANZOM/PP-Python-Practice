'''

Guessing the number game; 27 june 2022

Goto statements are not worth it. it create a spaghetti code.

'''
import random

randomnum = random.randint(1,100)

while True:
    num= int(input("Enter guessed number: "))
    if randomnum>num:
        print ("You guessed the Wrong Number, Think any greater Number.")
    elif randomnum<num:
        print ("You guessed the Wrong Number, Think any smaller Number.")
    else:
        print(f"You got the write Number. i.e: {num} ")
        break

print("THANK YOU, EXECUTE THE CODE AGAIN TO PLAY ONCE MORE")
