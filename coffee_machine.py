coffee_type = input()
sugar = input()
number_of_drinks = int(input())

price = 0

if coffee_type == "Espresso":
    if sugar == "Without":
        price = (number_of_drinks * 0.90) * 0.65
    elif sugar == "Normal":
        price = number_of_drinks * 1
    elif sugar == "Extra":
        price = number_of_drinks * 1.20
    if number_of_drinks >= 5:
        price *= 0.75
elif coffee_type == "Cappuccino":
    if sugar == "Without":
        price = (number_of_drinks * 1) * 0.65
    elif sugar == "Normal":
        price = number_of_drinks * 1.20
    elif sugar == "Extra":
        price = number_of_drinks * 1.60
elif coffee_type == "Tea":
    if sugar == "Without":
        price = (number_of_drinks * 0.50) * 0.65
    elif sugar == "Normal":
        price = number_of_drinks * 0.60
    elif sugar == "Extra":
        price = number_of_drinks * 0.70

if price <= 15:
    print(f"You bought {number_of_drinks} cups of {coffee_type} for {price:.2f} lv.")
else:
    price *= 0.8
    print(f"You bought {number_of_drinks} cups of {coffee_type} for {price:.2f} lv.")
