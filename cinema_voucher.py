voucher = int(input())

price = 0
voucher_left = voucher
ticket = 0
others = 0

for goods in range(voucher):
    name = input()
    if name == "End":
        break
    name_len = len(name)
    if name_len > 8:
        letter1 = name[0]
        letter2 = name[1]
        price = ord(letter1) + ord(letter2)
        if price <= voucher_left:
            ticket += 1
        else:
            break
    else:
        letter1 = name[0]
        price = ord(letter1)
        if price <= voucher_left:
            others += 1
        else:
            break
    voucher_left -= price

print(ticket)
print(others)
