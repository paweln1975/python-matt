"""
* Assignment: Database Update Many
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to update many records:
       a. table: `contacts`
       b. where: `lastname` == 'Watney'
       c. column: `group`
       d. value: 'staff'
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby zaktualizować wiele rekordów:
       a. tabela: `contacts`
       b. gdzie: `lastname` == 'Watney'
       c. kolumna: `group`
       d. wartość: 'staff'
    2. Uruchom doctesty - wszystkie muszą się powieść

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

# Write SQL query to update many records:
# - table: `contacts`
# - where: `lastname` == 'Watney'
# - column: `group`
# - value: 'staff'
# type: str
result = """

-- replace this comment
-- with your sql query

"""

