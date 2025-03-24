#!/usr/bin/env python3
# https://python3.info/advanced/fp-paradigm/currying.html


# %% Functional Currying
# - functools.partial()
# - functools.partialmethod()
# %%

from functools import partialmethod, partial

round2 = partial(round, ndigits=2)
numbers = [1.123, 2.3445, 3.984]
rounded_numbers = list(map(round2, numbers))
print(*rounded_numbers)

# %% Problem
# %%

class Cell:
    def __init__(self, alive: bool=True):
        self._alive = alive

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, state=True)
    set_dead = partialmethod(set_state, state=False)


c = Cell()
c.set_alive()
print(c.alive)

c.set_dead()
print(c.alive)


# %% Solution
# %%



# %% Partial
# - Create alias function and its arguments
# - Useful when you need to pass function with arguments to for example map or filter
# %%



# %% Partialmethod
# %%



