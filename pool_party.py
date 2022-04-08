from math import ceil
number_of_people = int(input())
entering_price = float(input())
chair_price = float(input())
umbrella_price = float(input())


entering_price_total = number_of_people * entering_price

umbrella_count = ceil(number_of_people / 2)
umbrella_price_total = umbrella_count * umbrella_price

chair_count = ceil(number_of_people * 0.75)
chair_price_total = chair_count * chair_price

total_bill = entering_price_total + umbrella_price_total + chair_price_total

print(f"{total_bill:.2f} lv.")
