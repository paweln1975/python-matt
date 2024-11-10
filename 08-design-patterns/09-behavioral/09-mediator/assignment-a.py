"""
* Assignment: DesignPatterns Behavioral Mediator
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    1. Implement Mediator pattern
    2. Create form with Username, Password and Submit button
    3. If Username and Password are provided enable Submit button
    4. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Mediator
    2. Stwórz formularz logowania z Username, Password i przyciskiem Submit
    3. Jeżeli Username i Password odblokuj przycisk Submit
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
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
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class UIElement(ABC):
    name: str
    owner: Form
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


