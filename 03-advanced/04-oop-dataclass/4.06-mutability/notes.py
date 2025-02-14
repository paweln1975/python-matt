#!/usr/bin/env python3
# https://python3.info/advanced/oop-dataclass/mutability.html


# %% Dataclass Mutability
# - problem with dict, list, set
# - You should not set mutable objects as a default function argument
# - field() creates new empty list for each object
# - It does not reuse reference
# - Discussion: https://github.com/ericvsmith/dataclasses/issues/3
# %%



# %% Recap
# - Function/method definition is evaluated once, when the function is defined
# - Function/method body is evaluated each time, when the function is called
# - This is how all dynamically typed languages work (JavaScript, PHP, Ruby, Perl etc).
# - You should not set mutable objects as a default function argument
# - Problem with mutable data structures like: dict, list, set
# %%



# %% Problem
# %%



# %% Solution
# - field(default_factory=lambda: [])
# %%



# %% Default Values
# - field(default_factory=lambda: ['user', 'staff', 'admins'])
# %%



# %% Default Factory
# - field(default_factory=default_groups)
# %%



# %% Short Notation
# - field(default_factory=list)
# - list is a callable object
# %%



