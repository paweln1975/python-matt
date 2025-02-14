"""
Name: Builtin Function Average
Difficulty: easy
Lines: 12
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
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint
>>> pprint(result)  # doctest: +ELLIPSIS
{'petal_length': 3.6666...,
 'petal_width': 1.1500...,
 'sepal_length': 5.6666...,
 'sepal_width': 3.0500...,
 'species': None}

"""

# %% SetUp

result: dict[str, list]

DATA = [
    ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),]

# English
# 1. Separate header and rows
# 2. Define dict `result: dict[str, list]`, keys are column names from header
# 3. For each row, add values to proper lists in `result`
# 4. Define function `mean()`, calculating mean for arbitrary number of arguments
# 5. Return `None` if any argument to the function is not `float` or `int`
# 6. To calculate mean use built-in functions
# 7. Iterating over `result` print column name and calculated average
# 8. Run doctests - all must succeed

# Polish
# 1. Odseparuj nagłówek od wierszy danych
# 2. Zdefiniuj słownik `result: dict[str, list]`, klucze to nazwy kolumn z nagłówka
# 3. Dla każdego wiersza, dodawaj wartości do odpowiednich list w `result`
# 4. Zdefiniuj funkcję `mean()`, liczącą średnią dla dowolnej ilości argumentów
# 5. Zwróć `None` jeżeli którykolwiek z argumentów do funkcji nie jest `float` lub `int`
# 6. Do wyliczenia średniej wykorzystaj wbudowane funkcje
# 7. Iterując po `result` wypisz nazwę kolumny oraz wyliczoną średnią
# 8. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
result = ...