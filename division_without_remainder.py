number = int(input())

counter_2 = 0
counter_3 = 0
counter_4 = 0
for i in range(1, number + 1):
    current_num = int(input())
    if current_num % 2 == 0:
        counter_2 += 1
    if current_num % 3 == 0:
        counter_3 += 1
    if current_num % 4 == 0:
        counter_4 += 1

percent_2 = counter_2 / number * 100
percent_3 = counter_3 / number * 100
percent_4 = counter_4 / number * 100

print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")