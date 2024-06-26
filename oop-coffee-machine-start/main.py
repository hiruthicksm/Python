from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menuitem=MenuItem
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
flag=True
while flag:
    print(menu.get_items())
    option=input()
    if option=="report":
        coffee_maker.report()
        money_machine.report()
    elif option=="off":
        flag=False
    else:
        drink=menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)






