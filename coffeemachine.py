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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(water, milk, coffee, coffee_type):
    if water < MENU[f'{coffee_type}']['ingredients']['water']:
        return f"Sorry there is not enough water in the machine"
    if coffee_type != "espresso":
        if milk < MENU[f'{coffee_type}']['ingredients']['milk']:
            return f"Not enough milk in the machine"
    elif coffee < MENU[f'{coffee_type}']['ingredients']['coffee']:
        return f"Not enough coffee in the machine"

machine_water = resources['water']
machine_milk = resources['milk']
machine_coffee = resources['coffee']

machine_on = True
machine_money = 0
while machine_on:

    order = input("What would you like? (espresso/latte/cappuccino) ☕ : ").lower()

    if order != "off" and order != "report":
        coffee_cost = MENU[f'{order}']['cost']
        resources = check_resource(machine_water, machine_milk, machine_coffee, order)
        if resources:
            print(resources)
        else:
            print("Please insert coins.")
            quarters_coins = int(input("how many quarters?: ")) * 0.25
            dimes_coins = int(input("how many dimes?: ")) * 0.10
            nickles_coins = int(input("how many nickles?: ")) * 0.05
            pennies_coins = int(input("how many pennies?: ")) * 0.01
            payed_amount = quarters_coins + dimes_coins + nickles_coins + pennies_coins

            if payed_amount >= coffee_cost:
                machine_money += coffee_cost
                order_change = f"{(payed_amount - coffee_cost):.2f}"
                print(f"Here is ${order_change} in change.")
                print(f"Here is your {order} ☕. Enjoy!")
                machine_water -= MENU[f'{order}']['ingredients']['water']
                machine_coffee -= MENU[f'{order}']['ingredients']['coffee']
                if order != "espresso":
                    machine_milk -= MENU[f'{order}']['ingredients']['milk']
            else:
                print(f"Sorry that's not enough money. Money refunded ${payed_amount}.")
    elif order == "off":
        machine_on = False
    elif order == "report":
        print(f"Water: {machine_water}ml\nMilk: {machine_milk}ml\nCoffee: {machine_coffee}g\nMoney: ${machine_money}")
