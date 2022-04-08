bag_20_kg_price = float(input())
bag_kg = float(input())
days_left = int(input())
bag_count = int(input())

bag_fee = 0
bag_10kg = bag_20_kg_price * 0.2
bag_10_20 = bag_20_kg_price * 0.5

if bag_kg < 10:
    bag_fee = bag_10kg
elif 10 <= bag_kg <= 20:
    bag_fee = bag_10_20
else:
    bag_fee = bag_20_kg_price

add_fee = 0

if days_left > 30:
    add_fee = bag_fee + (bag_fee * 0.1)
elif 7 <= days_left <= 30:
    add_fee = bag_fee + (bag_fee * 0.15)
elif 0 <= days_left <= 6:
    add_fee = bag_fee + (bag_fee * 0.4)

total_bag_price = add_fee * bag_count

print(f"The total price of bags is: {total_bag_price:.2f} lv. ")



