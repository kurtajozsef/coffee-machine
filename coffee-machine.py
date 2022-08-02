from helper import *

resources = {
    "Water": [
        300,
        "ml"
    ],
    "Milk": [
        100,
        "ml"
    ],
    "Coffee": [
        200,
        "g"
    ],
}


def report():
    for resource in resources:
        print(f"{resource} : {resources[resource][0]}{resources[resource][1]}")


def check_resources(beverage):
    recipe = recipes[beverage]
    for r in recipe:
        if resources[r][0] < recipe[r]:
            print(f"Machine doesn't have enough {r}")
            return False
    return True


def prepare_beverage(beverage):
    global resources
    for r in recipes[beverage]:
        resources[r][0] -= recipes[beverage][r]


def give_change(amount_given, amount_taken):
    print(f"You got back change ${amount_given - amount_taken}")


def make_beverage(beverage):
    amount = get_money(beverage)
    if amount < costs[beverage]:
        print(f"You gave {amount}, that's not enough.")
        return
    if not check_resources(beverage):
        return
    prepare_beverage(beverage)
    give_change(amount, costs[beverage])
    print(f"Here's your {beverage}!")


def get_money(beverage):
    total = 0
    print(f"You chose {beverage}, it costs ${costs[beverage]}.")
    for m in money:
        amount = int(input(f"{m}: "))
        total += money[m] * amount
    return total


def prompt():
    """Prompt user to select from options"""
    user_input = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_input == "off":
        return False
    elif user_input == "report":
        report()
        return True
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        make_beverage(user_input)
        return True
    else:
        print("Invalid input, try again")
        return False


retry = True
while retry:
    result = prompt()
    if not result:
        break
