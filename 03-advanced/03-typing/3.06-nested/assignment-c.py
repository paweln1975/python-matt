"""
Name: Typing Annotations List of Dict
Difficulty: easy
Lines: 2
Minutes: 2

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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> import importlib
>>> from typing import get_type_hints, get_origin

>>> module = importlib.import_module(__name__)
>>> annotations = get_type_hints(module)

>>> assert get_origin(annotations['data']) == list
>>> assert data == [
...     {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
...     {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
...     {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
... ], \
'Do not modify variable `data` value, just add type annotation'

"""

# %% SetUp

# English
# 1. Add type annotations to the variable
# 2. Run doctests - all must succeed

# Polish
# 1. Dodaj adnotacje typów do zmiennej
# 2. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
data: list[dict[str, str | list[float]]] = [
    {'features': [4.7, 3.2, 1.3, 0.2], 'label': 'setosa'},
    {'features': [7.0, 3.2, 4.7, 1.4], 'label': 'versicolor'},
    {'features': [7.6, 3.0, 6.6, 2.1], 'label': 'virginica'},
]