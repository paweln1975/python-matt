# doctest: +SKIP_FILE
"""
* Assignment: Django Conf CreateProject
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Create a project `myproject`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz projekt `myproject`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pathlib import Path

    >>> basedir = Path('myproject')
    >>> assert basedir.exists()
    >>> assert (basedir/'manage.py').exists()
    >>> assert (basedir/'myproject'/'settings.py').exists()
    >>> assert (basedir/'myproject'/'asgi.py').exists()
    >>> assert (basedir/'myproject'/'wsgi.py').exists()
    >>> assert (basedir/'myproject'/'urls.py').exists()
"""


