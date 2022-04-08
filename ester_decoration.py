customers = int(input())

basket_price = 1.50
wreath_price = 3.80
chocolate_bunny_price = 7
decoration = 0
item_price = 0
money_per_customer = 0

for customer in range(1, customers + 1):
    command = input()
    while command != "Finish":
        if command == "basket":
            decoration += 1
            item_price += basket_price

        elif command == "wreath":
            decoration += 1
            item_price += wreath_price

        elif command == "chocolate bunny":
            decoration += 1
            item_price += chocolate_bunny_price

        command = input()
        if command == "Finish":
            if decoration % 2 == 0:
                item_price = item_price - item_price * 0.2
            money_per_customer += item_price
            print(f"You purchased {decoration} items for {item_price:.2f} leva.")
    item_price = 0
    decoration = 0


average_bill = money_per_customer / customers

print(f"Average bill per client is: {average_bill:.2f} leva.")