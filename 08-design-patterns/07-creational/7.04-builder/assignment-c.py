"""
Name: DesignPatterns Creational BuilderEmail
Difficulty: easy
Lines: 4
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
Terminal: `python -m doctest -v assignment-c.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> result = Email()
>>> result.with_recipient('mwatney@esa.int')
Traceback (most recent call last):
ValueError: Invalid recipient

>>> result = Email()
>>> result.with_sender('mwatney@esa.int')
Traceback (most recent call last):
ValueError: Invalid sender

>>> result = (
...     Email()
...     .with_recipient('mwatney@nasa.gov')
...     .with_sender('mlewis@nasa.gov')
...     .with_subject('Hello from Mars')
...     .with_body('Greetings from Red Planet')
... )

>>> from pprint import pprint
>>> pprint(vars(result), width=72, sort_dicts=False)
{'recipient': 'mwatney@nasa.gov',
 'sender': 'mlewis@nasa.gov',
 'subject': b'Hello from Mars',
 'body': b'Greetings from Red Planet'}

Hints:
`re.match()`

"""

# %% SetUp

import re

from typing import Callable
Email: type
with_recipient: Callable[[object, str], object]
with_sender: Callable[[object, str], object]
with_subject: Callable[[object, str], object]
with_body: Callable[[object, str], object]

# English
# 1. Create class `Email`
# 2. Use builder pattern to set:
#    - `recipient: str` verify email address using regex
#    - `sender: str` verify email address using regex
# 3. For email validation use regex pattern: `r'^[a-z]+@nasa.gov$'`
# 4. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Email`
# 2. Użyj wzorca builder, aby ustawić:
#    - `recipient: str` zweryfikuj adres e-mail za pomocą wyrażenia regularnego
#    - `sender: str` zweryfikuj adres e-mail za pomocą wyrażenia regularnego
# 3. Do walidacji email użyj wzorca regex: `r'^[a-z]+@nasa.gov$'`
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Email:
    recipient: str
    sender: str
    subject: bytes
    body: bytes

    def with_recipient(self, recipient):
        self.recipient = recipient
        return self

    def with_sender(self, sender):
        self.sender = sender
        return self

    def with_subject(self, subject):
        self.subject = subject
        return self

    def with_body(self, body):
        self.body = body
        return self