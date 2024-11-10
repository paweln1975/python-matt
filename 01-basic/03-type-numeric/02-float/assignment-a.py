"""
* Assignment: Type Float Tax
* Type: class assignment
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Cost of the service is 1013.25 PLN net
    2. Service has value added tax (VAT) rate of 23%
    3. Calculate gross values (with tax)
    4. Run doctests - all must succeed

Polish:
    1. Cena usługi wynosi 1013.25 PLN netto
    2. Usługa objęta jest 23% stawką VAT
    3. Oblicz cenę brutto (z podatkiem)
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is float, \
    'Variable `result` has invalid type, should be float'

    >>> result = round(result, 2)
    >>> pprint(result)
    1246.3
"""

PERCENT = 100
VAT_23 = 1.23

PLN = 1
PRICE = 1013.25 * PLN

# Gross is net plus tax in PLN
# type: float
result = PRICE * VAT_23 / PLN



