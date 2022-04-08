a1 = int(input())
a2 = int(input())
n = int(input())
# calculate n/2 so we can use it in the 3-rd nested for
n2 = int(n * 0.5)

# Символ 1: символ с ASCII код от а1 до а2 - 1
for ch1 in range(a1, a2):
    # I'm checking if "символ 1 е нечетна"
    if ch1 % 2 == 0:
        continue
    letter = chr(ch1)
    # •   Символ 2: цифра от 1 до n - 1
    for ch2 in range(1, n):
        # •   Символ 3: цифра от 1 до n / 2 - 1
        for ch3 in range(1, n2):
            # •    Символ 4: цифрова репрезентация (ASCII код) на символ 1 - this will be ch1 from the first for
            # here I check if "сборът на символ 2, символ 3 и символ 4 е нечетен"
            if (ch1 + ch2 + ch3) % 2 == 0:
                continue

            print(f"{letter}-{ch2}{ch3}{ch1}")
