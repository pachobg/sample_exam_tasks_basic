import sys
command = input()
max_points = -sys.maxsize
points = 0
win_points = 0
winner = ""
while command != "Stop":

    for i in command:
        current_num = int(input())
        if ord(i) == current_num:
            points += 10
        else:
            points += 2
    if points > max_points:
        max_points = points
        winner = command
    elif points == max_points:
        max_points = points
        winner = command
    command = input()
    points = 0


print(f"The winner is {winner} with {max_points} points!")



