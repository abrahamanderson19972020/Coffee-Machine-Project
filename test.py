from menu import MENU, resources


def choice(want):
    try:
        drink = MENU[want]
        return drink
    except:
        print("Enter a valid input!(espresso/latte/cappuccino)")


def total_money():
    print("Please insert coin...")
    quarter_count = int(input("How many quarters >>>"))
    dime_count = int(input("How many dimes >>>"))
    nickel_count = int(input("How many nickels >>>"))
    penny_count = int(input("How many pennies >>>"))
    count = quarter_count * 25 + dime_count * 10 + nickel_count * 5 + penny_count * 1
    return count / 100


def compare(money, cost, drink, emoji):
    if money > cost:
        print(f"Here is ${money - cost} in change")
        print(f"Here is your {drink} {emoji} . Enjoy!")
    elif money == cost:
        print(f"Your money is enough to buy {drink}.")
        print(f"Here is your {drink} {emoji} . Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return


def resource_checker(drink, resource, ingredient):
    if drink == "espresso":
        if resource["water"] >= ingredient["water"] and resource["coffee"] >= ingredient["coffee"]:
            ingredient["water"] = resource["water"] - ingredient["water"]
            ingredient["coffee"] = resource["coffee"] - ingredient["coffee"]
            return ingredient
        else:
            print("Sorry, There is not enough resources. PLease add fill resources !")
            return False
    else:
        if resource["water"] >= ingredient["water"] and resource["coffee"] >= ingredient["coffee"] and resource[
            "milk"] >= ingredient["milk"]:
            ingredient["water"] = resource["water"] - ingredient["water"]
            ingredient["coffee"] = resource["coffee"] - ingredient["coffee"]
            ingredient["milk"] = resource["milk"] - ingredient["milk"]
            return ingredient
        else:
            print("Sorry, There is not enough resources. PLease add fill resources !")
            return False


def coffee_machine():
    resource = resources
    emoji = '☕'
    is_continue = True
    while is_continue == True:
        user_order = input("What would you like? (espresso/latte/cappuccino) or 'report' or 'off' to stop machine>>>")
        if user_order.lower() == "off":
            is_continue = False
        else:
            drink = user_order
            desire = choice(drink)
            cost = desire['cost']
            ingredient = desire['ingredients']
            print(f"The machine has {resource}")
            print(f"Your desire drink {drink} requires these ingredients {ingredient}")
            result = resource_checker(drink, resource, ingredient)
            if result == False:
                print("Sorry, There is not enough resources. PLease add fill resources !")
                is_continue = False
            else:
                resource = result
                print(f"Your desire drink {drink} costs ${cost}")
                money = total_money()
                print(f"You have ${money}")
                compare(money, cost, drink, emoji)
                print(f"The resource the machine has {resource}")


def main():
    coffee_machine()


if __name__ == "__main__":
    main()