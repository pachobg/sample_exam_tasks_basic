athlete_number = int(input())

back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0
workout_counter = 0
product_counter = 0

for athlete in range(1, athlete_number +1):
    activity = input()
    if activity == "Back":
        back_counter += 1
        workout_counter += 1
    elif activity == "Chest":
        chest_counter += 1
        workout_counter += 1
    elif activity == "Legs":
        legs_counter += 1
        workout_counter += 1
    elif activity == "Abs":
        abs_counter += 1
        workout_counter += 1
    elif activity == "Protein shake":
        protein_shake_counter += 1
        product_counter += 1
    elif activity == "Protein bar":
        protein_bar_counter += 1
        product_counter += 1

workout_percent = workout_counter / athlete_number * 100
product_percent = product_counter / athlete_number * 100

print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{workout_percent:.2f}% - work out")
print(f"{product_percent:.2f}% - protein")