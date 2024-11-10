
"""
>>> import sys; sys.tracebacklimit = 0

>>> from inspect import isfunction
>>> assert isfunction(km_to_meters)

>>> assert type(km_to_meters(0)) is float
>>> assert type(km_to_meters(0.0)) is float
>>> assert type(km_to_meters(1)) is float
>>> assert type(km_to_meters(1.0)) is float

>>> km_to_meters(1)
1000.0

>>> km_to_meters(0)
0.0

>>> km_to_meters(-1)
Traceback (most recent call last):
ValueError: Argument must be not negative

>>> km_to_meters(1.0)
1000.0

>>> km_to_meters(1.5)
1500.0

>>> km_to_meters(0.0)
0.0

>>> km_to_meters(-1.0)
Traceback (most recent call last):
ValueError: Argument must be not negative

>>> km_to_meters('1')
Traceback (most recent call last):
TypeError: Invalid argument type

>>> km_to_meters([1])
Traceback (most recent call last):
TypeError: Invalid argument type

>>> km_to_meters([1.0])
Traceback (most recent call last):
TypeError: Invalid argument type

>>> km_to_meters(True)
Traceback (most recent call last):
TypeError: Invalid argument type

>>> km_to_meters(None)
Traceback (most recent call last):
TypeError: Invalid argument type
"""
