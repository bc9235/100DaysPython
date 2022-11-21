import data


def user_order(drink):
    """Takes in customer request and selects ingredients and cost."""
    if drink == 'espresso':
        return data.MENU['espresso']
    elif drink == 'latte':
        return data.MENU['latte']
    else:
        return data.MENU['cappuccino']


def print_report():
    """Print report of resources in machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink, supplies):
    """Check if machine has enough resources to make drink."""
    if drink['ingredients']['water'] > supplies['water']:
        print("Sorry, there is not enough water.")
        return False
    elif drink['ingredients']['coffee'] > supplies['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    elif drink == 'latte' or drink == 'cappuccino':
        if drink['ingredients']['milk'] > supplies['milk']:
            print("Sorry, there is not enough milk.")
            return False
    else:
        return True


def transaction(drink, cost):
    """Ask user for coins and determine if they have enough money to proceed."""
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    cost = cost['cost']
    change = round(total - cost, 2)
    if total == cost:
        print(f"Your {drink} will be right up!")
        money += cost
        return True
    elif total > cost:
        print(f"Your change is ${change}.\nYour {drink} will be right up!")
        money += cost
        return True
    else:
        print(f"You don't have enough money for this {drink}.  Money refunded.")
        return False


def make_drink(drink, supplies):
    """Deducts supplies of making drink from resources."""
    supplies['water'] -= drink['ingredients']['water']
    supplies['coffee'] -= drink['ingredients']['coffee']
    if drink == 'latte' or drink == 'cappuccino':
        supplies['milk'] -= drink['ingredients']['milk']


resources = data.resources
money = 0
operate = True
while operate:
    request = input("What would you like? (espresso/latte/cappuccino): ")
    if request == 'report':
        print_report()
    elif request == 'off':
        operate = False
    else:
        order = user_order(request)
        can_make = check_resources(order, resources)
        if can_make:
            has_money = transaction(request, order)
            if has_money:
                make_drink(order, resources)
