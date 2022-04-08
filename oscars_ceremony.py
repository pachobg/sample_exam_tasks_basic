rent = int(input())

statue = rent - (rent * 0.3)
catering = statue - (statue * 0.15)
sound = catering / 2

total = rent + statue + catering + sound

print(f"{total:.2f}")
