movie_name = input()

student_ticket = 0
standard_ticket = 0
kid_ticket = 0
movie_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    for x in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
        movie_tickets += 1
    percent_full = movie_tickets / free_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")
    movie_tickets = 0
    movie_name = input()

total_tickets = student_ticket + standard_ticket + kid_ticket
standard_ticket_percent = standard_ticket / total_tickets * 100
student_ticket_percent = student_ticket / total_tickets * 100
kid_ticket_percent = kid_ticket / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_ticket_percent:.2f}% student tickets.")
print(f"{standard_ticket_percent:.2f}% standard tickets.")
print(f"{kid_ticket_percent:.2f}% kids tickets.")




