#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let=int(input("How many letters would you like in your password?\n"))
sym=int(input("How many symbols would you like?\n"))
num=int(input("How many numbers would you like?\n"))
password=[]
for i in range(1,let):
  x=random.choice(letters)
  password.append(x)
  

for i in range(0,sym):
 y=random.choice(symbols)
 password.append(y)

for i in range(0,num):
 z=random.choice(numbers)
 password.append(z)

random.shuffle(password)

newpass=""
for i in password:
  newpass=newpass+i
print(f"Your password is {newpass}")
    

