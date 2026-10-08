# Expense Tracker — Python CLI

[![Python Tests](https://github.com/olohi184/expense-tracker-python/actions/workflows/python-tests.yml/badge.svg)](https://github.com/olohi184/expense-tracker-python/actions/workflows/python-tests.yml)

A small, runnable Python expense tracker built from an earlier Jupyter/Colab learning project. Enter multiple expenses with a category and amount, view a total, and export a dated CSV report.

## Features
- Interactive command-line expense entry
- Category and timestamp per expense
- Decimal-based totals to avoid binary floating-point rounding errors
- CSV export to `expenses_v4.csv`
- Unit tests using Python's standard library

## Run
Requires **Python 3.10+**. No third-party packages are needed.

```bash
git clone https://github.com/olohi184/expense-tracker-python.git
cd expense-tracker-python
python main.py
```

Example:
```text
Expense item (or q): Lunch
Category: Food
Amount: 1200.50
Expense item (or q): q
Total: 1200.50
Saved to expenses_v4.csv
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Repository structure
- `main.py` — interactive CLI entry point
- `src/expense_tracker/tracker.py` — reusable data and CSV functions
- `tests/` — automated unit tests
- Existing `.ipynb` notebooks and earlier `.py` versions — retained as learning history

## Background
This repository began as notebook-based Python practice. The new CLI refactors the expense-tracking functionality from `expense_tracker_categories_v4.py` into reusable, testable code. Other experimental scripts and notebooks are preserved for transparency and are **not** part of the main application.

## Author
Olohimai Juliet Michael · [GitHub](https://github.com/olohi184)
