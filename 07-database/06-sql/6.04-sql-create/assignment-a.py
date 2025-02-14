"""
Name: Database Create Table
Difficulty: easy
Lines: 5
Minutes: 5

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
>>> from pathlib import Path
>>> import sqlite3

>>> database = Path(__file__).parent.parent / 'shop.db'
>>> db = sqlite3.connect(database)

>>> try:
...     _ = db.execute(result)
...     db.commit()
... except sqlite3.OperationalError as e:
...     assert 'table contacts already exists' in str(e)

>>> TABLES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="table"'
>>> tables = {row[0] for row in db.execute(TABLES)}
>>> assert 'contacts' in tables, \
'You need to create table named `contacts`'

>>> PRAGMA = '''
...     SELECT
...         `m`.`name` AS `table_name`,
...         `p`.`name` AS `col_name`,
...         `p`.`type` AS `col_type`,
...         `p`.`pk` AS `col_is_pk`,
...         `p`.`dflt_value` AS `col_default_val`,
...         `p`.[notnull] AS `col_is_not_null`
...     FROM `sqlite_master` AS `m`
...     LEFT OUTER JOIN `pragma_table_info`((`m`.`name`)) AS `p`
...                  ON `m`.`name` != `p`.`name`
...     WHERE `m`.`type` = 'table'
...     ORDER BY `table_name`
... '''

>>> pragma = db.execute(PRAGMA).fetchall()
>>> assert ('contacts', 'id', 'INTEGER', 1, None, 0) in pragma
>>> assert ('contacts', 'firstname', 'TEXT', 0, None, 0) in pragma
>>> assert ('contacts', 'lastname', 'TEXT', 0, None, 0) in pragma
>>> assert ('contacts', 'birthdate', 'DATE', 0, 'NULL', 0) in pragma

>>> db.close()

"""

# %% SetUp

result: str

# English
# 1. Write SQL query to create table:
#    - table: `contacts`
#    - column: `id`, integer, primary key, autoincrement
#    - column: `firstname`, text
#    - column: `lastname`, text
#    - column: `birthdate`, date, default null
#    - use: IF NOT EXISTS
# 2. Run doctests - all must succeed

# Polish
# 1. Napisz zapytanie SQL aby stworzyć tabelę:
#    - tabela: `contacts`
#    - kolumna: `id`, integer, primary key, autoincrement
#    - kolumna: `firstname`, text
#    - kolumna: `lastname`, text
#    - kolumna: `birthdate`, date, default null
#    - użyj: IF NOT EXISTS
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = """

-- replace this comment
-- with your sql query

"""