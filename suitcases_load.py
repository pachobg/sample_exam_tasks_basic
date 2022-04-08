cargo_place = float(input())

suitcases = 0
space_left = False
command = input()
while command != "End":
    current_suitcase = float(command)

    suitcases += 1
    if suitcases % 3 == 0:
        current_suitcase = current_suitcase + current_suitcase * 0.1
    if cargo_place < current_suitcase:
        space_left = True
        suitcases -= 1
        break
    cargo_place -= current_suitcase
    command = input()

if space_left:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcases} suitcases loaded.")



