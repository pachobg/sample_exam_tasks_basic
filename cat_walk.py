walk_time = int(input())
walks_per_day = int(input())
cal_per_day = int(input())

cal_per_min = 5
minutes = walk_time * walks_per_day
burned_cal = minutes * cal_per_min

walk_finish = cal_per_day * 0.5

if burned_cal >= walk_finish:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_cal}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_cal}.")
