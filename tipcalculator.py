print("Welcome to the tip calculator!")
total=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give ? 10, 12 or 15?"))
tiper=tip/100
tip_amt=tiper*float(total)
num=input('How many people to split the bill? ')
amount=float(total)+tip_amt
perp=round(float(amount)/float(num),2)
print(f"Each person should pay : {perp}")
