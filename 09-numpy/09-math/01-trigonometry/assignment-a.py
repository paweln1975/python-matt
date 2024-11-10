"""
* Assignment: Numpy Trigonometry
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Define function `trigonometry(angle_deg: int|float) -> dict`
    2. Return angle in radians and trigonometric function values (sin, cos, tg, ctg)
    3. Ctg for angle 180 and Tan for 90 degrees has infinite value, return `np.inf`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `trigonometry(angle_deg: int|float) -> dict`
    2. Zwróć kąt w radianach oraz wartości funkcji trygonometrycznych (sin, cos, tg, ctg)
    3. Ctg dla angle 180 oraz Tan dla 0 i 90 stopni ma wartość nieskończoną, zwróć `np.inf`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert trigonometry(0) is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert all(type(v) is not Ellipsis for v in trigonometry(0).values()), \
    'All values in the result must not be empty Ellipsis `...`'

    >>> trigonometry(180)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': np.float64(3.141592653589793),
     'sin': np.float64(1.2246467991473532e-16),
     'cos': np.float64(-1.0),
     'tan': inf,
     'ctg': np.float64(-8165619676597685.0)}

    >>> trigonometry(90)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': np.float64(1.5707963267948966),
     'sin': np.float64(1.0),
     'cos': np.float64(6.123233995736766e-17),
     'tan': np.float64(1.633123935319537e+16),
     'ctg': inf}

    >>> trigonometry(0)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': np.float64(0.0),
     'sin': np.float64(0.0),
     'cos': np.float64(1.0),
     'tan': np.float64(0.0),
     'ctg': inf}

    >>> trigonometry(np.pi)  # doctest: +NORMALIZE_WHITESPACE
    {'rad': np.float64(0.05483113556160755),
     'sin': np.float64(0.05480366514878953),
     'cos': np.float64(0.9984971498638638),
     'tan': np.float64(0.054886150808003326),
     'ctg': np.float64(18.21953234611204)}
"""

import numpy as np


def trigonometry(angle_deg):
    return {
        'rad': ...,
        'sin': ...,
        'cos': ...,
        'tan': ...,
        'ctg': ...,
    }


