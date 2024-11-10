# doctest: +SKIP_FILE
"""
* Assignment: Django Conf Superuser
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create superuser:
        a. username: `admin`
        b. email: `admin@example.com`
        c. password: `valid`
    2. Restart server
    3. Open browser and goto http://127.0.0.1:8000/admin/
    4. Login as `admin`
    5. Run doctests - all must succeed

Polish:
    1. Stwórz superuser:
        a. username: `admin`
        b. email: `admin@example.com`
        c. password: `valid`
    2. Uruchom serwer:
        a. ip: 127.0.0.1
        b. port: 8000
    3. Otwórz przeglądarkę i przejdź na stronę http://127.0.0.1:8000/admin/
    4. Zaloguj się jako `admin`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from urllib.request import urlopen
    >>> import sqlite3

    >>> sql = 'SELECT date_joined FROM auth_user WHERE username="admin"'
    >>> with sqlite3.connect('myproject/db.sqlite3') as db:
    ...     result = db.execute(sql).fetchone()
    >>> assert result is not None

    >>> response = urlopen('http://127.0.0.1:8000/admin/')
    >>> result = response.read().decode('utf-8')
    >>> assert result is not None
"""


