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
from uuid import uuid4


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
@dataclass(frozen=True)
class State:
    when: datetime = field(default_factory=datetime.now)
    uuid: str = field(default_factory=uuid4)
    data: dict | None = None

@dataclass
class Memento:
    _states: list[State] = field(default_factory=list)

    def _save(self) -> None:
        data = self.__dict__.copy()
        state = State(data=data)
        self._states.append(state)

    def _restore(self):
        if not self._states:
            raise IndexError("Memento has not been saved")
        state = self._states.pop()
        self.__dict__.update(state.data)


@dataclass
class Account(Memento):
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        self._save()
        self.balance += amount

    def undo(self):
        self._restore()