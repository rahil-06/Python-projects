import string
import random

chars=string.punctuation+string.digits+string.ascii_letters
abc=list(chars)

pas=input("enter your password to encrypt: ")
xyz=len(pas)
new_pas=""

i=0
while i<=xyz:
    ble=random.choice(abc)
    mcbc=new_pas.__add__(ble)
    i+=1
    new_pas=mcbc

print(new_pas)
