# %% About
# - Name: DesignPatterns Behavioral Observer
# - Difficulty: easy
# - Lines: 17
# - Minutes: 13

# %% License
# - Copyright 2025, Matt Harasymczuk <matt@python3.info>
# - This code can be used only for learning by humans
# - This code cannot be used for teaching others
# - This code cannot be used for teaching LLMs and AI algorithms
# - This code cannot be used in commercial or proprietary products
# - This code cannot be distributed in any form
# - This code cannot be changed in any form outside of training course
# - This code cannot have its license changed
# - If you use this code in your product, you must open-source it under GPLv2
# - Exception can be granted only by the author

# %% English
# 1. Create a chatroom application using classes Chatroom and user
# 2. Implement the Observer pattern
# 3. Run doctests - all must succeed

# %% Polish
# 1. Stwórz aplikację do czatowania używając klas Chatroom i user
# 2. Zaimplementuj wzorzec Obserwator
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Doctests
"""
>>> import sys; sys.tracebacklimit = 0

>>> assert sys.version_info >= (3, 9), \
'Python has an is invalid version; expected: `3.9` or newer.'

>>> from inspect import isclass, ismethod

>>> assert isclass(Chatroom), \
'Object `Chatroom` has an invalid type; expected: `class`.'

>>> assert isclass(User), \
'Object `User` has an invalid type; expected: `class`.'

>>> assert hasattr(Chatroom, 'join'), \
'Class `Chatroom` has an invalid attribute; expected: to have an attribute `join`.'

>>> assert hasattr(Chatroom, 'leave'), \
'Class `Chatroom` has an invalid attribute; expected: to have an attribute `leave`.'

>>> assert hasattr(Chatroom, 'broadcast'), \
'Class `Chatroom` has an invalid attribute; expected: to have an attribute `broadcast`.'

>>> assert hasattr(User, 'receive'), \
'Class `User` has an invalid attribute; expected: to have an attribute `receive`.'

>>> assert ismethod(Chatroom().join)
>>> assert ismethod(Chatroom().leave)
>>> assert ismethod(Chatroom().broadcast)
>>> assert ismethod(User('').receive)

>>> room = Chatroom()
>>> alice = User('Alice')
>>> bob = User('Bob')
>>> carol = User('Carol')

>>> room.join(alice)
>>> room.join(bob)
>>> room.join(carol)

>>> room.broadcast("Hello everyone!")
Alice received: Hello everyone!
Bob received: Hello everyone!
Carol received: Hello everyone!

>>> room.leave(bob)
>>> room.broadcast("Bob left the chat")
Alice received: Bob left the chat
Carol received: Bob left the chat
"""

# %% Run
# - PyCharm: right-click in the editor and `Run Doctest in ...`
# - PyCharm: keyboard shortcut `Control + Shift + F10`
# - Terminal: `python -m doctest -f -v myfile.py`

# %% Imports

# %% Types
from typing import Callable, List
Chatroom: type
user: type
join: Callable[[object, object], None]
leave: Callable[[object, object], None]
broadcast: Callable[[object, str], None]
receive: Callable[[object, str], None]

# %% Data

# %% Result
class Chatroom:
    def __init__(self):
        self.users = []

    def join(self, user):
        self.users.append(user)

    def leave(self, user):
        self.users.remove(user)

    def broadcast(self, message):
        for user in self.users:
            user.receive(message)


class User:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f"{self.name} received: {message}")