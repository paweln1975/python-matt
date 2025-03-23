#!/usr/bin/env python3
# https://python3.info/advanced/fp-paradigm/memoization.html


# %% Functional Memoization
# %%



# %% Problem
# - Calling the same function with the same parameter
# - Requires computation every time the function is called
# %%



# %% Solution
# - Memoization - remembering function results for given parameter
# - Store information in external dict
# - key: function parameter
# - value: function call result for given parameter
# - Dicts are very fast
# %%



# %% Function Based Decorator
# %%

def my_cache(fun):
    def wrapper(n):
        if n not in wrapper.cache:
            wrapper.cache[n] = fun(n)
        return wrapper.cache[n]
    wrapper.cache = {}
    return wrapper

@my_cache
def factorial(n: int = 0):
    print(f"Calculation {n}! for {n=}")
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(10))
print(factorial(5))
print(factorial(5))
print(factorial(5))
print(factorial(2))

# %% Class Based Decorator
# %%

class Cache(dict):
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, n: int = 0):
        return self[n]

    def __missing__(self, n: int = 0):
        self[n] = self.fun(n)
        return self[n]

@Cache
def fib(n: int):
    print(f"Calculation fib({n}) for {n=}")
    return 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)

print(fib(5))

# %% Functools Cache
# - Cache with unlimited size
# %%
from functools import cache

@cache
def factorial(n: int = 0):
    print(f"Second calculation {n}! for {n=}")
    return 1 if n == 0 else n * factorial(n-1)

print(factorial(15))
print(factorial(10))

print(factorial.cache_info())

# %% Functools LRU Cache
# - Least Recently Used
# - Cache with limited size
# - from functools import lru_cache
# - @lru_cache(maxsize=None)
# %%



# %% Performance
# - Date: 2025-01-14
# - Python: 3.13.1
# - IPython: 8.31.0
# - System: macOS 15.2
# - Computer: MacBook M3 Max
# - CPU: 16 cores (12 performance and 4 efficiency) / 3nm
# - RAM: 128 GB RAM LPDDR5
# %%



