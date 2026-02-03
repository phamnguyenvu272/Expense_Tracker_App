import unittest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import expense_tracker
from expense_tracker import (
    group_expenses_by_category,
    calculate_remaining_budget,
    save_expense_to_file,
    summarize_expenses,
    get_user_expense,
    main
)
from expense import Expense


class TestExpenseTracker(unittest.TestCase):
    def test_group_expenses_by_category(self):
        expenses = [
            Expense("A", "🍔 Food", 10),
            Expense("B", "🍔 Food", 5),
            Expense("C", "💼 Work", 20),
        ]
        res = group_expenses_by_category(expenses)
        self.assertEqual(res, {"🍔 Food": 15, "💼 Work": 20})

if __name__ == "__main__":
    unittest.main()
