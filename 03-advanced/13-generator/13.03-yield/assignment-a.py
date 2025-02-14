"""
Name: Generator Function Passwd
Difficulty: medium
Lines: 10
Minutes: 5

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

>>> from inspect import isfunction, isgeneratorfunction

>>> assert isfunction(function)
>>> assert isgeneratorfunction(generator)

>>> list(function(DATA))
['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']

>>> list(generator(DATA))
['root', 'bin', 'daemon', 'adm', 'shutdown', 'halt', 'nobody', 'sshd']

Hints:
`str.splitlines()`
`str.split()`
unpacking expression

"""

# %% SetUp

from typing import Callable, Generator
function: Callable[[str], list[str]]
generator: Callable[[str], Generator[str, None, None]]

DATA = """root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
nobody:x:99:99:Nobody:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
mwatney:x:1000:1000:Mark Watney:/home/mwatney:/bin/bash
mlewis:x:1001:1001:Melissa Lewis:/home/mlewis:/bin/bash
rmartinez:x:1002:1002:Rick Martinez:/home/rmartinez:/bin/bash
avogel:x:1003:1003:Alex Vogel:/home/avogel:/bin/bash
bjohanssen:x:1004:1004:Beth Johanssen:/home/bjohanssen:/bin/bash
cbeck:x:1005:1005:Chris Beck:/home/cbeck:/bin/bash"""

# English
# 1. Split `DATA` by lines and then by colon `:`
# 2. Extract system accounts (users with UID [third field] is less than 1000)
# 3. Return list of system account logins
# 4. Implement solution using function
# 5. Implement solution using generator and `yield` keyword
# 6. Run doctests - all must succeed

# Polish
# 1. Podziel `DATA` po liniach a następnie po dwukropku `:`
# 2. Wyciągnij konta systemowe (użytkownicy z UID (trzecie pole) mniejszym niż 1000)
# 3. Zwróć listę loginów użytkowników systemowych
# 4. Zaimplementuj rozwiązanie wykorzystując funkcję
# 5. Zaimplementuj rozwiązanie wykorzystując generator i słowo kluczowe `yield`
# 6. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
def function(data: str):
    ...

def generator(data: str):
    ...