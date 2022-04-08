fruit = input()
set_size = input()
number_of_sets = int(input())

price = 0

if fruit == "Watermelon":
    if set_size == "small":
        price = (number_of_sets * 2) * 56
    elif set_size == "big":
        price = (number_of_sets * 5) * 28.70

elif fruit == "Mango":
    if set_size == "small":
        price = (number_of_sets * 2) * 36.66
    elif set_size == "big":
        price = (number_of_sets * 5) * 19.60

elif fruit == "Pineapple":
    if set_size == "small":
        price = (number_of_sets * 2) * 42.10
    elif set_size == "big":
        price = (number_of_sets * 5) * 24.80

elif fruit == "Raspberry":
    if set_size == "small":
        price = (number_of_sets * 2) * 20
    elif set_size == "big":
        price = (number_of_sets * 5) * 15.20

if price < 400:
    print(f"{price:.2f} lv.")
elif 400 <= price <= 1000:
    price *= 0.85
    print(f"{price:.2f} lv.")
elif price > 1000:
    price *= 0.5
    print(f"{price:.2f} lv.")




