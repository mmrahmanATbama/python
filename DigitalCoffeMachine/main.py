# Program requirement
# TODO1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# TODO2: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# TODO3: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
import menu

MENU = menu.MENU
resources = menu.resources
money_accumulated = 0


def print_report():
    global resources
    global money_accumulated
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: {money_accumulated} ml")


def get_user_input():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'off':
            quit()
        elif user_choice == 'report':
            print_report()
        elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
            can_dispense = is_enough_condiments(user_choice)
            if can_dispense:
                collected_bill = float(process_coin(user_choice))
                if transaction(collected_bill, user_choice):
                    make_coffee(user_choice)
        else:
            print("Invalid input")


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def is_enough_condiments(coffee_requested):
    global resources
    global MENU
    ingredient_needed = MENU[coffee_requested]["ingredients"]

    for keys in ingredient_needed:
        if resources[keys] < ingredient_needed[keys]:
            print(f"Sorry not enough {keys}")
            return False

    return True


# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coin(coffee_requested):
    global MENU
    cost_of_coffee = MENU[coffee_requested]['cost']
    print(f"Cost of {coffee_requested}: {cost_of_coffee}")
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dime: "))
    nickel = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    total = quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + pennies * 0.01

    return "{:.2f}".format(total)


# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
def transaction(bill, coffee_selected):
    global money_accumulated
    coffee_cost = float(MENU[coffee_selected]['cost'])

    if bill < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if bill > coffee_cost:
        money_returned = round((bill - coffee_cost), 2)
        print(f"Here is ${money_returned} dollars in change.")

    money_accumulated = money_accumulated + coffee_cost
    return True


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
def make_coffee(coffee_wanted):
    global MENU
    global resources
    coffee_selected = MENU[coffee_wanted]['ingredients']
    print_report()
    for keys in coffee_selected:
        resources[keys] = resources[keys] - coffee_selected[keys]
    print(f"Here is your {coffee_wanted}. Enjoy!")
    print_report()


get_user_input()
