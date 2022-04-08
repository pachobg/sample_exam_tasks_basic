movie_name = input()
hall_type = input()
number_of_tickets = int(input())

price = 0

if movie_name == "A Star Is Born":
    if hall_type == "normal":
        price = number_of_tickets * 7.50
    elif hall_type == "luxury":
        price = number_of_tickets * 10.50
    elif hall_type == "ultra luxury":
        price = number_of_tickets * 13.50
elif movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        price = number_of_tickets * 7.35
    elif hall_type == "luxury":
        price = number_of_tickets * 9.45
    elif hall_type == "ultra luxury":
        price = number_of_tickets * 12.75
elif movie_name == "Green Book":
    if hall_type == "normal":
        price = number_of_tickets * 8.15
    elif hall_type == "luxury":
        price = number_of_tickets * 10.25
    elif hall_type == "ultra luxury":
        price = number_of_tickets * 13.25
elif movie_name == "The Favourite":
    if hall_type == "normal":
        price = number_of_tickets * 8.75
    elif hall_type == "luxury":
        price = number_of_tickets * 11.55
    elif hall_type == "ultra luxury":
        price = number_of_tickets * 13.95

print(f"{movie_name} -> {price:.2f} lv.")
