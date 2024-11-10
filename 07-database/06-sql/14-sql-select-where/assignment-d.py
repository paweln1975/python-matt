"""
* Assignment: Database Where GreaterOrEqual
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`
       b. columns: `firstname`, `lastname`, `birthdate`
       c. where: `birthdate` is later than '2000-01-01' (inclusive)
       d. use: >=
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `users`
       b. kolumny: `firstname`, `lastname`, `birthdate`
       c. gdzie: `birthdate` jest późniejsza niż '2000-01-01' (włącznie)
       d. użyj: >=
    2. Uruchom doctesty - wszystkie muszą się powieść

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
    [{'firstname': 'Beth', 'lastname': 'Johanssen', 'birthdate': '2006-05-09'}]
"""

# Write SQL query to select data:
# - table: `users`
# - columns: `firstname`, `lastname`, `birthdate`
# - where: `birthdate` is later than '2000-01-01' (inclusive)
# - use: >=
# type: str
result = """

SELECT `firstname`, `lastname`, `birthdate`
FROM `users`
WHERE `birthdate`

"""

