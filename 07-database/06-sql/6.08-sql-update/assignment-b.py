"""
Name: Database Update Many
Difficulty: easy
Lines: 2
Minutes: 3

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-b.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from pathlib import Path
>>> import sqlite3

>>> database = Path(__file__).parent.parent / 'shop.db'
>>> db = sqlite3.connect(database)
>>> _ = db.execute(result)
>>> db.commit()

>>> USERS = 'SELECT COUNT(*) FROM `contacts` WHERE `group` == "staff"'
>>> users = db.execute(USERS).fetchone()[0]
>>> assert users >= 2

>>> db.close()

"""

# %% SetUp

result: str

# English
# 1. Write SQL query to update many records:
#    - table: `contacts`
#    - where: `lastname` == 'Watney'
#    - column: `group`
#    - value: 'staff'
# 2. Run doctests - all must succeed

# Polish
# 1. Napisz zapytanie SQL aby zaktualizować wiele rekordów:
#    - tabela: `contacts`
#    - gdzie: `lastname` == 'Watney'
#    - kolumna: `group`
#    - wartość: 'staff'
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = """

-- replace this comment
-- with your sql query

"""