from random import *
from string import *

while True:
    try:
        lenReq = int(input("Enter required password length: "))
        if lenReq < 1:
            break
        elif lenReq > 50:
            break
    except:
        print("hmmmmmmmmmmmmmmmmmmmmmmm")

    Ques = input("Generate Password? ")

    password = ""

    pchars = ascii_letters + digits

    if Ques == "yes" or Ques == "Yes":
        for i in range(lenReq):
            password += choice(pchars)

    print(password)
    break
            
