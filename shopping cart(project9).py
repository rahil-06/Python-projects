foods=[]
prices=[]    
total=0

while True:
    food=input("enter food to buy or (quit Q):")
    if (food=="Q"):
        break
    else:
        price=float(input("enter price of food:"))
        foods.append(food)
        prices.append(price)

print("---YOUR CART---")

for food in foods:
    print(food)   
    
for price in prices:
    total+=price

print(f"total is Rs.{total}")



