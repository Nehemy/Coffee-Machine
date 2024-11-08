from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

machine_on = True

while machine_on:
    order = input(f"What would you like? ({menu_list.get_items()}) ☕ : ").lower()
    if order != "off" and order != "report":
        coffee_order = menu_list.find_drink(order)
        coffee_order_name = coffee_order.name
        coffee_order_cost = coffee_order.cost
        coffee_order_ingredients = coffee_order.ingredients

        if coffee.is_resource_sufficient(coffee_order):
            # coins = int(input("Input the coins"))
            money.make_payment(coffee_order_cost)
            coffee.make_coffee(coffee_order)
    elif order == "off":
        machine_on = False
    elif order == "report":
        coffee.report()
        money.report()