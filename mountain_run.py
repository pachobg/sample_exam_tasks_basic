

old_record = float(input())
meters = float(input())
seconds_per_meter = float(input())

all_time = meters * seconds_per_meter

delay = meters // 50 * 30

climb_time = all_time + delay

if climb_time < old_record:
    print(f"Yes! The new record is {climb_time:.2f} seconds.")
else:
    seconds_need = climb_time - old_record
    print(f"No! He was {seconds_need:.2f} seconds slower.")

