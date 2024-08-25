from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    # TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_choice = input(f"What would you like to drink?: ({menu.get_items()}) ")

    # TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice.lower() == "off":
        print("Coffee machine is shutting down....")
        is_machine_on = False
    # TODO 3. Print report.
    elif user_choice.lower() == "report":
        coffeemaker.report()
        money_machine.report()
    elif user_choice.lower() == "latte" or user_choice.lower() == "espresso" or user_choice.lower() == "cappuccino":
        # drink is a MenuItem object, find_drink returns such object
        drink = menu.find_drink(user_choice)
        # is_resource_sufficient takes a MenuItem object, which is drink here
        if coffeemaker.is_resource_sufficient(drink):
            # make machine takes parameter cost which is float, here we have
            # the MenuItem object's cost, which is drink.cost
            if money_machine.make_payment(drink.cost):
                # make_coffee takes MenuItem as a parameter, here drink
                coffeemaker.make_coffee(drink)
    else:
        print("Not valid input, Try again! ")

