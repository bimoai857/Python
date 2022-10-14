import random
def guess(x):
    low=1
    high=x
    feedback=' '
    while feedback!='c':
        guess=random.randint(low,high)
        print(f"Computer has guessed: {guess}")
        print("--H/h for too high--l/L for too low--c/C for correct guess!!!")
        feedback=input("Feedback: ").lower()
        if(feedback=='l'):
            low=guess+1
        elif(feedback=='h'):
            high=guess-1
    print("Yay!! the computer has guessed you number"+ (f'{guess}')+ "correct")

guess(100)
