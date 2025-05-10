MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource():
    if resources['water']>=MENU[prompt]["ingredients"]["water"]

coffee_machine_on=True
while coffee_machine_on==True:
    prompt=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt=='off':
        coffee_machine_on=False
    elif prompt=='report':
        print(f"Water: {resources["water"]} \n" 
              f"Milk: {resources["milk"]} \n" 
              f"Coffee: {resources["coffee"]} \n"
              f"Money: {profit}"
              )
    #else:
        