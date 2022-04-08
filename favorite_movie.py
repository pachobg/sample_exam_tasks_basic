import sys
command = input()

max_points = -sys.maxsize
movie_points = 0
movie_counter = 0
best_movie = ""
best_points = 0
while command != "STOP":

    movie_len = len(command)
    movie_counter += 1
    if movie_counter == 7:
        print("The limit is reached.")
        break

    for i in command:
        if i.islower():
            points = ord(i) - movie_len * 2
            movie_points += points
        elif i.isupper():
            points = ord(i) - movie_len
            movie_points += points
        elif i == " ":
            points = ord(i)
            movie_points += points
        elif i in "1234567890":
            points = ord(i)
            movie_points += points
    if movie_points > max_points:
        max_points = movie_points
        best_movie = command
        best_points = max_points

    command = input()
    movie_points = 0

print(f"The best movie for you is {best_movie} with {best_points} ASCII sum.")
