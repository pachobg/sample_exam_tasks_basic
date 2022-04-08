name_player_1 = input()
name_player_2 = input()

player_one_points = 0
player_two_points = 0

command = input()

while command != "End of game":
    card_player_one = int(command)
    card_player_two = int(input())
    if card_player_one > card_player_two:
        player_one_points += (card_player_one - card_player_two)
    elif card_player_two > card_player_one:
        player_two_points += (card_player_two - card_player_one)
    elif card_player_one == card_player_two:
        print("Number wars!")
        card_player_one = int(input())
        card_player_two = int(input())
        if card_player_one > card_player_two:
            print(f"{name_player_1} is winner with {player_one_points} points")
        elif card_player_two > card_player_one:
            print(f"{name_player_2} is winner with {player_two_points} points")
        break
    command = input()
    if command == "End of game":
        print(f"{name_player_1} has {player_one_points} points")
        print(f"{name_player_2} has {player_two_points} points")


