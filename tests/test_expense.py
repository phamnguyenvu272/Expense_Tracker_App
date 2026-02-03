import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense import Expense


class TestExpense(unittest.TestCase):
    def test_repr_contains_fields(self):
        e = Expense("Coffee", "🍔 Food", 3.5)
        r = repr(e)
        self.assertIn("Coffee", r)
        self.assertIn("Food", r)
        self.assertIn("$3.50", r)


if __name__ == "__main__":
    unittest.main()
