#!/usr/bin/env python3
# https://python3.info/advanced/generator/yield-from.html


# %% Generator Yield From
# - Since Python 3.3: :pep:380 -- Syntax for Delegating to a Subgenerator
# - Helps with refactoring generators
# - Useful for large generators which can be split into smaller ones
# - Delegation call
# - yield from terminates on GeneratorExit from other function
# - The value of the yield from expression is the first argument to the StopIteration exception raised by the iterator when it terminates
# - Return expr in a generator causes StopIteration(expr) to be raised upon exit from the generator
# %%



# %% Problem
# %%



# %% Solution
# - yield from
# %%



# %% Rationale
# %%



# %% Execute
# %%



# %% Itertools Chain
# %%



# %% Yield From Sequences
# %%



# %% Yield From Comprehensions
# %%



# %% Yield From Functions
# - Delegation call
# %%



# %% Conclusion
# - Python yield keyword creates a generator function.
# - It's useful when the function returns a large amount of data by splitting it into multiple chunks.
# - We can also send values to the generator using its send() function.
# - The yield from statement is used to create a sub-iterator from the generator function.
# %%



