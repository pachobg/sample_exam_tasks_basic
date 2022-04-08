movie_budget = float(input())
current_budget = movie_budget
budget_is_spend = False
total_salary = 0

command = input()
while command != "ACTION":
    command_len = len(command)
    if command_len > 15:
        actor_salary = current_budget * 0.2
        current_budget -= actor_salary
        total_salary += actor_salary

    else:
        number = float(input())
        current_budget -= number
        total_salary += number

    if total_salary > movie_budget:
        budget_is_spend = True
        break
    command = input()
difference = abs(movie_budget - total_salary)
if budget_is_spend:
    print(f"We need {difference:.2f} leva for our actors.")
else:
    print(f"We are left with {difference:.2f} leva.")