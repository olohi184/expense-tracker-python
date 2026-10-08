"""Expense tracking logic, separated from interactive input."""
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
import csv
from pathlib import Path


@dataclass(frozen=True)
class Expense:
    item: str
    category: str
    amount: Decimal
    date: str


def calculate_total(expenses: list[Expense]) -> Decimal:
    return sum((expense.amount for expense in expenses), Decimal("0"))


def save_expenses(expenses: list[Expense], path: str | Path) -> None:
    """Write records and total to CSV, using the original project's columns."""
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Item", "Category", "Amount", "Date"])
        for expense in expenses:
            writer.writerow([expense.item, expense.category, str(expense.amount), expense.date])
        writer.writerow(["Total", "", str(calculate_total(expenses)), ""])


def create_expense(item: str, category: str, amount: str) -> Expense:
    value = Decimal(amount)
    if not value.is_finite() or value < 0:
        raise ValueError("Amount must be a non-negative finite number")
    if not item.strip() or not category.strip():
        raise ValueError("Item and category are required")
    return Expense(item.strip(), category.strip(), value, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
