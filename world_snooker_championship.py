stage_of_championship = input()
ticket_type = input()
number_of_tickets = int(input())
picture = input()

price = 0

if stage_of_championship == "Quarter final":
    if ticket_type == "Standard":
        price = number_of_tickets * 55.50
    elif ticket_type == "Premium":
        price = number_of_tickets * 105.20
    elif ticket_type == "VIP":
        price = number_of_tickets * 118.90

elif stage_of_championship == "Semi final":
    if ticket_type == "Standard":
        price = number_of_tickets * 75.88
    elif ticket_type == "Premium":
        price = number_of_tickets * 125.22
    elif ticket_type == "VIP":
        price = number_of_tickets * 300.40

elif stage_of_championship == "Final":
    if ticket_type == "Standard":
        price = number_of_tickets * 110.10
    elif ticket_type == "Premium":
        price = number_of_tickets * 160.66
    elif ticket_type == "VIP":
        price = number_of_tickets * 400

if price <= 2500:
    if picture == "Y":
        price = price + (number_of_tickets * 40)
elif 2500 < price <= 4000:
    price *= 0.9
    if picture == "Y":
        price = price + (number_of_tickets * 40)
elif price > 4000:
    price *= 0.75

print(f"{price:.2f}")

