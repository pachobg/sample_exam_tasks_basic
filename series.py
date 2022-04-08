budget = float(input())
number_of_serials = int(input())

serial_price = 0
total_serial_price = 0
for number in range(1, number_of_serials + 1):
    serial_name = input()
    price = float(input())
    if serial_name == "Thrones":
        serial_price = price - price * 0.5
        total_serial_price += serial_price
    elif serial_name == "Lucifer":
        serial_price = price - price * 0.4
        total_serial_price += serial_price
    elif serial_name == "Protector":
        serial_price = price - price * 0.3
        total_serial_price += serial_price
    elif serial_name == "TotalDrama":
        serial_price = price - price * 0.2
        total_serial_price += serial_price
    elif serial_name == "Area":
        serial_price = price - price * 0.1
        total_serial_price += serial_price
    else:
        serial_price = price
        total_serial_price += serial_price


difference = abs(budget - total_serial_price)
if budget >= total_serial_price:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
