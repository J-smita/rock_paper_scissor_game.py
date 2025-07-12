print("             ROCK🪨 -PAPER📃-SCISSOR✂️  GAME")

import random
a = ["Rock", "Paper", "Scissor"]
computer = random.choice(a).lower()

while True:

    b = input("What do you want to take?\n1)Rock\n2)Paper\n3)Scissor\n4)EXIT\n(r or p or s or e)\n--> ").lower()

    print("Computer has taken: ",computer.capitalize())

    if(b=="e"):
        print("OK👍\nyou can exit🚪")
        break

    elif(computer=="rock" and b=="r"):
        print("DRAW🤝\n\n")

    elif(computer=="paper" and b=="p"):
        print("DRAW🤝\n\n")

    elif(computer=="scissor" and b=="s"):
        print("DRAW🤝\n\n")

    elif(computer=="rock" and b=="p"):
        print("You are winner🥳\n\n")

    elif(computer=="rock" and b=="s"):
        print("Computer is winner💻\n\n")

    elif(computer=="paper" and b=="r"):
        print("Computer is winner💻\n\n")

    elif(computer=="paper" and b=="s"):
        print("You are winner🥳\n\n")

    elif(computer=="scissor" and b=="r"):
        print("You are winner🥳\n\n")

    elif(computer=="scissor" and b=="p"):
        print("Computer is winner💻\n\n")
        
    else:
        print("Wrong input❌\n\n")
    
