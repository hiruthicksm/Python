MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
image="☕️"
def coin_calc(quarters,dimes,nickles,pennies):
    amount=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return amount
water=300
milk=200
coffee=100
money=0
def printreport(water,milk,coffee,money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}gm")
    print(f"Money: ${money}")
def game(water,milk,coffee,money):
    #resources
   flag=True
   while flag:
        choice=input("What would you like? (espresso/latte/cappuccino): ")
        if choice=="report":
            printreport(water,milk,coffee,money)

        if choice=="off":
            flag=False
        if choice=="latte" or choice=="espresso" or choice=="cappuccino":
            selected = MENU[choice]
            ing = selected['ingredients']
            if water<ing['water']:
                print("Sorry there is not enough water.")
                game(water,milk,coffee,money)
            if milk<ing['milk']:
                print("Sorry there is not enough milk.")
                game(water,milk,coffee,money)
            if coffee<ing['coffee']:
                print("Sorry there is not enough coffee.")
                game(water,milk,coffee,money)

            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))

            total = coin_calc(quarters, dimes, nickles, pennies)
            amt = selected['cost']
            balance = round(total - amt, 2)
            print(f"Here is your ${balance} in change.")
            money = money + amt

            if total < amt:
                print("Sorry that's not enough money. ")
                game(water, milk, coffee, money)

            print(f"Here is your {choice} {image}.Enjoy!")

            water = water - ing['water']
            milk = milk - ing['milk']
            coffee = coffee - ing['coffee']
game(water,milk,coffee,money)
