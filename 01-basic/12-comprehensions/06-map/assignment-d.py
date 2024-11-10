"""
* Assignment: Comprehension List Join
* Type: class assignment
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result: str` with
       comma-separated string from `DATA` values
    2. Non-functional requirements:
        a. Use `DATA` variable
        b. Use list comprehension
        c. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str` ze
       stringiem z oddzielonymi przecinkiem wartościami z `DATA`
    2. Non-functional requirements:
        a. Użyj zmiennej `DATA`
        b. Użyj list comprehension
        c. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * str.join()
    * str()
    * [... for ... in ...]

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'Mark,Watney,40'
"""

DATA = ['Mark', 'Watney', 40]

# Comma-separated string from `DATA` values
# type: str
result = ','.join(str(x) for x in DATA)

