minutes = int(input())
seconds = int(input())
length = float(input())
seconds_per_100m = int(input())

quota_time = minutes * 60 + seconds

acceleration = length / 120 * 2.5

final_time = (length / 100) * seconds_per_100m - acceleration

if final_time <= quota_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {final_time:.3f}.")
else:
    difference = final_time - quota_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
