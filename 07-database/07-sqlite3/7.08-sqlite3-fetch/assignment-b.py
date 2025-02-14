"""
Name: SQLite3 Fetch Logs
Difficulty: easy
Lines: 11
Minutes: 13

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
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> assert type(result) is not Ellipsis
>>> assert type(result) is list
>>> assert len(result) > 0
>>> assert all(type(row) is tuple for row in result)

>>> result  # doctest: +NORMALIZE_WHITESPACE
[(28, '1969-07-24 17:29:00', 'INFO', 'Crew egress'),
 (27, '1969-07-24 16:50:35', 'WARNING', 'Splashdown (went to apex-down)'),
 (26, '1969-07-24 16:35:05', 'WARNING', 'Entry'),
 (25, '1969-07-24 16:21:12', 'INFO', 'CM/SM separation'),
 (24, '1969-07-22 04:55:42', 'WARNING', 'Transearth injection ignition (SPS)'),
 (23, '1969-07-21 21:35:00', 'INFO', 'CSM/LM docked'),
 (22, '1969-07-21 17:54:00', 'WARNING', 'LM lunar liftoff ignition (LM APS)'),
 (21, '1969-07-21 05:11:13', 'DEBUG', 'EVA ended (hatch closed)'),
 (20, '1969-07-21 03:15:16', 'INFO', 'LMP on lunar surface'),
 (19, '1969-07-21 03:05:58', 'DEBUG', 'Contingency sample collection started (CDR)'),
 (18, '1969-07-21 02:56:16', 'WARNING', 'Neil Armstrong first words on the Moon'),
 (17, '1969-07-21 02:56:15', 'WARNING', '1st step taken lunar surface (CDR)'),
 (16, '1969-07-21 02:39:33', 'DEBUG', 'EVA started (hatch open)'),
 (15, '1969-07-20 20:17:39', 'WARNING', 'LM lunar landing'),
 (14, '1969-07-20 20:14:18', 'ERROR', 'LM 1201 alarm'),
 (13, '1969-07-20 20:10:22', 'ERROR', 'LM 1202 alarm'),
 (12, '1969-07-20 20:05:05', 'WARNING', 'LM powered descent engine ignition'),
 (11, '1969-07-20 17:44:00', 'INFO', 'CSM/LM undocked'),
 (10, '1969-07-16 21:43:36', 'INFO', 'Lunar orbit circularization ignition'),
 (9, '1969-07-16 17:21:50', 'INFO', 'Lunar orbit insertion ignition'),
 (8, '1969-07-16 16:56:03', 'INFO', 'CSM docked with LM/S-IVB'),
 (7, '1969-07-16 16:22:13', 'INFO', 'Translunar injection'),
 (6, '1969-07-16 13:39:40', 'DEBUG', 'S-II center engine cutoff'),
 (5, '1969-07-16 13:35:17', 'DEBUG', 'Launch escape tower jettisoned'),
 (4, '1969-07-16 13:34:44', 'WARNING', 'S-II ignition'),
 (3, '1969-07-16 13:33:23', 'DEBUG', 'Maximum dynamic pressure (735.17 lb/ft^2)'),
 (2, '1969-07-16 13:31:53', 'WARNING', 'S-IC engine ignition (#5)'),
 (1, '1969-07-14 21:00:00', 'INFO', 'Terminal countdown started')]

Hints:
`datetime.fromisoformat(str)`
`datetime.combine(date, time)`
`datetime.strptime(str, format)`

"""

# %% SetUp

import sqlite3
from datetime import date, datetime, time

result: list[tuple]

DATABASE = ':memory:'

DATA = """1969-07-14, 21:00:00, INFO, Terminal countdown started
1969-07-16, 13:31:53, WARNING, S-IC engine ignition (#5)
1969-07-16, 13:33:23, DEBUG, Maximum dynamic pressure (735.17 lb/ft^2)
1969-07-16, 13:34:44, WARNING, S-II ignition
1969-07-16, 13:35:17, DEBUG, Launch escape tower jettisoned
1969-07-16, 13:39:40, DEBUG, S-II center engine cutoff
1969-07-16, 16:22:13, INFO, Translunar injection
1969-07-16, 16:56:03, INFO, CSM docked with LM/S-IVB
1969-07-16, 17:21:50, INFO, Lunar orbit insertion ignition
1969-07-16, 21:43:36, INFO, Lunar orbit circularization ignition
1969-07-20, 17:44:00, INFO, CSM/LM undocked
1969-07-20, 20:05:05, WARNING, LM powered descent engine ignition
1969-07-20, 20:10:22, ERROR, LM 1202 alarm
1969-07-20, 20:14:18, ERROR, LM 1201 alarm
1969-07-20, 20:17:39, WARNING, LM lunar landing
1969-07-21, 02:39:33, DEBUG, EVA started (hatch open)
1969-07-21, 02:56:15, WARNING, 1st step taken lunar surface (CDR)
1969-07-21, 02:56:16, WARNING, Neil Armstrong first words on the Moon
1969-07-21, 03:05:58, DEBUG, Contingency sample collection started (CDR)
1969-07-21, 03:15:16, INFO, LMP on lunar surface
1969-07-21, 05:11:13, DEBUG, EVA ended (hatch closed)
1969-07-21, 17:54:00, WARNING, LM lunar liftoff ignition (LM APS)
1969-07-21, 21:35:00, INFO, CSM/LM docked
1969-07-22, 04:55:42, WARNING, Transearth injection ignition (SPS)
1969-07-24, 16:21:12, INFO, CM/SM separation
1969-07-24, 16:35:05, WARNING, Entry
1969-07-24, 16:50:35, WARNING, Splashdown (went to apex-down)
1969-07-24, 17:29, INFO, Crew egress"""

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        level TEXT,
        message TEXT);"""

SQL_INSERT = 'INSERT INTO logs VALUES (NULL, ?, ?, ?);'
SQL_SELECT = 'SELECT * FROM logs ORDER BY datetime DESC;'

# English
# 1. Split `DATA` by lines:
#    - Strip line from whitespace at the begining and at the end
#    - Extract date, time, log level and message from each line
#    - Parse date and time as date and time objects
#    - Combine date and time into datetime object
#    - Define datetime, level and message as tuple
#    - Add that tuple to `data: list[tuple]`
# 2. Connect to database:
#    - Execute `SQL_CREATE_TABLE` to create database table
#    - Execute `SQL_INSERT` to insert logs to in `list[tuple]` format
#    - Execute `SQL_SELECT` to select data
#    - Iterate over rows and append each to `result: list[tuple]`
# 3. Run doctests - all must succeed

# Polish
# 1. Podziel `DATA` po liniach:
#    - Oczyść linię z białych znaków na początku i na końcu
#    - Wyciągnij datę, czas, poziom logowania i teść z każdej linii
#    - Rozczytaj datę i czas jako obiekty date and time
#    - Połącz datę i czas w obiekt datetime
#    - Zdefiniuj datetime, level i message jako tuplę
#    - Dodaj tą tuplę do `data: list[tuple]`
# 2. Połącz się do bazy danych:
#    - Wykonaj `SQL_CREATE_TABLE` aby stworzyć tabelę w bazie danych
#    - Wykonaj `SQL_INSERT` aby wstawić logi w formacie `list[tuple]`
#    - Wykonaj `SQL_SELECT` aby wybrać dane
#    - Iterując po wierszach dopisuj je do `result: list[tuple]`
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...