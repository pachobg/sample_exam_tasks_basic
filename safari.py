budget = float(input())
fuel = float(input())
week_day = input()

price = 0
fuel_price = fuel * 2.10
gid = 100

if week_day == "Saturday":
    price = fuel_price + gid
    price *= 0.9

elif week_day == "Sunday":
    price = fuel_price + gid
    price *= 0.8

if budget >= price:
    money_left = budget - price
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_need = price - budget
    print(f"Not enough money! Money needed: {money_need:.2f} lv.")
