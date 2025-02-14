#!/usr/bin/env python3
# https://python3.info/advanced/typing/type.html


# %% Typing Type
# - All classes are types
# %%



# %% Instance
# %%



# %% Inheritance
# - Dependency Inversion Principle
# - Always depend upon abstraction not an implementation
# - More information in OOP SOLID
# %%



# %% Instance Variables
# %%



# %% Class Variables
# - ClassVar indicates that a given attribute is intended to be used as a class variable and should not be set on instances of that class.
# - https://docs.python.org/3/library/typing.html#typing.ClassVar
# %%



# %% Method Return Type
# %%



# %% Required Method Arguments
# %%



# %% Optional Method Arguments
# %%



# %% Init Method
# %%



# %% Composition
# %%



# %% Aggregation
# %%



# %% Forward Reference Problem
# %%



# %% Forward Reference Solution: Str
# - Annotations can be a str
# %%



# %% Forward Reference Solution: Future Annotations
# - Since Python 3.7
# - from __future__ import annotations
# %%



# %% Forward Reference Solution: Self
# - Since 3.11: :pep:673 - Self Type
# %%



# %% Final Class
# - Since Python 3.8: :pep:591 -- Adding a final qualifier to typing
# - There is no runtime checking of these properties
# %%



# %% Final Method
# - Since Python 3.8: :pep:591 -- Adding a final qualifier to typing
# - There is no runtime checking of these properties
# %%



# %% Final Attribute
# - A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass
# - There is no runtime checking of these properties
# - https://docs.python.org/3/library/typing.html#typing.Final
# %%



# %% Override
# - Method need to be overriden in child class
# %%



# %% Overload
# - Signs that a method is overloaded on purpose
# - It is not a mistake, that it has the same name as in base class
# %%



# %% Override and Overload
# %%



# %% Recap
# - Type annotations
# - Type hints
# - Optional, but a good practice
# - Python does not verify if values have correct types
# - IDEs such as PyCharm, VS Code or tools such as mypy can do that
# %%



