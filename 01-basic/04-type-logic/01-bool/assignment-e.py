"""
* Assignment: Type Bool StrTrueFalse
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define variables:
        a. `result_d: bool` with result of `bool('0')`
        b. `result_e: bool` with result of `bool('0.0')`
        c. `result_f: bool` with result of `bool('False')`
        d. `result_f: bool` with result of `bool('None')`
    2. Non-functional requirements:
        a. do not evaluate expressions in REPL or script
        b. fill in what you think is the result
        c. in place of ellipsis (`...`) insert only `True` or `False`
        d. this assignment checks if you understand the bool type
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne:
        a. `result_d: bool` with result of `bool('0')`
        b. `result_e: bool` with result of `bool('0.0')`
        c. `result_f: bool` with result of `bool('False')`
        d. `result_f: bool` with result of `bool('None')`
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

    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'
    >>> assert type(result_d) is bool, \
    'Variable `result_d` has invalid type, should be bool'

    >>> pprint(result_a)
    True
    >>> pprint(result_b)
    True
    >>> pprint(result_c)
    True
    >>> pprint(result_d)
    True
"""

# Result of `bool('0')`
# type: bool
result_a = True

# Result of `bool('0.0')`
# type: bool
result_b = True

# Result of `bool('False')`
# type: bool
result_c = True

# Result of `bool('None')`
# type: bool
result_d = True

