"""
* Assignment: Django Conf Install
* Complexity: easy
* Lines of code: 1 line
* Time: 2 min

English:
    1. Install Django in the newest version

Polish:
    1. Zainstaluj Django w najnowszej wersji

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import django

    >>> version = tuple(int(x) for x in django.__version__.split('.'))
    >>> assert version >= (5, 0), \
    'Django version is too old. Expected at least 5.0'
"""


