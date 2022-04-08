from math import ceil
number_of_guests = int(input())
budget = int(input())

eggs = number_of_guests * 2
easter_bread = ceil(number_of_guests / 3)

egg_price = eggs * 0.45
easter_bread_price = easter_bread * 4

price = egg_price + easter_bread_price

if budget >= price:
    diff = budget - price
    print(f"Lyubo bought {easter_bread} Easter bread and {eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    diff = price - budget
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")