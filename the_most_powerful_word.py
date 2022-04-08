from math import floor
import sys

max_letter_sum = -sys.maxsize

word = input()

word_len = len(word)
letter_sum = 0

the_most_power_word = ""
while word != "End of words":
    letter1 = word[0]
    for i in word:
        letter_sum += ord(i)

    if letter1 in "AEIOUYaeiouy":
        letter_sum *= len(word)
    else:
        letter_sum /= len(word)

    if letter_sum > max_letter_sum:
        max_letter_sum = letter_sum
        the_most_power_word = word
    word = input()
    letter_sum = 0

print(f"The most powerful word is {the_most_power_word} - {floor(max_letter_sum)}")





