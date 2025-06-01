import random
comp=random.choice([1,0,-1])
choice = input("Enter your choice(s,w,g) : ")
choiceDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
num=choiceDict[choice]
print(f"You chose {reverseDict[num]}\nComputer chose {reverseDict[comp]}")
if(comp==num):
    print("It's a Draw!")
else:
    if(comp==1 and num == -1):
        print("You lose!")
    elif(comp==1 and num == 0):
        print("You win!")
    elif(comp==-1 and num == 0):
        print("You lose!")
    elif(comp==-1 and num == 1):
        print("You win!")
    elif(comp==0 and num == -1):
        print("You win!")
    elif(comp==0 and num == 1):
        print("You lose!")
    else:
        ("An error occurred")
