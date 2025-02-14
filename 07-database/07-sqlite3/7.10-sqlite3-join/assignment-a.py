"""
Name: SQLite3 Join Relations
Difficulty: medium
Lines: 15
Minutes: 21

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert type(result) is not Ellipsis
>>> assert type(result) is list
>>> assert len(result) > 0
>>> assert all(type(row) is dict for row in result)

>>> result  # doctest: +NORMALIZE_WHITESPACE
[{'id': 1, 'firstname': 'José', 'lastname': 'Jiménez', 'astronaut_id': 1, 'street': '2101 E NASA Pkwy', 'city': 'Houston', 'state': 'Texas', 'code': 77058, 'country': 'USA'},
 {'id': 1, 'firstname': 'José', 'lastname': 'Jiménez', 'astronaut_id': 1, 'street': None, 'city': 'Kennedy Space Center', 'state': 'Florida', 'code': 32899, 'country': 'USA'},
 {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'astronaut_id': 2, 'street': '4800 Oak Grove Dr', 'city': 'Pasadena', 'state': 'California', 'code': 91109, 'country': 'USA'},
 {'id': 2, 'firstname': 'Mark', 'lastname': 'Watney', 'astronaut_id': 2, 'street': '2825 E Ave P', 'city': 'Palmdale', 'state': 'California', 'code': 93550, 'country': 'USA'},
 {'id': 3, 'firstname': 'Иван', 'lastname': 'Иванович', 'astronaut_id': 3, 'street': '', 'city': 'Космодро́м Байкону́р', 'state': 'Кызылординская область', 'code': None, 'country': 'Қазақстан'},
 {'id': 5, 'firstname': 'Alex', 'lastname': 'Vogel', 'astronaut_id': 5, 'street': 'Linder Hoehe', 'city': 'Cologne', 'state': None, 'code': 51147, 'country': 'Germany'}]

Hints:
`cursor = db.cursor()`
`astronaut_id = cursor.lastrowid`

"""

# %% SetUp

import sqlite3

result: list[tuple]

DATABASE = ':memory:'

DATA = [
    {"firstname": "José", "lastname": "Jiménez", "addresses": [
        {"street": "2101 E NASA Pkwy", "code": 77058, "city": "Houston", "state": "Texas", "country": "USA"},
        {"street": None, "code": 32899, "city": "Kennedy Space Center", "state": "Florida", "country": "USA"}]},

    {"firstname": "Mark", "lastname": "Watney", "addresses": [
        {"street": "4800 Oak Grove Dr", "code": 91109, "city": "Pasadena", "state": "California", "country": "USA"},
        {"street": "2825 E Ave P", "code": 93550, "city": "Palmdale", "state": "California", "country": "USA"}]},

    {"firstname": "Иван", "lastname": "Иванович", "addresses": [
        {"street": "", "code": None, "city": "Космодро́м Байкону́р", "state": "Кызылординская область", "country": "Қазақстан"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "addresses": []},

    {"firstname": "Alex", "lastname": "Vogel", "addresses": [
        {"street": "Linder Hoehe", "city": "Cologne", "code": 51147, "state": None, "country": "Germany"}]}
]

SQL_CREATE_TABLE_ASTRONAUTS = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT);"""

SQL_CREATE_TABLE_ADDRESSES = """
    CREATE TABLE IF NOT EXISTS addresses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        astronaut_id INTEGER,
        street TEXT,
        city TEXT,
        state TEXT,
        code INTEGER,
        country TEXT);"""

SQL_CREATE_INDEX_ASTRONAUT_LASTNAME = """
    CREATE INDEX IF NOT EXISTS lastname_index ON astronauts (lastname);"""

SQL_INSERT_ASTRONAUT = """
    INSERT INTO astronauts VALUES (
        NULL,
        :firstname,
        :lastname);"""

SQL_INSERT_ADDRESS = """
    INSERT INTO addresses VALUES (
        NULL,
        :astronaut_id,
        :street,
        :city,
        :state,
        :code,
        :country);"""

SQL_SELECT = """
    SELECT *
    FROM astronauts
    JOIN addresses
    ON astronauts.id=addresses.astronaut_id;"""

# English
# 1. Connect to database:
#    - Set returned result type to `sqlite3.Row`
#    - Get cursor and next things execute on it
#    - Execute `SQL_CREATE_TABLE_ASTRONAUTS` to create table `astronauts`
#    - Execute `SQL_CREATE_TABLE_ADDRESSES` to create table `addresses`
#    - Execute `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` to create index
# 2. Iterate over `DATA`:
#    - Seprate `addresses` from other values
#    - Execute `SQL_INSERT_ASTRONAUT` to insert astroanut to database
#    - Get `id` of the last inserted row (`cursor.lastrowid`)
#    - Add `id` to each address
#    - Executing `SQL_INSERT_ADDRESS` insert `addresses` to database
# 3. Executing `SQL_SELECT` select data from database:
#    - Join data from both tables
#    - Append each row to `result: list[dict]`
# 4. Run doctests - all must succeed

# Polish
# 1. Połącz się do bazy danych:
#    - Ustaw typ zwracanych wyników na `sqlite3.Row`
#    - Pobierz kursor i następne polecenia wykonuj na nim
#    - Wykonując `SQL_CREATE_TABLE_ASTRONAUTS` stwórz tabelę `astronauts`
#    - Wykonując `SQL_CREATE_TABLE_ADDRESSES` stwórz tabelę `addresses`
#    - Wykonując `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` stwórz indeks
# 2. Iteruj po `DATA`:
#    - Oddziel `addresses` od pozostałych wartości
#    - Wykonując `SQL_INSERT_ASTRONAUT` wstaw astronautę do bazy
#    - Pobierz `id` ostatniego wstawianego wiersza (`cursor.lastrowid`)
#    - Dodaj to `id` do każdego adresu
#    - Wykonując `SQL_INSERT_ADDRESS` wstaw adresy do bazy danych
# 3. Wykonując `SQL_SELECT` wybierz dane z bazy:
#    - Połącz dane z obu tabel
#    - Dodaj każdy rekord do `result: list[dict]`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...