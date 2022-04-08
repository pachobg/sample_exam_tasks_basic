number_of_eggs_player1 = int(input())
number_of_eggs_player2 = int(input())

command = input()
while command != "End of battle":
    if command == "one":
        number_of_eggs_player2 -= 1
    elif command == "two":
        number_of_eggs_player1 -= 1
    if number_of_eggs_player1 == 0 or number_of_eggs_player2 == 0:
        break
    command = input()
    if command == "End of battle":
        print(f"Player one has {number_of_eggs_player1} eggs left.")
        print(f"Player two has {number_of_eggs_player2} eggs left.")

if number_of_eggs_player1 == 0:
    print(f"Player one is out of eggs. Player two has {number_of_eggs_player2} eggs left.")
elif number_of_eggs_player2 == 0:
    print(f"Player two is out of eggs. Player one has {number_of_eggs_player1} eggs left.")