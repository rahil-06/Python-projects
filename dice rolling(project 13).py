# print("\u25CF \u250c \u2500 \u2510 \u2502 \u2514 \u2518") #ASCII Art




dict={1:("┌──────────┐",
         "│          │",
         "│     ●    │",
         "│          │",
         "└──────────┘"),
    2:( "┌──────────┐",
        "│  ●       │",
        "│          │",
        "│       ●  │",
        "└──────────┘"),
    3:( "┌──────────┐",
        "│  ●       │",
        "│     ●    │",
        "│       ●  │",
        "└──────────┘"),
    4:( "┌──────────┐",
        "│  ●    ●  │",
        "│          │",
        "│  ●    ●  │",
        "└──────────┘"),
    5:( "┌──────────┐",
        "│  ●    ●  │",
        "│     ●    │",
        "│  ●    ●  │",
        "└──────────┘"),
    6:( "┌──────────┐",
        "│  ●    ●  │",
        "│  ●    ●  │",
        "│  ●    ●  │",
        "└──────────┘")}

import random

total=0
dice=[]
input_dice=int(input("What are the No. of dices?:"))

for die in range(input_dice):
    dice.append(random.randint(1,6))

for die in range(input_dice):
    for line in dict[dice[die]]:
        print(line)

for die in dice:
    total+=die
print(f"total is: {total}")