# Expense_Tracker_App
Python CLI Expense Tracker App

# run the python app
go to the correct folder and run
```bash
python3 expense_tracker.py
```

# Testing

Run the unit tests with the standard library unittest test discovery:

```bash
python -m unittest discover -v
```

# Coverage

Check test coverage locally using coverage.py:

```bash
# run tests and collect coverage data
coverage run -m unittest discover -v

# print a coverage summary in the terminal
coverage report -m

# generate an HTML report and open it in the browser
coverage html
open htmlcov/index.html
```

Notes:
- A `.coveragerc` file can be included to skip tests and other patterns from the report. Did not commit this file to Git.
