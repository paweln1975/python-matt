"""
* Assignment: Type Float Tax
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Cost of the service is 100.00 EUR
    2. Calculate price in Polish Zloty PLN (PLN)
    3. Calculate price in US Dollars (USD)
    4. Calculate price in Australian Dollars (AUD)
    5. Calculate price in Canadian Dollars (CAD)
    3. Run doctests - all must succeed

Polish:
    1. Cena usługi wynosi 100.00 EUR
    2. Oblicz kwotę w polskich złotych (PLN)
    3. Oblicz kwotę w dolarach amerykańskich (USD)
    4. Oblicz kwotę w dolarach australijskich (AUD)
    5. Oblicz kwotę w dolarach kanadyjskich (CAD)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result_a is not Ellipsis, \
    'Assign your result to variable `result_a`'
    >>> assert type(result_a) is float, \
    'Variable `result_a` has invalid type, should be float'

    >>> assert result_b is not Ellipsis, \
    'Assign your result to variable `result_b`'
    >>> assert type(result_b) is float, \
    'Variable `result_b` has invalid type, should be float'

    >>> assert result_c is not Ellipsis, \
    'Assign your result to variable `result_c`'
    >>> assert type(result_c) is float, \
    'Variable `result_c` has invalid type, should be float'

    >>> assert result_d is not Ellipsis, \
    'Assign your result to variable `result_d`'
    >>> assert type(result_d) is float, \
    'Variable `result_d` has invalid type, should be float'

    >>> result = round(result_a, 1)
    >>> pprint(result)
    435.0

    >>> result = round(result_b, 1)
    >>> pprint(result)
    110.0

    >>> result = round(result_c, 1)
    >>> pprint(result)
    166.0

    >>> result = round(result_d, 1)
    >>> pprint(result)
    149.0
"""

EUR = 1
PLN = EUR / 4.35
USD = EUR / 1.10
AUD = EUR / 1.66
CAD = EUR / 1.49

PRICE = 100*EUR

# PRICE in Polish Zloty PLN (PLN)
# type: float
result_a = PRICE/PLN

# PRICE in US Dollars (USD)
# type: float
result_b = PRICE/USD

# PRICE in Australian Dollars (AUD)
# type: float
result_c = PRICE/AUD

# PRICE in Canadian Dollars (CAD)
# type: float
result_d = PRICE/CAD

