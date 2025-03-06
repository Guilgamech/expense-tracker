# Expense Tracker CLI

A simple command-line application to track expenses. Users can add, delete, and view expenses along with a summary of their spending.

## Features
- Add an expense with a description and amount.
- Update an expense.
- Delete an expense.
- View all expenses.
- View a summary of total expenses.
- View a summary of expenses for a specific month.
- Data stored in a JSON file.

## Installation
Ensure you have Python installed on your system. Clone this repository and navigate to the project directory.
```sh
$ git clone <repository-url>
$ cd expense-tracker
```

## Usage
Run the script with the following commands:

### Add an expense
```sh
python expense_tracker.py add --description "Lunch" --amount 20
```
Output:
```
Expense added successfully (ID: 1)
```

### List all expenses
```sh
$ python expense_tracker.py list
```
Output:
```
ID  Date       Description  Amount
1   2024-08-06  Lunch        $20
```

### Delete an expense

```sh
python expense_tracker.py delete --id 1
```

Output:

```
Expense deleted successfully
```

### View total expenses summary

```sh
python expense_tracker.py summary
```

Output:
```
Total expenses: $20
```

### View summary for a specific month
```sh
$ python expense_tracker.py summary --month 8
```
Output:
```
Total expenses for August: $20
```

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.

