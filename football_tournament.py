football_team = input()

games = int(input())
wins = 0
draws = 0
loses = 0
points = 0

if games == 0:
    print(f"{football_team} hasn't played any games during this season.")
elif games > 0:
    for game in range(1, games + 1):
        result = input()
        if result == "W":
            wins += 1
            points += 3
        elif result == "D":
            draws += 1
            points += 1
        elif result == "L":
            loses += 1

if wins == 0 and games > 0:
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print("Win rate: 0.00%")
elif wins >= 1:
    average_win_rate = wins / games * 100
    print(f"{football_team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {average_win_rate:.2f}%")
