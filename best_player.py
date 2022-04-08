player = input()
max_goals = 0
best_player = ""
while player != "END":
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = player

    if goals >= 10:
        break
    player = input()

print(f"{best_player} is the best player!")

if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")


