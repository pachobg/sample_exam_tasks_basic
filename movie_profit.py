movie_name = input()
premiere_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
cinema_tax = int(input())

all_sold_tickets = premiere_days * number_of_tickets
total_money = all_sold_tickets * ticket_price
cinema_free = total_money * cinema_tax / 100

profit= total_money - cinema_free

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
