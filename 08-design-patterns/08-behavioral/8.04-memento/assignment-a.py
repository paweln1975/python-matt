"""
Name: DesignPatterns Behavioral Memento
Difficulty: medium
Lines: 29
Minutes: 13

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

>>> account = Account()

>>> account.deposit(100.00)
>>> account.balance
100.0

>>> account.deposit(50.00)
>>> account.balance
150.0

>>> account.deposit(25.00)
>>> account.balance
175.0

>>> account.undo()
>>> account.balance
150.0

"""

# %% SetUp

from dataclasses import dataclass, field
from datetime import datetime

# English
# 1. Implement Memento pattern
# 2. Create account history of transactions with:
#    - `when: datetime` - date and time of a transaction
#    - `amount: float` - transaction amount
# 3. Allow for transaction undo
# 4. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj wzorzec Memento
# 2. Stwórz historię transakcji na koncie z:
#    - `when: datetime` - data i czas transakcji
#         b: `amount: float` - kwota transakcji
# 3. Pozwól na wycofywanie (undo) transakcji
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class Account:
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError