principal=0
time=0
rate=0

while True:
    if(principal>=0):
        principal=float(input("enter your principal amount:"))
    else:
        print("principal cant be zero")

    if(rate>=0):
        rate=float(input("enter your rate:"))
    else:
        print("rate cant be lesser than 0")

    if(time>=0):
        time=int(input("enter the time in years:"))
    else:
        print("time cant be less than 0")

    break

Amount=principal*(1+rate/100)**time
print(f"The amount after {time} years is Rs.{Amount:.2f}")



