#!/usr/bin/env python3
# https://python3.info/advanced/typing/package-check.html


# %% Typing Check
# - mypy - the reference implementation for type checkers
# - pyre - written in OCaml and optimized for performance
# - pyright - a type checker that emphasizes speed
# - pytype - checks and infers types for unannotated code
# %%



# %% Python
# - https://docs.python.org/dev/howto/annotations.html
# - from inspect import get_annotations - preferred before Python 3.14
# - from annotationlib import get_annotations - preferred since Python 3.14 (PEP-649)
# - from typing import get_type_hints
# - object.__annotations__ - will change behavior in Python 3.14 (PEP-649)
# - https://docs.python.org/dev/whatsnew/3.14.html#pep-649-deferred-evaluation-of-annotations
# %%



# %% MyPy
# - By community
# - https://github.com/python/mypy
# - https://mypy-lang.org/
# %%



# %% PyType
# - By Google
# - Pytype checks and infers types for your Python code - without requiring type annotations
# - https://github.com/google/pytype
# - https://pypi.org/project/pytype/
# %%



# %% Pyright
# - By Microsoft
# - https://github.com/microsoft/pyright
# %%



# %% Pyre
# - By Facebook
# - Pyre is a performant type checker for Python compliant with PEP 484. Pyre can analyze codebases with millions of lines of code incrementally – providing instantaneous feedback to developers as they write code
# - https://pyre-check.org/
# - https://pypi.org/project/pyre-check/
# %%



