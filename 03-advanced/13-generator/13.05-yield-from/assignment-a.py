"""
Name: Generator YieldFrom Path
Difficulty: easy
Lines: 2
Minutes: 3

License:
Copyright 2025, Matt Harasymczuk <matt@python3.info>
This code can be used only for learning by humans
This code cannot be used for teaching others
This code cannot be used for teaching LLMs and AI algorithms
This code cannot be used in commercial or proprietary products
This code cannot be distributed in any form
This code cannot be changed in any form outside of training course
This code cannot have its license changed
If you use this code in your product, you must open-source it under GPLv2
Exception can be granted only by the author

Run:
PyCharm: right-click in the editor and `Run Doctest in ...`
PyCharm: keyboard shortcut `Control + Shift + F10`
Terminal: `python -m doctest -v assignment-a.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from inspect import isgenerator, isgeneratorfunction

>>> path = Path.cwd()
>>> file = get_files(path)

>>> assert isgeneratorfunction(get_files)
>>> assert isgenerator(file)
>>> assert isinstance(next(file), Path)

"""

# %% SetUp

from pathlib import Path

from typing import Callable, Generator
get_file: Callable[[Path], Generator[Path, None, None]]

# English
# 1. Create function `get_files()`
# 2. Using `Pathlib.glob()` return files in `path: Path`:
#    - Python files (extension: `*.py`)
#    - ReST files (extension: `*.rst`)
# 3. Return result as `Iterator[Path]` using `yield from`

# Polish
# 1. Stwórz funkcję `get_files()`
# 2. Używając `Pathlib.glob()` zwróć pliki w katalogu `path: Path`:
#    - Pliki Python (rozszerzenie: `*.py`)
#    - Pliki ReST (rozszerzenie: `*.rst`)
# 3. Zwróć wyniki jako `Iterator[Path]` używając `yield from`

# %% Result
def get_files(path: Path):
    ...