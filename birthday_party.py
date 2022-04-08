rent = float(input())

cake_price = rent * 0.2
drink_price = cake_price - cake_price * 0.45
animator_price = rent / 3

total = rent + cake_price + drink_price + animator_price

print(total)
