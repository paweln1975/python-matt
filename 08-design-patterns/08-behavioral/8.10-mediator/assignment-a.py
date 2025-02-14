"""
Name: DesignPatterns Behavioral Mediator
Difficulty: medium
Lines: 15
Minutes: 21

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

>>> form = LoginForm()
>>> form.set_username('mwatney')
>>> form.set_password('')
>>> form.submit()
Traceback (most recent call last):
PermissionError: Cannot submit form without Username and Password

>>> form = LoginForm()
>>> form.set_username('mwatney')
>>> form.set_password('Ares3')
>>> form.submit()
'Submitted'

"""

# %% SetUp

from typing import Any
from abc import ABC, abstractmethod
from dataclasses import dataclass

# English
# 1. Implement Mediator pattern
# 2. Create form with Username, Password and Submit button
# 3. If Username and Password are provided enable Submit button
# 4. Run doctests - all must succeed

# Polish
# 1. Zaimplementuj wzorzec Mediator
# 2. Stwórz formularz logowania z Username, Password i przyciskiem Submit
# 3. Jeżeli Username i Password odblokuj przycisk Submit
# 4. Uruchom doctesty - wszystkie muszą się powieść

# %% Result
@dataclass
class UIElement(ABC):
    name: str
    owner: 'Form'
    value: Any

    def changed(self):
        raise NotImplementedError

    @abstractmethod
    def set_value(self, value: Any) -> None: ...

    @abstractmethod
    def get_value(self) -> Any: ...

@dataclass
class Input(UIElement):
    value: str = ''

    def get_value(self) -> str:
        raise NotImplementedError

    def set_value(self, value: str) -> None:
        raise NotImplementedError

@dataclass
class Button(UIElement):
    value: bool = False

    def set_value(self, value: bool) -> None:
        raise NotImplementedError

    def get_value(self) -> Any:
        raise NotImplementedError

    def enable(self):
        self.set_value(True)

    def disable(self):
        self.set_value(False)

    def is_enabled(self) -> bool:
        return self.value

class Form(ABC):
    @abstractmethod
    def on_change(self): ...

class LoginForm(Form):
    username_input: Input
    password_input: Input
    submit_button: Button

    def __init__(self):
        raise NotImplementedError

    def set_username(self, username: str):
        raise NotImplementedError

    def set_password(self, password: str):
        raise NotImplementedError

    def on_change(self):
        raise NotImplementedError

    def submit(self):
        if self.submit_button.is_enabled():
            return 'Submitted'
        else:
            raise PermissionError('Cannot submit form without Username and Password')