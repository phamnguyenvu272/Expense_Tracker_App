import calendar
import datetime
from expense import Expense


def main(input_func=input):
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    while True:
        choice = input_func(f"""Menu:
            1. Add Expense      
            2. View Summary
            
            🎯 What do you want to do?: """)
        
        if choice == "1":
            # Get user input for expense.
            expense = get_user_expense(input_func=input_func)

            # Write their expense to a file.
            save_expense_to_file(expense, expense_file_path)

            # Read file and summarize expenses.
            summarize_expenses(expense_file_path, budget)
            break
        if choice == "2":
            # Read file and summarize expenses.
            summarize_expenses(expense_file_path, budget)
            break
        else:
            print("Invalid category. Please try again!")

# use input_func parameter to allow injection of custom input function for testing
def get_user_expense(input_func=input):
    print(f"🎯 Getting User Expense")
    expense_name = input_func("Enter expense name: ")

    # Validate expense amount input: keep prompting until a valid non-negative number is entered
    while True:
        amount_input = input_func("Enter expense amount: ")
        try:
            expense_amount = float(amount_input)
            if expense_amount < 0:
                print("Amount cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value (e.g., 12.50).")

    print(f"You've entered: {expense_name}, Amount: {expense_amount}")

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")  

        value_range = f"[1 - {len(expense_categories)}]"
        # validating the user input
        try:
            selected_index = int(input_func(f"Enter a category number {value_range}: ")) - 1
        except ValueError:
            print(f"Invalid input. Please enter a number from {value_range}.")
            continue

        if 0 <= selected_index < len(expense_categories):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    # YL added , encoding="utf-8": specify UTF‑8 encoding so emojis do not crash on Windows
    with open(expense_file_path, "a", encoding="utf-8") as file: # a for append mode
        file.write(f"{expense.name},{expense.amount},{expense.category}\n") #\n for new line

        
# ---------------------------------------------------------
#  YL added— FEATURE 1: Group Expenses by Category
# ---------------------------------------------------------
def group_expenses_by_category(expenses: list[Expense]) -> dict:
    """
    Group expenses by category and return:
    {category: total_amount}
    """
    amount_by_category = {}

    for expense in expenses:
        if expense.category in amount_by_category:
            amount_by_category[expense.category] += expense.amount
        else:
            amount_by_category[expense.category] = expense.amount

    return amount_by_category


# ---------------------------------------------------------
# YL added— FEATURE 2: Track Remaining Budget
# ---------------------------------------------------------
def calculate_remaining_budget(expenses: list[Expense], monthly_budget: float) -> float:
    """
    Calculate remaining budget after subtracting total expenses.
    Returns a float (can be negative if overspent).
    """
    total_spent = sum(e.amount for e in expenses)
    return monthly_budget - total_spent


# ---------------------------------------------------------
# YL Updated summarize_expenses() using above 2 feature functions
# ---------------------------------------------------------
def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = [] # this variable is a list of Expenses
    # YL added , encoding="utf-8":
    with open(expense_file_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            name, amount, category = line.strip().split(",")
            expenses.append(Expense(name=name, amount=float(amount), category=category))

    # --- YL edit ---
    amount_by_category = group_expenses_by_category(expenses)

    print("Expenses By Category:")
    for category, amount in amount_by_category.items():
        print(f"  {category}: ${amount:.2f}")

    # --- YL edit: Remaining Budget ---
    remaining_budget = calculate_remaining_budget(expenses, budget)
    total_spent = budget - remaining_budget

    print(f"💵 Total Spent: ${total_spent:.2f}")
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    # Daily budget calculation
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))
    else:
        print("End of month — no daily budget calculation.")

 
def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()