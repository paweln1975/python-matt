"""
>>> import sys; sys.tracebacklimit = 0

>>> from inspect import isfunction
>>> assert isfunction(celsius_to_kelvin)

>>> celsius_to_kelvin(0)
273.15

>>> celsius_to_kelvin(1)
274.15

>>> celsius_to_kelvin(-1)
272.15

>>> celsius_to_kelvin(-273.15)
0.0

>>> celsius_to_kelvin(-273.15000000001)
Traceback (most recent call last):
ValueError: Argument must be not less than -273.15

>>> celsius_to_kelvin(0.0)
273.15

>>> celsius_to_kelvin(1.0)
274.15

>>> celsius_to_kelvin([0, 1])
[273.15, 274.15]

>>> celsius_to_kelvin((0, 1))
(273.15, 274.15)

>>> celsius_to_kelvin({0, 1})
{273.15, 274.15}
"""