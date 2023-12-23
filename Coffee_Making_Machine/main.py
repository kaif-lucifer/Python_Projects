MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0

resources = {
    "water": 300,  # You can increase 
    "milk": 200,  # these amounts as per the capacity
    "coffee": 100,   # of your coffee machine
}


# TODO: 0 Print report of  coffee machine resources
def check_resources():
    print(
        f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ₹{profit}")


# TODO: 1 To check sufficiency of resources
def is_resources_sufficient(drink):
    drink_ingredients = drink['ingredients']
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 2 To take users coins in the Coffee machine
def process_coins():
    cash = int(input("Please insert coins\nHow many ₹20 coins? : ")) * 20
    cash += int(input("How many ₹10 coins? : ")) * 10
    cash += int(input("How many ₹5 coins? : ")) * 5
    cash += int(input("How many ₹2 coins? : ")) * 2
    return cash


# TODO: 3 To check whether transaction is successful or not
def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        profit += drink_cost
        change = money_received - drink_cost
        print(f"Here is your change ₹{change} ")
        return True


# TODO: 4 To make coffee making function
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy your drink!!")


# Main function loop starts here
is_on = True
while is_on:
    input_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if input_choice == "report":
        check_resources()
    elif input_choice == "off":
        is_on = False
    else:
        order = MENU[input_choice]
        if is_resources_sufficient(order):
            payment = process_coins()
            if is_transaction_successful(payment, order['cost']):
                make_coffee(input_choice, order['ingredients'])
