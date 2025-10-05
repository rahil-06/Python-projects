import random

target=random.randint(1,10)


while True:
    choice=(input("Enter your choice or Quit(Q):"))
    if(choice=="Q"):
        break
    choice=int(choice)
    if (choice==target):
        print("Correct guess WOHOOO!!")
        break
    elif(choice<target):
        print("OHH NOO its a small guess,take an bigger one")
    else:
        print("OHH NOO its a big guess,take an smaller one")


print("---GAME OVERR---")
