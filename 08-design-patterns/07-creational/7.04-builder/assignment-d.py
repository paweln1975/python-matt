"""
Name: DesignPatterns Creational BuilderEmail
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
Terminal: `python -m doctest -v assignment-d.py`

Tests:
>>> import sys; sys.tracebacklimit = 0
>>> assert sys.version_info >= (3, 9), \
'Python 3.9+ required'

>>> from pprint import pprint

>>> result = (
...     Email()
...     .with_recipient('mwatney@nasa.gov')
...     .with_sender('mlewis@nasa.gov')
...     .with_subject('Hello from Mars')
...     .with_body('Greetings from Red Planet')
...     .with_attachment(b'myfile.txt')
... )

>>> pprint(vars(result), width=72, sort_dicts=False)
{'recipient': 'mwatney@nasa.gov',
 'sender': 'mlewis@nasa.gov',
 'subject': b'Hello from Mars',
 'body': b'Greetings from Red Planet',
 'attachment': b'bXlmaWxlLnR4dA=='}

"""

# %% SetUp

import re
from base64 import b64encode

from typing import Callable
Email: type
with_recipient: Callable[[object, str], object]
with_sender: Callable[[object, str], object]
with_subject: Callable[[object, str], object]
with_body: Callable[[object, str], object]
with_attachment: Callable[[object, bytes], object]

# English
# 1. Create class `Email`
# 2. Use builder pattern to set:
#    - `attachment: bytes` base64 encoded
# 3. Run doctests - all must succeed

# Polish
# 1. Stwórz klasę `Email`
# 2. Użyj wzorca builder, aby ustawić:
#    - `attachment: bytes` zakodowane w standardzie base64
# 3. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
class Email:
    recipient: str
    sender: str
    subject: bytes
    body: bytes
    attachment: bytes

    def with_recipient(self, recipient: str):
        if not re.match(r'^[a-z]+@nasa.gov$', recipient):
            raise ValueError(f'Invalid recipient')
        self.recipient = recipient
        return self

    def with_sender(self, sender: str):
        if not re.match(r'^[a-z]+@nasa.gov$', sender):
            raise ValueError(f'Invalid sender')
        self.sender = sender
        return self

    def with_subject(self, subject):
        self.subject = subject.encode()
        return self

    def with_body(self, body):
        self.body = body.encode()
        return self

    def with_attachment(self, attachment):
        ...