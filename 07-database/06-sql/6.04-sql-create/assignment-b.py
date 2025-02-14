"""
Name: Database Create Index
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

>>> try:
...     _ = db.execute(result)
...     db.commit()
... except sqlite3.OperationalError as e:
...     assert 'index contacts_lastname already exists' in str(e)

>>> INDEXES = 'SELECT `name` FROM `sqlite_master` WHERE `type`="index"'
>>> indexes = {row[0] for row in db.execute(INDEXES)}
>>> assert 'contacts_lastname' in indexes

>>> PRAGMA = '''
...     SELECT
...         `m`.`tbl_name` AS `table_name`,
...         `il`.`name` AS `index_name`,
...         `ii`.`name` AS `column_name`,
...         CASE `il`.`origin` WHEN 'pk' THEN 1 ELSE 0 END AS `is_primary_key`,
...         CASE `il`.[unique] WHEN 1 THEN 0 ELSE 1 END AS `non_unique`,
...         `il`.[unique] AS `is_unique`,
...         `il`.`partial`,
...         `il`.`seq` AS `sequence_in_index`
...     FROM `sqlite_master` AS `m`,
...         `pragma_index_list`(`m`.`name`) AS `il`,
...         `pragma_index_info`(`il`.`name`) AS `ii`
...     WHERE `m`.`type` = 'table'
...       AND `m`.`tbl_name` = 'contacts'
...     GROUP BY
...         `m`.`tbl_name`,
...         `il`.`name`,
...         `ii`.`name`,
...         `il`.`origin`,
...         `il`.`partial`,
...         `il`.`seq`
...     ORDER BY 1, 6
... '''

>>> pragma = db.execute(PRAGMA).fetchall()
>>> assert ('contacts', 'contacts_lastname', 'lastname', 0, 1, 0, 0, 0) in pragma

>>> db.close()

"""

# %% SetUp

result: str

# English
# 1. Write SQL query to create index:
#    - name: `contacts_lastname`
#    - table: `contacts`
#    - column: `lastname`
#    - use: IF NOT EXISTS
# 2. Run doctests - all must succeed

# Polish
# 1. Napisz zapytanie SQL aby stworzyć indeks:
#    - nazwa: `contacts_lastname`
#    - tabela: `contacts`
#    - kolumna: `lastname`
#    - użyj: IF NOT EXISTS
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = """

-- replace this comment
-- with your sql query

"""