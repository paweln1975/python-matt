#!/usr/bin/env python3
# https://python3.info/advanced/oop-paradigm/identity.html


# %% OOP Identity
# - id() will change every time you execute script
# - id() returns an integer which is guaranteed to be unique and constant for object during its lifetime
# - Two objects with non-overlapping lifetimes may have the same id() value
# - In CPython it's also the memory address of the corresponding C object
# - Since Python 3.8 - Compiler produces a SyntaxWarning when identity checks (is and is not) are used with certain types of literals (e.g. str, int). These can often work by accident in *CPython*, but are not guaranteed by the language spec. The warning advises users to use equality tests (== and !=) instead.
# - is checks for object identity
# - is compares id() output for both objects
# - CPython: compares the memory address a object resides in
# %%



# %% Builtin id()
# - id(obj) -> int - Function id() returns an integer
# - Guaranteed to be unique and constant for object during its lifetime
# - Will change every time you execute script
# - In CPython id() shows the memory address of an object
# - Returned value of id() will change every time you execute script
# %%



# %% None Type Identity
# - NoneType object is a singleton
# - It always has the same identity (during one run)
# %%



# %% Bool Type Identity
# - Bool object is a singleton
# - It always has the same identity (during one run)
# %%



# %% Int Type Identity
# - SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# - Integer interning (caching) for values from -5 to 256
# - -5 to 256 are interned (cached) and have the same id() value
# - -5 to 256 are singletons
# - -5 to 256 are preallocated in memory
# - they are never deleted from memory (during one run)
# %%



# %% Float Type Identity
# - SyntaxWarning: "is" with 'float' literal. Did you mean "=="?
# - Floats are never cached
# %%



# %% String Types Identity
# - Strings are interned only if they do not contains special characters
# - SyntaxWarning: "is" with 'float' literal. Did you mean "=="?
# %%



# %% Sequences Identity
# %%



# %% Mappings Identity
# %%



# %% Collections Identity
# %%



# %% Object Identity
# %%



# %% Class Identity
# - Class object is a singleton
# - It always has the same identity (during one run)
# %%



# %% Type Identity
# - Type object is a singleton
# %%



