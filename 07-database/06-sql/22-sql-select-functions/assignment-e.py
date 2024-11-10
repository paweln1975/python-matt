"""
* Assignment: Database Function Min
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `products`
       b. column: `name`, `price`
       c. what: cheapest product
       d. use: MIN()
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
       a. tabela: `products`
       b. kolumna: `name`, `price`
       c. co: najtańszy produkt
       d. użyj: MIN()
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
    [{'name': 'November', 'MIN(`price`)': 12.0}]
"""

# Write SQL query to select data:
# - table: `products`
# - column: `name`, `price`
# - what: cheapest product
# - use: MIN()
result = """

SELECT `name`, `price`
FROM `products`

"""

