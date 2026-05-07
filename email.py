import re
name=input("Enter Name: ")
email=input("Enter Email: ")
phone=input("Enter Phone Number: ")
password=input("Enter Password: ")
if email.endswith("@gmail.com"):
    print("Valid Email")
else:
    print("Invalid Email")
digits=re.findall("[0-9]",phone)
if len(phone)==10 and len(digits)==10:
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
small=re.findall("[a-z]",password)
capital=re.findall("[A-Z]",password)
digit=re.findall("[0-9]",password)
special=re.findall("[!@#$%^&*:~]",password)
if small!=[] and capital!=[] and digit!=[] and special!=[]:
    print("Valid Password")
else:
    if small==[]:
        print("Password must contain small letter")
    if capital==[]:
        print("Password must contain capital letter")
    if digit==[]:
        print("Password must contain numeric digit")
    if special==[]:
        print("Password must contain special character (!@#$%^&*:~)")
if email.endswith("@gmail.com") and len(phone)==10 and len(digits)==10 and small!=[] and capital!=[] and digit!=[] and special!=[]:
    print("All Details are Valid")
else:
    print("Details are Invalid")
