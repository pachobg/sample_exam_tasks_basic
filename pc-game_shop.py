sold_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range(1, sold_games + 1):
    command = input()
    if command == "Hearthstone":
        hearthstone += 1
    elif command == "Fornite":
        fornite += 1
    elif command == "Overwatch":
        overwatch += 1
    else:
        others += 1

hearthstone_percent = hearthstone / sold_games * 100
fornite_percent = fornite / sold_games * 100
overwatch_percent = overwatch / sold_games * 100
others_percent = others / sold_games * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
