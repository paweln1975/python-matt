# doctest: +SKIP_FILE
"""
* Assignment: Django Conf Runserver
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Run server:
        a. ip: 127.0.0.1
        b. port: 8000
    2. Open browser and goto http://127.0.0.1:8000/
    3. Run doctests - all must succeed

Polish:
    1. Uruchom serwer:
        a. ip: 127.0.0.1
        b. port: 8000
    2. Otwórz przeglądarkę i przejdź na stronę http://127.0.0.1:8000/
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from urllib.request import urlopen

    >>> response = urlopen('http://127.0.0.1:8000/')
    >>> result = response.read().decode('utf-8')
    >>> assert result is not None
"""


