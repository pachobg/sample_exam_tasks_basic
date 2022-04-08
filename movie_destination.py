budget = float(input())
destination = input()
season = input()
days = int(input())

money = 0

if destination == "Dubai":
    if season == "Winter":
        money = days * 45000
    elif season == "Summer":
        money = days * 40000
elif destination == "Sofia":
    if season == "Winter":
        money = days * 17000
    elif season == "Summer":
        money = days * 12500
elif destination == "London":
    if season == "Winter":
        money = days * 24000
    elif season == "Summer":
        money = days * 20250

if destination == "Dubai":
    money = money - money * 0.3

if destination == "Sofia":
    money = money + money * 0.25

if budget >= money:
    money_left = budget - money
    print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")
else:
    money_need = money - budget
    print(f"The director needs {money_need:.2f} leva more!")




