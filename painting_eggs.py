egg_size = input()
egg_color = input()
number_of_eggs = int(input())

price = 0

if egg_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    elif egg_color == "Yellow":
        price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    elif egg_color == "Yellow":
        price = 7
elif egg_size == "Small":
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    elif egg_color == "Yellow":
        price = 5

total_money = price * number_of_eggs

fee = total_money * 0.35

final = total_money - fee

print(f"{final:.2f} leva.")
