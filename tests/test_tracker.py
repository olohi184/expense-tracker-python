"""Run with: python -m unittest discover -s tests -v."""
import csv
import sys
import tempfile
import unittest
from decimal import Decimal, InvalidOperation
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from expense_tracker.tracker import create_expense, calculate_total, save_expenses


class ExpenseTrackerTests(unittest.TestCase):
    def test_total_and_duplicate_items(self):
        expenses = [create_expense("Lunch", "Food", "1200.50"), create_expense("Lunch", "Food", "200")]
        self.assertEqual(calculate_total(expenses), Decimal("1400.50"))

    def test_invalid_amount(self):
        with self.assertRaises((InvalidOperation, ValueError)):
            create_expense("Bus", "Transport", "not-a-number")
        with self.assertRaises(ValueError):
            create_expense("Bus", "Transport", "-5")

    def test_csv_export(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "expenses.csv"
            save_expenses([create_expense("Data", "Utilities", "500")], path)
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.reader(handle))
            self.assertEqual(rows[0], ["Item", "Category", "Amount", "Date"])
            self.assertEqual(rows[-1], ["Total", "", "500", ""])


if __name__ == "__main__":
    unittest.main()
