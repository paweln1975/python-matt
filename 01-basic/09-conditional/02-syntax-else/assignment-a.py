"""
* Assignment: Conditional If Adult
* Type: class assignment
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. The user entered his/her age: 30
    2. Define variable `result: str` with value:
        a. 'junior' - if age is below 18
        b. 'senior' - if age is 18 or above
    3. Use if-else block
    4. Run doctests - all must succeed

Polish:
    1. Użytkownik podał swój wiek: 30
    2. Zdefiniuj zmienną `result: str` z wartością:
       a. 'junior' - jeżeli wiek jest poniżej 18 lat
       b. 'senior' - jeżeli wiek jest 18 lat lub więcej
    3. Użyj bloku if-else
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `<`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> assert result is not Ellipsis, \
    'Assign your result to variable `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> assert result in {'junior', 'senior'}, \
    'Variable `result` should be either junior or senior'

    >>> pprint(result)
    'senior'
"""

AGE = 30


# Define variable `result: str` with value:
# - 'junior' - if age is below 18
# - 'senior' - if age is 18 or above
# Use if-else block
# type: str
result = 'junior' if AGE < 18 else 'senior'


