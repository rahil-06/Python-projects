menu={"pizza":200,
      "burger":100,
      "maggi":50}
total=0
cart=[]
for key,value in menu.items():
    print(f"Food:{key:10}Price{value:.2f}")

while True:
    food=input("Enter food itrmes (Q):")

    if (food=="Q"):
        break
    elif menu.get(food) is not None:
        cart.append(food)


for foods in cart:
    total+=menu.get(foods)
    print(foods,end=" ")

print()
print(f'Print total is {total}')

  



