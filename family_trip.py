budget = float(input())
overnights = int(input())
price_per_overnight = float(input())
percent_add_spends = int(input())

add_spend_money = budget * percent_add_spends / 100
discount = 0
price = 0

if overnights > 7:
    discount = price_per_overnight - (price_per_overnight * 0.05)
    price = discount * overnights
else:
    price = overnights * price_per_overnight

total_spend_money = price + add_spend_money

if budget >= total_spend_money:
    money_left = budget - total_spend_money
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_need = total_spend_money - budget
    print(f"{money_need:.2f} leva needed.")

