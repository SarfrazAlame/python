import random

computer = random.choice([1,0,-1])
you = {"s":1, "g":0, "w":-1}

yourStr = input("Enter your Choice : ")

user = you[yourStr]


if(computer == user):
    print("Match is draw")
else:
    if(computer == 1 and user==-1):
        print("You lose")
    elif(computer == 1 and user == 0):
        print("you win")
    elif(computer == 0 and user == 1):
        print("you lose")
    elif(computer == 0 and user == -1):
        print("you won")