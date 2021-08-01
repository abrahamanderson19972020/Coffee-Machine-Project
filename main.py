from menu import MENU, resources

resource = resources
profit = 0
emoji = '☕'

def is_enough_resource(ingredients):
    for item in ingredients:
        if ingredients[item] >= resource[item]:
            print(f"Sorry there is not enough {item}")
            return False
    else:
        return True


def total_money():
    print("Please insert coin...")
    quarter_count = int(input("How many quarters >>>"))
    dime_count = int(input("How many dimes >>>"))
    nickel_count = int(input("How many nickels >>>"))
    penny_count = int(input("How many pennies >>>"))
    count = quarter_count * 0.25 + dime_count * 0.1 + nickel_count * 0.05 + penny_count * 0.01
    return count


def is_transaction_enough(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit = drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resource[item] -= ingredients[item]
    print(f"Here is your {drink_name} {emoji} . Enjoy!")

def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "rapport":
            print(f"Water: {resource['water']} ml")
            print(f"Milk: {resource['milk']} ml")
            print(f"Coffee: {resource['coffee']} g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choice]
            is_enough_resource(drink["ingredients"])
            payment = total_money()
            if is_transaction_enough(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])




if __name__ == "__main__":
    main()