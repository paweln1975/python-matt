"""
* Assignment: Math IEEE754 NoFix
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define variables with prices:
        a. candy = 0.10 USD
        b. cookie = 0.20 USD
    2. Define `result: float` with sum of prices for a candy and a cookie
    3. Do not fix precision error from IEEE-754
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne z cenami:
        a. cukierek (candy) = 0,10 USD
        b. ciasteczko (cookie) = 0,20 USD
    2. Zdefiniuj `result: float` z sumą cen za ciasteczko i cukierek
    3. Nie uwzględniaj poprawki na błąd precyzji wynikający z IEEE-754
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    0.30000000000000004
"""

# Define variables with prices:
# - candy = 0.10 USD
# - cookie = 0.20 USD
candy = ...
cookie = ...

# Total price for both a candy and a cookie
# Do not fix precision error from IEEE-754
# type: int
result = ...

