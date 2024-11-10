"""
* Assignment: Database Join Inner
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to select data:
       a. table: `users`, `addresses`
       b. column: `firstname`, `lastname`, `street`, `city`, `country
       c. what: merge data from both tables
       d. use: INNER JOIN
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wybrać dane:
         a. tabela: `users`, `addresses`
         b. kolumny: `firstname`, `lastname`, `street`, `city`, `country
         c. co: scal dane z obu tabel
         d. użyj: INNER JOIN
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

    >>> pprint(list(data), sort_dicts=False, width=250)
    [{'firstname': 'Mark', 'lastname': 'Watney', 'street': '2101 E NASA Pkwy', 'city': 'Houston', 'country': 'USA'},
     {'firstname': 'Mark', 'lastname': 'Watney', 'street': 'Kennedy Space Center', 'city': 'Merritt Island', 'country': 'USA'},
     {'firstname': 'Melissa', 'lastname': 'Lewis', 'street': 'Kamienica Pod św. Janem Kapistranem', 'city': 'Cracow', 'country': 'Poland'},
     {'firstname': 'Rick', 'lastname': 'Martinez', 'street': 'Chkalovskoye Shosse', 'city': 'Zvyozdny Gorodok', 'country': 'Russia'},
     {'firstname': 'Rick', 'lastname': 'Martinez', 'street': 'Baikonur Cosmodrome', 'city': 'Baikonur', 'country': 'Kazakhstan'},
     {'firstname': 'Alex', 'lastname': 'Vogel', 'street': 'Linder Hoehe', 'city': 'Cologne', 'country': 'Germany'},
     {'firstname': 'Beth', 'lastname': 'Johanssen', 'street': '2825 E Ave P', 'city': 'Palmdale', 'country': 'USA'},
     {'firstname': 'Chris', 'lastname': 'Beck', 'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'country': 'USA'}]
"""

# Write SQL query to select data:
# - table: `users`, `addresses`
# - column: `firstname`, `lastname`, `street`, `city`, `country
# - what: merge data from both tables
# - use: INNER JOIN
result = """

-- replace this comment
-- with your sql query

"""

