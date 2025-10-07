# expense_tracker_csv.py

import csv

# Dictionary to store expenses
expenses = {}

print("Welcome to Expense Tracker with CSV Saving!")
print("Enter your expenses. Type 'q' when done.\n")

# Collect user input
while True:
    item = input("Enter expense item (or 'q' to quit): ")
    
    if item.lower() == 'q':
        break
    
    try:
        amount = float(input(f"Enter amount for {item}: "))
        expenses[item] = amount
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

# Calculate total expenses
total = sum(expenses.values())

print("\n📝 Your Expenses:")
for item, amount in expenses.items():
    print(f"- {item}: {amount}")

print(f"\n💰 Total Expenses = {total}")

# Save to CSV
with open("expenses.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Amount"])
    for item, amount in expenses.items():
        writer.writerow([item, amount])
    writer.writerow(["Total", total])

print("\n✅ Expenses saved to 'expenses.csv'")

Added V3: Expense Tracker with CSV saving
