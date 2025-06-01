import random

# choose a random number between 0,1,-1
comp=random.choice([1,0,-1])

#enter s for snake, w for water, g for gun
choice = input("Enter your choice(s,w,g) : ")

#Assign numerical values: 1 for snake, -1 for water and 0 for gun
choiceDict={"s":1,"w":-1,"g":0}

#reverseDict helps in retrieving strings from numerical values
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

#num holds the numerical value associated to your choice
num=choiceDict[choice]

#Display the choices of the player and the computer
print(f"You chose {reverseDict[num]}\nComputer chose {reverseDict[comp]}")

#draw condition
if(comp==num):
    print("It's a Draw!")
else:
    #losing conditions
    if(comp==1 and num == -1):
        print("You lose!")
    elif(comp==-1 and num == 0):
        print("You lose!")
    elif(comp==0 and num == 1):
        print("You lose!")
    #winning condition
    elif(comp==1 and num == 0):
        print("You win!")
    elif(comp==-1 and num == 1):
        print("You win!")
    elif(comp==0 and num == -1):
        print("You win!")
    else:
        ("An error occurred")
