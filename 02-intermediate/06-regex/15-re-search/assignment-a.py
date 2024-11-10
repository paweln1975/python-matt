"""
* Assignment: RE Search Astronauts
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Define variables with start and end position in `DATA`:
        a. `result_a: tuple[int,int]` for 'Neil Armstrong'
        b. `result_b: tuple[int,int]` for 'Buzz Aldrin'
        c. `result_c: tuple[int,int]` for 'Michael Collins'
        f. `result_d: tuple[int,int]` for 'Mark Watney'
    2. For each element return tuple i.e. `(10, 20)`
    3. If element is not present in `DATA` assign `None`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienne z pozycją startu i końca w `DATA`:
        a. `result_a: tuple[int,int]` dla 'Neil Armstrong'
        b. `result_b: tuple[int,int]` dla 'Buzz Aldrin'
        c. `result_c: tuple[int,int]` dla 'Michael Collins'
        f. `result_d: tuple[int,int]` dla 'Mark Watney'
    2. Dla każdego ciągu znaków zwracaj tuple np. `(10, 20)`
    3. Jeżeli ciąg znaków nie jest obecny w `DATA` przypisz `None`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `re.search()`
    * `re.Match.span()`

References:
    [1] Wikipedia: Apollo 11
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result_a is not Ellipsis, \
    'Assign result to variable: `result_a`'
    >>> assert type(result_a) is tuple, \
    'Variable `result_a` has invalid type, should be tuple'
    >>> assert all(type(x) is int for x in result_a), \
    'All elements in variable `result_a`, should be int'
    >>> assert len(result_a) == 2, \
    'Variable `result_a` has invalid length, should be 2'

    >>> assert result_b is not Ellipsis, \
    'Assign result to variable: `result_b`'
    >>> assert type(result_b) is tuple, \
    'Variable `result_b` has invalid type, should be tuple'
    >>> assert all(type(x) is int for x in result_b), \
    'All elements in variable `result_b`, should be int'
    >>> assert len(result_b) == 2, \
    'Variable `result_b` has invalid length, should be 2'

    >>> assert result_c is not Ellipsis, \
    'Assign result to variable: `result_c`'
    >>> assert type(result_c) is tuple, \
    'Variable `result_c` has invalid type, should be tuple'
    >>> assert all(type(x) is int for x in result_c), \
    'All elements in variable `result_c`, should be int'
    >>> assert len(result_c) == 2, \
    'Variable `result_c` has invalid length, should be 2'

    >>> assert result_d is not Ellipsis, \
    'Assign result to variable: `result_d`'
    >>> assert type(result_d) is type(None), \
    'Variable `result_d` has invalid type, should be None'

    >>> print(result_a)
    (78, 92)
    >>> print(result_b)
    (116, 127)
    >>> print(result_c)
    (562, 577)
    >>> print(result_d)
    None
"""

import re


DATA = (
    "Apollo 11 was the spaceflight that first landed humans on the Moon. "
    "Commander Neil Armstrong and lunar module pilot Buzz Aldrin formed "
    "the American crew that landed the Apollo Lunar Module Eagle on "
    "July 20, 1969, at 20:17 UTC. Armstrong became the first person to "
    "step onto the lunar surface six hours and 39 minutes later on "
    "July 21 at 02:56 UTC; Aldrin joined him 19 minutes later. They spent "
    "about two and a quarter hours together outside the spacecraft, "
    "and they collected 47.5 pounds (21.5 kg) of lunar material to bring "
    "back to Earth. Command module pilot Michael Collins flew the command "
    "module Columbia alone in lunar orbit while they were on the Moon's "
    "surface. Armstrong and Aldrin spent 21 hours, 36 minutes on the "
    "lunar surface at a site they named Tranquility Base before lifting "
    "off to rejoin Columbia in lunar orbit. "
)


# use re.search() to get 'Neil Armstrong' a (start, end) position or None
# type: tuple[int,int] | None
result_a = ...

# use re.search() to get 'Buzz Aldrin' a (start, end) position or None
# type: tuple[int,int] | None
result_b = ...

# use re.search() to get 'Michael Collins' a (start, end) position or None
# type: tuple[int,int] | None
result_c = ...

# use re.search() to get 'Mark Watney' a (start, end) position or None
# type: tuple[int,int] | None
result_d = ...


