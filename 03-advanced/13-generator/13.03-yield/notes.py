#!/usr/bin/env python3
# https://python3.info/advanced/generator/yield.html


# %% Generator Yield
# - yield keyword turns function into generator function
# %%



# %% Problem
# - Python do not execute code after function returns
# - In order to return two values from the function you must use tuple
# %%



# %% Solution
# %%



# %% Call Generator
# - Generators are called just like a regular function
# - The rule with positional and keyword arguments are identical to regular functions
# %%



# %% Result Object
# - Calling a generator will return a generator object
# - This object is an iterator
# %%



# %% Evaluate Eagerly
# %%



# %% Evaluate Lazily
# - All generators implements Iterator protocol
# - Iterator has obj.__iter__() method which enable use of iter(obj)
# - Iterator has obj.__next__() method which enable use of next(obj)
# %%



# %% Evaluate Loop
# %%



# %% Evaluate Iterator
# %%



# %% Execution
# - There can be one or many yield keywords in a generator function
# - Each yield keyword pauses the function and returns the value
# - After last yield raises StopIteration
# %%



# %% Yield from a Loop
# %%



# %% Yields from Loops
# %%



# %% Yield in a Zip Loop
# - firstnames() - generator (a stream) returning firstnames
# - lastnames() - generator (a stream) returning lastnames
# - for fname, lname in zip(firstnames(), lastnames())
# %%



