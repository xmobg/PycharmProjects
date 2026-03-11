import os
import json

def load_expenses():
    if os.path.exists('expenses.json') and os.path.getsize('expenses.json') > 0:
        with open('expenses.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []

def add_expense(expenses):
    amount = float(input('Enter amount of expense: '))
    category = input('Enter category of expense: ')
    expenses.append({'amount': amount, 'category': category})

def save_expenses(expenses):
    with open('expenses.json', 'w', encoding='utf-8') as f:
        json.dump(expenses, f, indent=2)

expenses = load_expenses()

while True:
    print("\nWelcome to the expenses app!")
    print("Please select an option:")
    print("1. Add an expense")
    print("2. Show expenses")
    print("3. Exit the app")

    option = int(input('Enter an option: '))

    if option == 1:
        add_expense(expenses)
        save_expenses(expenses)
    elif option == 2:
        if not expenses:
            print("No expenses yet.")
        else:
            print("\nYour expenses:")
            for e in expenses:
                print(f"{e['category']}: {e['amount']:.2f} euro")
            total = sum(e['amount'] for e in expenses)
            print(f" Total expenses: {total:.2f} euro")
    elif option == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
