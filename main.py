import argparse
import json
import os
from datetime import datetime

EXPENSE_FILE = "expenses.json"

# Load existing expenses
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense(description, amount):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    expenses.append({
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    })
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

# List all expenses
def list_expenses():
    expenses = load_expenses()
    print("ID  Date       Description  Amount")
    for exp in expenses:
        print(f"{exp['id']}   {exp['date']}  {exp['description']}  ${exp['amount']}")

# Delete an expense
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [exp for exp in expenses if exp["id"] != expense_id]
    save_expenses(expenses)
    print("Expense deleted successfully")

# Show total summary
def summary(month=None):
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses if not month or datetime.strptime(exp["date"], "%Y-%m-%d").month == month)
    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")

# Command-line argument parsing
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--description", required=True, help="Expense description")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")

    list_parser = subparsers.add_parser("list", help="List all expenses")

    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, required=True, help="Expense ID")

    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", type=int, help="Month (1-12)")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        summary(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
