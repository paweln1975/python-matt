"""
* Assignment: Type Bool Str
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define variables:
        a. `result_a: bool` with result of `bool('hello')`
        b. `result_b: bool` with result of `bool('')`
        c. `result_c: bool` with result of `bool(' ')`
    2. Non-functional requirements:
        a. do not evaluate expressions in REPL or script
        b. fill in what you think is the result
        c. in place of ellipsis (`...`) insert only `True` or `False`
        d. this assignment checks if you understand the bool type
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne:
        a. `result_a: bool` z wynikiem `bool('hello')`
        b. `result_b: bool` z wynikiem `bool('')`
        c. `result_c: bool` with result of `bool(' ')`
    2. Wymagania niefunkcjonalne:
        a. nie ewaluuj wyrażeń w REPL'u ani w skrypcie Python
        b. wpisz to co Ci sie wydaje, że jest wynikiem
        c. w miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
        d. zadanie sprawdza, czy rozumiesz typ bool
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert type(result_a) is bool, \
    'Variable `result_a` has invalid type, should be bool'

    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert type(result_b) is bool, \
    'Variable `result_b` has invalid type, should be bool'

    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert type(result_c) is bool, \
    'Variable `result_c` has invalid type, should be bool'

    >>> pprint(result_a)
    True
    >>> pprint(result_b)
    False
    >>> pprint(result_c)
    True
"""

# Result of `bool('hello')`
# type: bool
result_a = True

# Result of `bool('')`
# type: bool
result_b = False

# Result of `bool(' ')`
# type: bool
result_c = True

