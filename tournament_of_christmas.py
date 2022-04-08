win_count = 0
lose_count = 0
tournament_wins = 0
tournament_lose = 0
collected_money = 0
tournament_money = 0

tournament_days = int(input())

for day in range(1, tournament_days + 1):
    command = input()
    while command != "Finish":
        result = input()
        if result == "win":
            win_count += 1
            collected_money += 20
        elif result == "lose":
            lose_count += 1

        command = input()

    if win_count > lose_count:
        collected_money = collected_money + collected_money * 0.1
        tournament_wins += 1
    else:
        tournament_lose += 1
    tournament_money += collected_money
    win_count = 0
    lose_count = 0
    collected_money = 0


if tournament_wins > tournament_lose:
    tournament_money = tournament_money + tournament_money * 0.2
    print(f"You won the tournament! Total raised money: {tournament_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {tournament_money:.2f}")


