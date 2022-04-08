time_of_contract = input()
type_of_contract = input()
mobile_net = input()
months = int(input())

price = 0

if time_of_contract == "one":
    if type_of_contract == "Small":
        price = 9.98
    elif type_of_contract == "Middle":
        price = 18.99
    elif type_of_contract == "Large":
        price = 25.98
    elif type_of_contract == "ExtraLarge":
        price = 35.99
elif time_of_contract == "two":
    if type_of_contract == "Small":
        price = 8.58
    elif type_of_contract == "Middle":
        price = 17.09
    elif type_of_contract == "Large":
        price = 23.59
    elif type_of_contract == "ExtraLarge":
        price = 31.79

if mobile_net == "no":
    price = price * months
elif mobile_net == "yes":
    if price <= 10:
        price = (price + 5.50) * months
    elif 10 < price <= 30:
        price = (price + 4.35) * months
    elif price > 30:
        price = (price + 3.85) * months

if time_of_contract == "two":
    price = price - (price * 0.0375)


print(f"{price:.2f} lv.")





