budget_need = float(input())

price = 0

while price < budget_need:
    cocktail_name = input()
    if cocktail_name == "Party!":
        break
    cocktail_count = int(input())
    price_per_order = len(cocktail_name) * cocktail_count
    if price_per_order % 2 != 0:
        price_per_order *= 0.75
    price += price_per_order
    if price >= budget_need:
        break

if price >= budget_need:
    club_income = price - budget_need
    print("Target acquired.")
    print(f"Club income - {price:.2f} leva.")
else:
    club_income = budget_need - price
    print(f"We need {club_income:.2f} leva more.")
    print(f"Club income - {price:.2f} leva.")


