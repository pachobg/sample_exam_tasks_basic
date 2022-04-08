import sys
from math import ceil
easter_bread = int(input())
used_sugar = 0
used_flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
for bread in range(1, easter_bread + 1):
    sugar = int(input())
    flour = int(input())
    used_sugar += sugar
    used_flour += flour
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

sugar_package = ceil(used_sugar / 950)
flour_package = ceil(used_flour / 750)

print(f"Sugar: {sugar_package}")
print(f"Flour: {flour_package}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")