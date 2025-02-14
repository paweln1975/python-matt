"""
Name: Database Select OrderByMany
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from pprint import pprint
>>> from pathlib import Path
>>> import sqlite3

>>> database = Path(__file__).parent.parent / 'shop.db'
>>> with sqlite3.connect(database) as db:
...    db.row_factory = sqlite3.Row
...    data = map(dict, db.execute(result).fetchall())

>>> pprint(list(data), sort_dicts=False, width=79)
[{'firstname': 'Chris', 'lastname': 'Beck'},
 {'firstname': 'Beth', 'lastname': 'Johanssen'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'},
 {'firstname': 'Alex', 'lastname': 'Vogel'},
 {'firstname': 'Mark', 'lastname': 'Watney'}]

"""

# %% SetUp

result: str

# English
# 1. Write SQL query to select data:
#    - table: `users`
#    - columns: `firstname`, `lastname`
#    - order1: `lastname` ascending
#    - order2: `firstname` descending
# 2. Run doctests - all must succeed

# Polish
# 1. Napisz zapytanie SQL aby wybrać dane:
#    - tabela: `users`
#    - kolumny: `firstname`, `lastname`
#    - kolejność1: `lastname` rosnąco
#    - kolejność2: `firstname` malejąco
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = """

SELECT `firstname`, `lastname`
FROM `users`

"""