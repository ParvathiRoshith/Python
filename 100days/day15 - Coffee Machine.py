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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource():
    if resources['water']<MENU[prompt]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources['milk']<MENU[prompt]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif resources['coffee']<MENU[prompt]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        return "Process"
    
def check_amount():
    global profit
    if amount<MENU[prompt]["cost"]:
        return "Stop"
    elif amount>MENU[prompt]["cost"]:
        profit=profit+MENU[prompt]["cost"]
        change=round(amount-MENU[prompt]["cost"],2)
        print(f"Here is ${change} dollars in change.")
    else:
        profit=profit+amount

def deduct_resource():
    resources['water'] = resources['water'] - MENU[prompt]["ingredients"]["water"]
    resources['milk'] = resources['milk'] - MENU[prompt]["ingredients"]["milk"]
    resources['coffee'] = resources['coffee'] - MENU[prompt]["ingredients"]["coffee"]

coffee_machine_on=True
while coffee_machine_on==True:
    prompt=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt=='off':
        coffee_machine_on=False
    elif prompt=='report':
        print(f"Water: {resources["water"]}ml \n" 
              f"Milk: {resources["milk"]}ml \n" 
              f"Coffee: {resources["coffee"]}g \n"
              f"Money: ${profit}"
              )
    else:
        if check_resource()=="Process":
            print("Please insert coins.")
            q=int(input("How many quarters?: "))
            d=int(input("How many dimes?: "))
            n=int(input("How many nickles?: "))
            p=int(input("How many pennies?: "))
            amount=(q*0.25)+(d*0.10)+(n*0.05)+(p*0.01)
            if check_amount()=='Stop':
                print("Sorry that's not enough money. Money refunded.")
            else:
                deduct_resource()
                print(f"Here is your {prompt} Enjoy!")