number_of_windows = int(input())
type_of_windows = input()
type_of_delivery = input()

price = 0

if number_of_windows >= 10:
    if type_of_windows == "90X130":
        price = number_of_windows * 110
        if 30 < number_of_windows <= 60:
            price *= 0.95
        elif number_of_windows > 60:
            price *= 0.92

    elif type_of_windows == "100X150":
        price = number_of_windows * 140
        if 40 < number_of_windows <= 80:
            price *= 0.94
        elif number_of_windows > 80:
            price *= 0.9

    elif type_of_windows == "130X180":
        price = number_of_windows * 190
        if 20 < number_of_windows <= 50:
            price *= 0.93
        elif number_of_windows > 50:
            price *= 0.88

    elif type_of_windows == "200X300":
        price = number_of_windows * 250
        if 25 < number_of_windows <= 50:
            price *= 0.91
        elif number_of_windows > 50:
            price *= 0.86

    if type_of_delivery == "With delivery":
        price = price + 60

    if number_of_windows > 90:
        price *= 0.96
        print(f"{price:.2f} BGN")
    else:
        print(f"{price:.2f} BGN")
else:
    print("Invalid order")
