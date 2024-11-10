"""
* Assignment: DesignPatterns Behavioral Memento
* Complexity: medium
* Lines of code: 29 lines
* Time: 13 min

English:
    1. Implement Memento pattern
    2. Create account history of transactions with:
        a. `when: datetime` - date and time of a transaction
        b. `amount: float` - transaction amount
    3. Allow for transaction undo
    4. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Memento
    2. Stwórz historię transakcji na koncie z:
        a. `when: datetime` - data i czas transakcji
        b: `amount: float` - kwota transakcji
    3. Pozwól na wycofywanie (undo) transakcji
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
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

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Account:
    balance: float = 0.0

    def deposit(self, amount: float) -> None:
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


