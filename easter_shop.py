number_of_eggs = int(input())

command = input()
eggs_sold = 0
while command != "Close":

    if command == "Buy":
        buy_eggs = int(input())
        if buy_eggs > number_of_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {number_of_eggs}.")
            break
        eggs_sold += buy_eggs
        number_of_eggs -= buy_eggs

    elif command == "Fill":
        fill_eggs = int(input())
        number_of_eggs += fill_eggs

    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
