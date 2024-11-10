"""
* Assignment: Type Float Tax
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Cost of the service is 1000.00 PLN net
    2. Service has value added tax (VAT) rate of 23%
    3. Calculate VAT tax
    4. Run doctests - all must succeed

Polish:
    1. Cena usługi wynosi 1000.00 PLN netto
    2. Usługa objęta jest 23% stawką VAT
    3. Oblicz wartości podatku VAT
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'
    >>> assert type(result) is float, \
    'Variable `result` has invalid type, should be float'

    >>> pprint(result)
    230.0
"""

PLN = 1.00
VAT_23 = 0.23

PRICE = 1000.00*PLN

# VAT tax for 1000.00 PLN net price
# type: float
result = PRICE*VAT_23

