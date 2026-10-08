"""Run the interactive expense tracker: python main.py."""
import sys
from pathlib import Path
from decimal import InvalidOperation

sys.path.insert(0, str(Path(__file__).parent / "src"))
from expense_tracker.tracker import create_expense, calculate_total, save_expenses


def main() -> None:
    expenses = []
    print("Welcome to Expense Tracker! Type 'q' to finish.")
    while True:
        item = input("Expense item (or q): ").strip()
        if item.lower() == "q":
            break
        category = input("Category: ").strip()
        amount = input("Amount: ").strip()
        try:
            expenses.append(create_expense(item, category, amount))
        except (InvalidOperation, ValueError) as exc:
            print(f"Invalid expense: {exc}")
    for expense in expenses:
        print(f"{expense.item} ({expense.category}): {expense.amount} on {expense.date}")
    print(f"Total: {calculate_total(expenses)}")
    save_expenses(expenses, "expenses_v4.csv")
    print("Saved to expenses_v4.csv")


if __name__ == "__main__":
    main()
