days = int(input())
hours = int(input())
bill = 0
current_bill = 0
for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_bill += 2.50
            bill += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            current_bill += 1.25
            bill += 1.25
        else:
            current_bill += 1
            bill += 1
    print(f"Day: {day} - {current_bill:.2f} leva")
    current_bill = 0

print(f"Total: {bill:.2f} leva")