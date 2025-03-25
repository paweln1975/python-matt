"""
factorial function Be sure to use recursion.
"""

def factorial(n: int) -> int:
    """
    >>> import sys; sys.tracebacklimit = 0
    >>> factorial(5)
    120
    >>> factorial(2)
    2
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    >>> factorial(-1)
    Traceback (most recent call last):
    ValueError: The provided parameter should be at least 0.
    """
    if n < 0:
        raise ValueError('The provided parameter should be at least 0.')
    return 1 if n <= 1 else n * factorial(n-1)