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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def current_resources_report(resource):
    water = f"Water: {resource['water']}ml\n"
    milk = f"Milk: {resource['milk']}ml\n"
    coffee = f"Coffee: {resource['coffee']}g\n"
    money = f"Money: ${resource['money']}"
    combined_resources = water + " " + milk + " " + coffee + " " + money
    print(combined_resources)


# Calculate users change and return the remaining change based on users choice of drink
def users_change(drink_cost):
    quarter = float(input("How many quarters?: "))
    dime = float(input("How many dimes?: "))
    nickle = float(input("How many nickles?: "))
    pennie = float(input("How many pennies?: "))

    total_paid = (0.25 * quarter) + (0.1 * dime) + (0.05 * nickle) + (0.01 * pennie)
    change_left = (total_paid - drink_cost)
    return change_left


def price_compare(user_money, cost_of_drink, drink):
    if user_money >= cost_of_drink:
        updated_change = (user_money - cost_of_drink)
        print(f"Here is ${round(updated_change, 1)} in change.")
        print(f"Here is your {drink}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return updated_change


while(True):
    change = 0
    user_drink = input("What would you like? (espresso/latte/cappuccino): ")
    if user_drink.lower() == "off":
        break
    elif user_drink not in MENU:
        print("Invalid drink choice. Please try again.")
        continue
    user_drink_cost = MENU[user_drink]["cost"]
    ingredients = MENU[user_drink]["ingredients"]
    water_quantity = ingredients["water"]
    coffee_quantity = ingredients["coffee"]
    milk_quantity = ingredients["milk"]
    system_water_quantity = resources["water"]
    system_milk_quantity = resources["milk"]
    system_coffee_quantity = resources["coffee"]
    # Check if current resources equal to resources needed to make the drink
    if system_water_quantity < water_quantity:
        print("Sorry there is not enough water.")
        continue
    elif system_milk_quantity < milk_quantity:
        print("Sorry there is not enough milk")
        continue
    elif system_coffee_quantity < coffee_quantity:
        print("Sorry there is not enough coffee")
        continue
    resources["water"] -= water_quantity
    resources["milk"] -= milk_quantity
    resources["coffee"] -= milk_quantity
    print("Please insert coins.")
    change = users_change(user_drink_cost)
    resources["money"] = change
    price_compare(change, MENU[user_drink]["cost"], user_drink)


