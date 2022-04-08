from math import ceil

height = int(input())
width = int(input())
not_paint_part_percent = int(input())

quadratic_meters_area = height * width * 4
area_for_painting = quadratic_meters_area - quadratic_meters_area * not_paint_part_percent / 100

painted_area = 0

command = input()

while command != "Tired!":
    liters_paint = int(command)

    if liters_paint >= area_for_painting:
        litters_left = liters_paint - area_for_painting
        print(f"All walls are painted and you have {ceil(litters_left)} l paint left!")
        break
    area_for_painting -= liters_paint
    painted_area += liters_paint
    command = input()

if area_for_painting >= painted_area:
    print(f"{ceil(area_for_painting)} quadratic m left.")

if area_for_painting == painted_area:
    print("All walls are painted! Great job, Pesho!")
