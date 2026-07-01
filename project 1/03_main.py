import random
computer = random.choice(["stone", "paper", "scissor"])
youstr = input("Enter your choice:")

# By now we have 2 numbers,youand computer


if(computer==youstr):
    print("Its a draw")
else:
    if(computer == "stone" and youstr == "paper"):
        print("you win!")
    elif(computer == "paper" and youstr == "stone"):
        print("You lose!")
    elif(computer == "scissor" and youstr == "paper"):
        print("you lose!")
    elif(computer == "paper" and youstr == "scissor"):
        print("you win!")
    elif(computer == "scissor" and youstr == "stone"):
        print("you win!")
    elif(computer == "stone" and youstr == "scissor"):
        print("you lose!")
    else:
        print("something went wrong!")
        