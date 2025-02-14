"""
Name: Database Join Left
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> from pprint import pprint
>>> from pathlib import Path
>>> import sqlite3

>>> database = Path(__file__).parent.parent / 'shop.db'
>>> with sqlite3.connect(database) as db:
...    db.row_factory = sqlite3.Row
...    data = map(dict, db.execute(result).fetchall())

>>> pprint(list(data), sort_dicts=False, width=250)
[{'firstname': 'Chris', 'lastname': 'Beck', 'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'country': 'USA'},
 {'firstname': 'Beth', 'lastname': 'Johanssen', 'street': '2825 E Ave P', 'city': 'Palmdale', 'country': 'USA'},
 {'firstname': 'Melissa', 'lastname': 'Lewis', 'street': 'Kamienica Pod św. Janem Kapistranem', 'city': 'Cracow', 'country': 'Poland'},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'street': 'Baikonur Cosmodrome', 'city': 'Baikonur', 'country': 'Kazakhstan'},
 {'firstname': 'Rick', 'lastname': 'Martinez', 'street': 'Chkalovskoye Shosse', 'city': 'Zvyozdny Gorodok', 'country': 'Russia'},
 {'firstname': 'Alex', 'lastname': 'Vogel', 'street': 'Linder Hoehe', 'city': 'Cologne', 'country': 'Germany'},
 {'firstname': 'Mark', 'lastname': 'Watney', 'street': '2101 E NASA Pkwy', 'city': 'Houston', 'country': 'USA'},
 {'firstname': 'Mark', 'lastname': 'Watney', 'street': 'Kennedy Space Center', 'city': 'Merritt Island', 'country': 'USA'}]

"""

# %% SetUp

result: str

# English
# 1. Write SQL query to select data:
#    - table: `users`, `addresses`
#    - column: `firstname`, `lastname`, `street`, `city`, `country
#    - what: merge data from both tables
#    - use: LEFT JOIN
# 2. Run doctests - all must succeed

# Polish
# 1. Napisz zapytanie SQL aby wybrać dane:
#    - tabela: `users`, `addresses`
#    - kolumny: `firstname`, `lastname`, `street`, `city`, `country
#    - co: scal dane z obu tabel
#    - użyj: LEFT JOIN
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = """

-- replace this comment
-- with your sql query

"""