from random import *
from string import *

Q = input("Generate Password? ")

password = ""

pchars = ascii_letters + digits

if Q == "yes" or Q == "Yes":
    for i in range(10):
        password += choice(pchars)

print(password)
        
print("No inting")
