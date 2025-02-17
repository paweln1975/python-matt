from typing import Final, Literal
#!/usr/bin/env python3
# https://python3.info/advanced/typing/advanced.html


# %% Typing Advanced
# %%



# %% Union
# - Used to inform static type checker that the variable should either X or Y
# - Since Python 3.10: :pep:604 -- Allow writing union types as X | Y
# - int | str == str | int
# - Could be with more than two types
# %%



# %% Optional
# - Used to inform static type checker that the variable should be X or None
# - Since Python 3.10: :pep:604 -- Allow writing union types as X | Y
# - int | None == None | int
# - Could be with more than two types
# %%



# %% Final
# - Used to inform static type checker the value should not change
# - Used to define constants
# - Since Python 3.8: :pep:591 -- Adding a final qualifier to typing
# %%

a: Final[int] = 10
print(a)

# %% Literal
# - Since Python 3.8: :pep:586 -- Literal Types
# - Literal de-duplicates parameters
# - Equality comparisons of Literal objects are not order dependent
# - https://docs.python.org/3/library/typing.html#typing.Literal
# %%

groups: Literal['users', 'admins', 'others']
groups = 'user'
print(groups)

# %% Any
# %%



# %% Further Reading
# - https://www.infoq.com/presentations/dynamic-static-typing/
# - https://github.com/pandas-dev/pandas/blob/8fd2d0c1eea04d56ec0a63fae084a66dd482003e/pandas/core/frame.py#L505
# %%



