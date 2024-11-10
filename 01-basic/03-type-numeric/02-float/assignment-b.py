"""
* Assignment: Type Float Tax
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Price of the service is 100.00 USD
    2. Define `result: float` with price in cents
    3. Run doctests - all must succeed

Polish:
    1. Cena usługi wynosi 100.00 USD
    2. Zdefiniuj `result: float` ceną w centach
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is float, \
    'Variable `result` has invalid type, should be float'

    >>> pprint(result)
    10000.0
"""

DOLLAR = 1
CENT = DOLLAR / 100

PRICE = 100*DOLLAR

# PRICE in US cents
# type: float
result = PRICE / CENT

