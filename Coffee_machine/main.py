MENU = {
    "espresso": {
        "ingridents": {
            "water": 50,
            "coffee": 18,
    },
    "cost": 1.5,
    },
    "latte": {
        "ingridents": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
    "cost": 2.5,
    },
    "cappuccino":{
        "ingridents":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
    "cost": 3.0,
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

def is_sufficient(order_ingrident):
    """ Checks weather the ingridents for the given order is sufficient"""
    for item in order_ingrident:
        if order_ingrident[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def is_transaction_sucessful(money_recieved, drink_cost):
    """Processes coins and returns total"""
    if money_recieved > drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"You have {change}")
        global profit
        profit+= drink_cost
        return True
    else:
        print("Sorry the money is not enough, Money refunded")
        return False

def make_coffee(drink_name, order_ingridents):
    """serves order"""
    for item in order_ingridents:
        resources[item] -= order_ingridents[item]
    print(f"Here is your {drink_name} Enjoy.")




machine_on = True
while machine_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if  choice == "off":
        machine_on = False
    elif choice== "report":
        print(f"Water {resources['water']} ml")
        print(f"milk {resources['milk']} ml")
        print(f"coffee {resources['coffee']} g")
        print(f"Profit {profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingridents']):
            payment = int(input("Money: "))
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(choice, drink["ingridents"])
