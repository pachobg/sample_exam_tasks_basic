command = input()

win = 0
lost = 0
tournament_count = 0

while command != "End of tournaments":
    tournaments = int(input())
    for tournament in range(1, tournaments + 1):
        ally_points = int(input())
        enemy_points = int(input())
        tournament_count += 1
        difference = abs(ally_points - enemy_points)
        if ally_points > enemy_points:
            win += 1
            print(f"Game {tournament} of tournament {command}: win with {difference} points.")
        elif ally_points < enemy_points:
            lost += 1
            print(f"Game {tournament} of tournament {command}: lost with {difference} points.")
    command = input()

win_percent = win / tournament_count * 100
lost_percent = lost / tournament_count * 100

print(f"{win_percent:.2f}% matches win")
print(f"{lost_percent:.2f}% matches lost")
