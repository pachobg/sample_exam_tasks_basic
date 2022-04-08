destination = input()
time = input()
overnights = int(input())

price = 0

if destination == "France":
    if time == "21-23":
        price = 30
    elif time == "24-27":
        price = 35
    elif time == "28-31":
        price = 40
elif destination == "Italy":
    if time == "21-23":
        price = 28
    elif time == "24-27":
        price = 32
    elif time == "28-31":
        price = 39
elif destination == "Germany":
    if time == "21-23":
        price = 32
    elif time == "24-27":
        price = 37
    elif time == "28-31":
        price = 43

money_need = price * overnights

print(f"Easter trip to {destination} : {money_need:.2f} leva.")
