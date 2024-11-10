"""
* Assignment: Math IEEE754 IntFix
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Define variables with prices:
        a. candy = 0.10 USD
        b. cookie = 0.20 USD
    2. Define `result: float` with sum of prices for a candy and a cookie
    3. Fix precision error from IEEE-754
    4. Use `int` type for that reason
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne z cenami:
        a. cukierek (candy) = 0,10 USD
        b. ciasteczko (cookie) = 0,20 USD
    2. Zdefiniuj `result: float` z sumą cen za ciasteczko i cukierek
    3. Uwzględnij poprawkę na błąd precyzji wynikający z IEEE-754
    4. W tym celu wykorzystaj typ `int`
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result
    0.3
"""

CENT = 1
DOLLAR = 100*CENT

# Define variables with prices:
# - candy = 0.10 USD
# - cookie = 0.20 USD
candy = ...
cookie = ...

# Total price for both a candy and a cookie
# Fix precision error from IEEE-754
# Use `int` type for that reason
# type: int
result = ...


