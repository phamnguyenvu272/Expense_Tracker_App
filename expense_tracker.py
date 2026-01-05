import calendar
import datetime
from expense import Expense


def main():
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    while True:
        choice = input(f"""Menu:
            1. Add Expense      
            2. View Summary
            
            🎯 What do you want to do?: """)
        
        if choice == "1":
            # Get user input for expense.
            expense = get_user_expense()

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


def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
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
        # TODO: need to validate this input
        # TODO: try catch block
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 
        # TODO: except exception handling can be added here

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as file: # a for append mode
        file.write(f"{expense.name},{expense.amount},{expense.category}\n") #\n for new line

def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = [] # this variable is a list of Expenses
    with open(expense_file_path, "r") as f: # r for read mode
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {} # {} for dictionary: to hold total amount by category
    for expense in expenses:
        key = expense.category # key for the dictionary
        if key in amount_by_category: # if the category already exists in the dictionary
            amount_by_category[key] += expense.amount # add the amount to the existing amount
        else:
            amount_by_category[key] = expense.amount # else create a new key with the amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses]) # sum all the amounts in the expenses list
    print(f"💵 Total Spent: ${total_spent:.2f}")

    # TODO: take care of scenario where total_spent > budget, show 0 or negative
    remaining_budget = budget - total_spent # 
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now() # get current date
    days_in_month = calendar.monthrange(now.year, now.month)[1] # get number of days in the current month
    remaining_days = days_in_month - now.day # calculate remaining days in the month

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))

 
def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()

#YL test