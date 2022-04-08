import sys
easter_bread = int(input())
max_grade = -sys.maxsize
grade = 0
best_beaker = ""
for bread in range(1, easter_bread + 1):
    beaker = input()
    command = input()
    while command != "Stop":
        current_grade = int(command)
        grade += current_grade
        if grade > max_grade:
            max_grade = grade
            best_beaker = beaker
        command = input()
        if command == "Stop":
            print(f"{beaker} has {grade} points.")
            if max_grade <= grade:
                print(f"{beaker} is the new number 1!")
    grade = 0

print(f"{best_beaker} won competition with {max_grade} points!")

