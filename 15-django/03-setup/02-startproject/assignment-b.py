# doctest: +SKIP_FILE
"""
* Assignment: Django Conf Migrate
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Migrate the database
    2. Run doctests - all must succeed

Polish:
    1. Wykonaj migrację bazy danych
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path

    >>> basedir = Path('myproject')
    >>> assert basedir.exists()
    >>> assert (basedir/'db.sqlite3').exists()
"""


