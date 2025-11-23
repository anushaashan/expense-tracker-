import csv

csv_file = "expenses.csv"   # CSV already exists

# Function: Add new expense
def expenses_add():
    print("\n--- Add New Expense ---")

    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Study, etc.): ")
    amount = input("Enter amount: ")
    note = input("Enter note (optional): ")

    # Write the new expense to the csv file
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!\n")


# Function: Show existing expenses
def see_expenses():
    print("\n--- All Expenses ---")

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    print("-----------------------\n")


# Function: Monthly total expenses
def monthly_expenses():
    print("\n--- Total Monthly Expenses ---")

    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader, None)   # safely skip header if it exists

        for row in reader:
            date, category, amount, note = row

            # check month and year
            if date.startswith(f"{year}-{month}"):
                total += float(amount)

    print(f"Money spent in {month}/{year}: ₹{total}\n")


# MENU LOOP
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Check Monthly Total")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        expenses_add()
    elif choice == "2":
        see_expenses()
    elif choice == "3":
        monthly_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again!\n")

