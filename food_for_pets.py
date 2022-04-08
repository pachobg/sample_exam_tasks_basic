days = int(input())
pet_food = float(input())

cookies = 0
dog_food = 0
cat_food = 0

for day in range(1, days + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())
    dog_food += current_dog_food
    cat_food += current_cat_food
    if day % 3 == 0:
        cookies += (current_dog_food + current_cat_food) * 0.1

all_food = dog_food + cat_food
all_food_percent = all_food / pet_food * 100
dog_food_percent = dog_food / all_food * 100
cat_food_percent = cat_food / all_food * 100

print(f"Total eaten biscuits: {round(cookies)}gr.")
print(f"{all_food_percent:.2f}% of the food has been eaten.")
print(f"{dog_food_percent:.2f}% eaten from the dog.")
print(f"{cat_food_percent:.2f}% eaten from the cat.")
