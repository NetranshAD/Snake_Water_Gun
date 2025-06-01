import random

#computer chooses a random number between 1,0,-1
comp=random.choice([1,0,-1])

#Player enters the choice: r for rock, p for paper and s for scissors 
choice = input("Enter your choice(r,p,s) : ")

#numerical values are assigned: 1 for rock,-1 for paper and 0 for scissors
choiceDict={"r":1,"p":-1,"s":0}

#reverseDict helps in retrieving strings from numerical values
reverseDict={1:"Rock",-1:"Paper",0:"Scissors"}

#num holds the numerical value associated to your choice
num=choiceDict[choice]

#Display the choices of the player and the computer
print(f"You chose {reverseDict[num]}\nComputer chose {reverseDict[comp]}")

#draw condition
if(comp==num):
    print("It's a Draw!")
    
    
else:
    #winning condition
    if(comp==1 and num == -1):
        print("You Win!")
    elif(comp==-1 and num == 0):
        print("You Win!")
    elif(comp==0 and num == 1):
        print("You Win!")
        
    #losing condition
    elif(comp==1 and num == 0):
        print("You Lose!")
    elif(comp==-1 and num == 1):
        print("You Lose!")
    elif(comp==0 and num == -1):
        print("You Lose!")
        
    #error condition
    else:
        ("An error occurred")
