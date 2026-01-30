import csv
from datetime import datetime

FILE = "data.csv"

def add_expense(category, amount):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount])

def show_total():
    total = 0
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[2])
        print(f"Total expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No data yet.")

while True:
    print("\n1. Add expense")
    print("2. Show total")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        add_expense(cat, amt)
        print("Saved!")
    elif choice == "2":
        show_total()
    elif choice == "3":
        break
