from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

operate = True

while operate:
    user_order = input(f"What would you like? ({menu.get_items()}): ")
    if user_order == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_order == "off":
        operate = False
    else:
        drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
