from math import floor
balls = int(input())

points = 0
red_points = 0
red_balls = 0
orange_points = 0
orange_balls = 0
yellow_points = 0
yellow_balls = 0
white_points = 0
white_balls = 0
black_divided = 0
other_colors = 0
for ball in range(1, balls + 1):
    color = input()
    if color == "red":
        red_balls += 1
        red_points = red_balls * 5
        points += 5
    elif color == "orange":
        orange_balls += 1
        orange_points = orange_balls * 10
        points += 10
    elif color == "yellow":
        yellow_balls += 1
        yellow_points = yellow_balls * 15
        points += 15
    elif color == "white":
        white_balls += 1
        white_points = white_balls * 20
        points += 20
    elif color == "black":
        black_divided += 1
        points = points / 2
    else:
        other_colors += 1

print(f"Total points: {floor(points)}")
print(f"Points from red balls: {red_balls}")
print(f"Points from orange balls: {orange_balls}")
print(f"Points from yellow balls: {yellow_balls}")
print(f"Points from white balls: {white_balls}")
print(f"Other colors picked: {other_colors}")
print(f"Divides from black balls: {floor(black_divided)}")
