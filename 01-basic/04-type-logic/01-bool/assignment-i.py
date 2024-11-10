"""
* Assignment: Type Bool Or
* Type: class assignment
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. What should be substituted in expressions to get expected value?
    2. Define variables:
        a. `result_a: bool` with solution to expression `True or ... == True`
        b. `result_b: bool` with solution to expression `True or ... == False`
    2. Non-functional requirements:
        a. do not evaluate expressions in REPL or script
        b. fill in what you think is the result
        c. in place of ellipsis (`...`) insert only `True` or `False`
        d. this assignment checks if you understand the bool type
    3. Run doctests - all must succeed

Polish:
    1. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    2. Zdefiniuj zmienne:
        a. `result_a: bool` z odpowiedź do wyrażenia `True or ... == True`
        b. `result_b: bool` z odpowiedź do wyrażenia `True or ... == False`
    3. Wymagania niefunkcjonalne:
        a. nie ewaluuj wyrażeń w REPL'u ani w skrypcie Python
        b. wpisz to co Ci sie wydaje, że jest wynikiem
        c. w miejsce trzech kropek (`...`) wstawiaj tylko `True` lub `False`
        d. zadanie sprawdza, czy rozumiesz typ bool
    4. Uruchom doctesty - wszystkie muszą się powieść

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

    >>> result = True or result_a
    >>> pprint(result)
    True

    >>> result = True or result_b
    >>> pprint(result)
    True
"""

# Solution to expression `True or ... == True`
# type: bool
result_a = True

# Solution to expression `True or ... == False`
# type: bool
result_b = False

