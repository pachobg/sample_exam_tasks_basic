player_name = input()

points = 301
good_shoot = 0
bad_shoot = 0
command = input()


while command != "Retire":
    if command == "Single":
        current_points = int(input())
        if current_points <= points:
            good_shoot += 1
            points -= current_points
        elif current_points > points:
            bad_shoot += 1

    elif command == "Double":
        current_points = int(input())
        calculated_points = current_points * 2
        if calculated_points <= points:
            good_shoot += 1
            points -= calculated_points
        elif calculated_points > points:
            bad_shoot += 1

    elif command == "Triple":
        current_points = int(input())
        calculated_points = current_points * 3
        if calculated_points <= points:
            good_shoot += 1
            points -= calculated_points
        elif calculated_points > points:
            bad_shoot += 1

    if points == 0:
        print(f"{player_name} won the leg with {good_shoot} shots.")
        break
    command = input()
    if command == "Retire":
        print(f"{player_name} retired after {bad_shoot} unsuccessful shots.")
