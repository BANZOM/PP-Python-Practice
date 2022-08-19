'''

Guessing the number game; 27 june 2022

'''
import random
import goto


label .playagian
randomnum = random.randint(7,14)
#print(randomnum)
# print("Enter a number: ");

label .agian
num=int( input ("Enter A Number: "))


if randomnum>num:
    print ("You guessed the Wrong Number, Think any greater Number.")
    goto .agian
elif randomnum<num:
    print ("You guessed the Wrong Number, Think any smaller Number.")
    goto .agian
else:
    print(f"You got the write Number. i.e: {num} ")
    
rewine = int(input("Want to play agian,Enter 9: "));
if rewine == 9:
    goto .playagian
    
    # need to complete and to learn goto statement in python


