import random
import string



char=string.digits
password=""

while True:
    permission=input("Do u want to generate an random password?(Y/N) :")
    if (permission=="N"):
        break
    if (permission=="Y"):
        pass_n=int(input("Input your random password's length:"))
        for i in range(pass_n):
            abc=random.choice(char)
            password += abc
        print(f"your random password is : {password}")
        break
    




