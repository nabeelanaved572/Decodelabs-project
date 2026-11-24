# Expense Tracker
expense = []

while(True):
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Exit")

    choice = int(input("Entre your choice"))

    if choice == 1:
        name = input("Entre expense name:")
        amt = float(input("Entre the amount:"))

        expense.append([name, amt])
        print("Expense added successfully")

    elif choice == 2:
        print("Your expense: ")
        for item in expenses:
            print(f"{item[0]} : Rs. {item[1]}")

    elif choice == 3:
        total = 0
        for item in expense:
            total += item[1]

        print("Total expense : Rs", Total)

    elif choice == 4:
        print("Thank you! you can exist")
        break

    else:
        print("Invalid choice")
