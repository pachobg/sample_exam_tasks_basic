bitcoins = int(input())
china_uan = float(input())
change_fee = float(input())

bitcoin_lv = bitcoins * 1168

us = china_uan * 0.15

us_lv = us * 1.76

all_lv = bitcoin_lv + us_lv

euro = all_lv / 1.95

fee_cost = euro * change_fee / 100

change = euro - fee_cost

print(f"{change:.2f}")
