berries_price = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
berries_kg = float(input())

berries_total = berries_price * berries_kg

raspberries_price = berries_price / 2
raspberries_total = raspberries_price * raspberries_kg

orange_price = raspberries_price - (raspberries_price * 0.4)
orange_total = orange_price * orange_kg

banana_price = raspberries_price - (raspberries_price * 0.8)
banana_total = banana_price * banana_kg

bill = berries_total + raspberries_total + orange_total + banana_total

print(f"{bill:.2f}")
