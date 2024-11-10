"""
* Assignment: Database Select OrderByRandom
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`
       c. order: random
       d. limit: 1 row
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`
       c. kolejność: losowa
       d. limit: 1 wiersz
    2. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * RANDOM(0) - sets the seed to zero in MySQL
    * There is no seeded random in SQLite3

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> from pathlib import Path
    >>> import sqlite3

    >>> database = Path(__file__).parent.parent / 'shop.db'
    >>> with sqlite3.connect(database) as db:
    ...    db.row_factory = sqlite3.Row
    ...    data = map(dict, db.execute(result).fetchall())

    >>> pprint(list(data), sort_dicts=False, width=79)  # doctest: +SKIP
    [{'firstname': 'Mark', 'lastname': 'Watney'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`
# - order: random
# - limit: 1 row
# type: str
result = """

SELECT `firstname`, `lastname`
FROM `users`
ORDER BY ...
LIMIT 1

"""

