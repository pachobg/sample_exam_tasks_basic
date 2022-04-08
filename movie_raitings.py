import sys
number_of_movies = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
best_movie = ""
words_movie = ""
total_rating = 0

for x in range(number_of_movies):
    movie_name = input()
    rating = float(input())
    if rating > max_rating:
        max_rating = rating
        best_movie = movie_name
    elif rating < min_rating:
        min_rating = rating
        words_movie = movie_name
    total_rating += rating

average = total_rating / number_of_movies

print(f"{best_movie} is with highest rating: {max_rating:.1f}")
print(f"{words_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")

