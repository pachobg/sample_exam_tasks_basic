budget = float(input())

product_number = 0
total_bill = 0
budget_ends = False

product_name = input()
product_price = float(input())


while product_name != "Stop":

    product_number += 1
    if product_number % 3 == 0:
        product_price /= 2
        budget -= product_price
        total_bill += product_price
        if budget < product_price:
            product_number -= 1
            budget_ends = True
            break
    else:
        if budget < product_price:
            budget_ends = True
            break
        budget -= product_price
        total_bill += product_price
    product_name = input()
    if product_name == "Stop":
        break
    product_price = float(input())


if budget_ends:
    difference = product_price - budget
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
else:
    print(f"You bought {product_number} products for {total_bill:.2f} leva.")