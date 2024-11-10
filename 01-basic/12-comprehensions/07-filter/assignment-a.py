"""
* Assignment: Comprehension Filter Even
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use list comprehension
    2. Generate `result: list[int]`
       of even numbers from 0 to 10 (without 10)
    3. Run doctests - all must succeed

Polish:
    1. Użyj rozwinięcia listowego
    2. Wygeneruj `result: list[int]`
       parzystych liczb z przedziału 0 do 10 (bez 10)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `range()`
    * `%`
    * `==`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is list, \
    'Result should be a list'
    >>> assert all(type(x) is int for x in result), \
    'Result should be a list of int'

    >>> result
    [0, 2, 4, 6, 8]
"""

# Even numbers from 0 to 10 (without 10)
# type: list[int]
result = [x for x in range(10) if not x % 2]

