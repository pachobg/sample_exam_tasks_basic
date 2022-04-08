food = int(input())

food_in_grams = food * 1000

eaten_food = 0

command = input()

while command != "Adopted":
    food_per_day = int(command)
    eaten_food += food_per_day
    command = input()

difference = abs(food_in_grams - eaten_food)
if food_in_grams >= eaten_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")

