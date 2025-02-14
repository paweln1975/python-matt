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
Terminal: `python -m doctest -v assignment-b.py`

Tests:

Hints:
`cursor = db.cursor()`
`astronaut_id = cursor.lastrowid`

"""

# %% SetUp

result: list[tuple]

DATABASE = ':memory:'

DATA = {
    "mission": "Ares 3",
    "launch_date": "2035-06-29T00:00:00",
    "destination": "Mars",
    "destination_landing": "2035-11-07T00:00:00",
    "destination_location": "Acidalia Planitia",
    "crew": [{"name": "Melissa Lewis", "birthdate": "1995-07-15"},
             {"name": "Rick Martinez", "birthdate": "1996-01-21"},
             {"name": "Alex Vogel", "birthdate": "1994-11-15"},
             {"name": "Chris Beck", "birthdate": "1999-08-02"},
             {"name": "Beth Johanssen", "birthdate": "2006-05-09"},
             {"name": "Mark Watney", "birthdate": "1994-10-12"}],
}

# English
# 1. Connect to database:
#    - Set returned result type to `sqlite3.Row`
#    - Get cursor and next things execute on it
#    - Execute `SQL_CREATE_TABLE_ASTRONAUTS` to create table `astronauts`
#    - Execute `SQL_CREATE_TABLE_ADDRESSES` to create table `addresses`
#    - Execute `SQL_CREATE_INDEX_ASTRONAUT_LASTNAME` to create index
# 2. Iterate over `DATA`:
#    - Seprate `crew` from other values
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
#    - Oddziel `crew` od pozostałych wartości
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