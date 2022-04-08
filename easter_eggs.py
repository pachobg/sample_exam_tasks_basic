import sys
number_of_eggs = int(input())

max_eggs = -sys.maxsize
red = 0
orange = 0
blue = 0
green = 0
best_color = ""
for egg in range(1, number_of_eggs + 1):
    color = input()
    if color == "red":
        red += 1
        if red > max_eggs:
            max_eggs = red
            best_color = "red"
    elif color == "orange":
        orange += 1
        if orange > max_eggs:
            max_eggs = orange
            best_color = "orange"
    elif color == "blue":
        blue += 1
        if blue > max_eggs:
            max_eggs = blue
            best_color = "blue"
    elif color == "green":
        green += 1
        if green > max_eggs:
            max_eggs = green
            best_color = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {best_color}")


