num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

option=input("Enter the operation to be done (+,-,*,/):")



if (option=="+"):
    res=num1+num2
    print(f"Your added numbers are:{res:.2f}")
elif(option=="-"):
    if (num1>num2):
        res=num1-num2
        print(f"Your subtracted answer is:{res:.2f}")
    else:
        res=num2-num1
        print(f"Your subtracted answer is:{res:.2f}")
elif(option=="*"):
    res=num1*num2
    print(f"Your multiplied number is:{res:.2f}")
else:
    ask=input("A:num1/num2 or B:num2/num1:(A/B)")
    if (ask=="A"):
        res=(num1/num2)
        print(f"The answer is :{res:.2f}")
    else:
        res=(num2/num1)
        print(f"The answer is:{res:.2f}")
