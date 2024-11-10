"""
* Assignment: Type Int Bits
* Type: homework
* Complexity: medium
* Lines of code: 3 lines
* Time: 3 min

English:
    1. File size is 1337 megabits [Mb]
    2. Calculate size in bits [b]
    3. Calculate size in kilobits [kb]
    4. Use floordiv (`//`) operator
    5. Run doctests - all must succeed

Polish:
    1. Wielkość pliku to 1337 megabits [Mb]
    2. Oblicz wielkość w bitach [b]
    3. Oblicz wielkość w kilobitach [kb]
    4. Użyj operatora floordiv (`//`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Divide (floordiv)
    * 1 kb = 1024 b
    * 1 Mb = 1024 Kb

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert size_bits is not Ellipsis, \
    'Assign your result to variable `size_bits`'
    >>> assert size_kilobits is not Ellipsis, \
    'Assign your result to variable `size_kilobits`'
    >>> assert size_megabits is not Ellipsis, \
    'Assign your result to variable `size_megabits`'
    >>> assert type(size_bits) is int, \
    'Variable `size_bits` has invalid type, should be int'
    >>> assert type(size_kilobits) is int, \
    'Variable `size_kilobits` has invalid type, should be int'
    >>> assert type(size_megabits) is int, \
    'Variable `size_megabits` has invalid type, should be int'

    >>> assert size_bits == 1_401_946_112, \
    'Invalid value for `size_bits`. Check you calculation'
    >>> assert size_kilobits == 1_369_088, \
    'Invalid value for `size_kilobits`. Check you calculation'
    >>> assert size_megabits == 1337, \
    'Invalid value for `size_megabits`. Check you calculation'
"""

b = 1
kb = 1024 * b
Mb = 1024 * kb

SIZE = 1337 * Mb

# SIZE in bits
# Use floordiv (`//`) operator
# type: int
size_bits = SIZE // b

# SIZE in kilobits
# Use floordiv (`//`) operator
# type: int
size_kilobits = SIZE // kb

# SIZE in megabits
# Use floordiv (`//`) operator
# type: int
size_megabits = SIZE // Mb

