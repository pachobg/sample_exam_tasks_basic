record = int(input())

jumps = 0
failed_jump = 0
not_success = False
lath_high = record - 30
successful_jump = 0
good_jump = 0
while lath_high <= record:
    for jump in range(1, 3 + 1):
        current_jump = int(input())
        jumps += 1
        if current_jump <= lath_high:
            failed_jump += 1

        if current_jump > lath_high:
            successful_jump += 1
            good_jump = lath_high
            failed_jump = 0
            lath_high += 5
            break
    if failed_jump == 3:
        not_success = True
        break

if not_success:
    print(f"Tihomir failed at {lath_high}cm after {jumps} jumps.")
if good_jump >= record:
    print(f"Tihomir succeeded, he jumped over {good_jump}cm after {jumps} jumps.")
