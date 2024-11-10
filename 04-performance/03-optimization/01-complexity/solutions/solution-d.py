
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')
    return sum(args) / len(args)

# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     if not args:
# ...         return 0
# ...     return sum(args) / len(args)
# ...
# ... mean()
# Python 3.10: 165 ns ± 28.5 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
# Python 3.11: 124 ns ± 26.1 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     if len(args) == 0:
# ...         return 0
# ...     return sum(args) / len(args)
# ...
# ... mean()
# Python 3.10: 174 ns ± 29.2 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)
# Python 3.11: 143 ns ± 32 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

# >>> %%timeit -r 1000 -n 1000
# ... def mean(*args):
# ...     try:
# ...         return sum(args) / len(args)
# ...     except ZeroDivisionError:
# ...         return 0
# ...
# ... mean()
# Python 3.10: 395 ns ± 65.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)
# Python 3.11: 436 ns ± 67 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

# https://docs.python.org/dev/whatsnew/3.11.html#optimizations
# "Zero-cost" exceptions are implemented.
# The cost of try statements is almost eliminated when no exception is raised.
