import random

def game():
    user=input("What's your choice? 'r' for rock 'p' for paper and 's' for scissor!! :")
    computer=random.choice(['r','p','s'])

    if(user==computer):
        return "'It's a tie!!!"
    if(user=='r' and computer=='s') or (user=='p' and computer=='r') or (user=='s' and computer=='p'):
        return "You've won!!!!"
    return "You've Lost!!!"

print(game())