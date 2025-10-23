import random
options=("rock",'paper','scissors')
choice=input('Enter your choice(rock/paper/scissors):').lower()
computer=random.choice(options)

def output(choice,computer):
    print(f'Your choice:{choice}')
    print(f"computer choice:{computer}")


while True:
    
    if (choice=='quit'):
        print("You have exited the game")
        break
    computer=random.choice(options)
    if (choice != computer):
        print(".... WELCOME TO ROCK PAPER SCISSORS GAME.....")
        if(choice=='rock' and computer=="scissors"):
            output(choice,computer)
            print("you win")
        elif(choice=='paper' and computer=='rock'):
            output(choice,computer)
            print("you win")
        elif(choice=='scisssors' and computer=='paper'):
            output(choice,computer)
            print("you win")
        else:
            output(choice,computer)  
            print("computer wins")
            

    elif(choice==computer):
        print('Its a tie')
    break
print("......Game Over.....")