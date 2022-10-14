import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!= random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if(guess< x):
            print("Your guess is low!!")
        elif(guess>x):
            print("Your guess is high!!")
        else:
            print("Your guess is correct!!")
        
guess(10)