weight=float(input("enter your weight:"))

choice=input("The weight is in pounds or kilogram (K/P):")

if (choice=="K"):
    result=(weight)*2.205
    print(f"The weight in pounds is:{result:.4f}")

elif (choice=="P"):
    result=(weight)/2.205
    print(f"The weight in kgs is:{result:.4f}")

else:
    print("invalid choice :(")