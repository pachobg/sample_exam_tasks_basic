company_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
net_price = float(input())
service = float(input())

price_ticket_adult = net_price + service
total_adult_ticket_cost = adult_tickets * price_ticket_adult

price_kid_ticket = net_price - net_price * 0.7
price_kid_ticket_service = price_kid_ticket + service
total_kid_ticket_cost = kid_tickets * price_kid_ticket_service

money = total_adult_ticket_cost + total_kid_ticket_cost

profit = money * 0.2

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
