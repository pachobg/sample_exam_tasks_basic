hall_seats = int(input())

command = input()
current_seats = hall_seats
price = 0
total_money = 0
people_counter = 0
while command != "Movie time!":
    people_enter = int(command)
    people_counter += people_enter
    if current_seats < people_enter:
        print("The cinema is full.")
        break
    if people_enter % 3 == 0:
        price = (people_enter * 5) - 5
        total_money += price
    else:
        price = people_enter * 5
        total_money += price
    current_seats -= people_enter

    command = input()
    if command == "Movie time!":
        difference = hall_seats - people_counter
        print(f"There are {difference} seats left in the cinema.")

print(f"Cinema income - {total_money} lv.")
