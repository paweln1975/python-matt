#!/usr/bin/env python3
# https://python3.info/advanced/oop-dataclass/parameters.html


# %% Dataclass Parameters
# - init - Generate __init__() method
# - repr - Generate __repr__() method
# - eq - Generate __eq__() and __ne__() methods
# - order - Generate __lt__(), __le__(), __gt__(), and __ge__() methods
# - unsafe_hash - If False: the __hash__() method is generated according to how eq and frozen are set
# - frozen - If True: assigning to fields will generate an exception
# - match_args - Generate __match_args__() method
# - kw_only - Mark all fields as keyword-only
# - slots - Create class with __slots__
# %%



# %% Init
# - Generate __init__() method
# - Default: init=True
# %%



# %% Repr
# - Generate __repr__() method
# - Default: repr=True
# %%



# %% Order
# - Generate __lt__(), __le__(), __gt__(), and __ge__() methods
# - Default: order=False
# %%



# %% Unsafe_hash
# - Generate __hash__() method
# - Default: unsafe_hash=False
# - If False then the __hash__() method is generated according to how eq and frozen are set
# %%



# %% Match_args
# - Generate __match_args__() method
# - Default: match_args=True
# - Since Python 3.10
# %%



# %% Frozen
# - Prevents object from modifications
# - Default: frozen=False
# - If True then assigning to fields will generate an exception
# %%



# %% Kw_only
# - Mark all fields as keyword-only
# - Default: kw_only=False
# - Since Python 3.10
# %%



# %% Slots
# - Create class with __slots__
# - Default: slots=False
# - Since Python 3.10
# %%



