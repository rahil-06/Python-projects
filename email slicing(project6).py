email=input("input ur email id:")
username= email[:email.index("@")]
domain=email[email.index("@")+1:]

print(f"Your username is {username} and domain is {domain}")