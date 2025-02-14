@dataclass
class UIElement(ABC):
    name: str
    owner: Form
    value: Any

    def changed(self):
        self.owner.on_change()

    @abstractmethod
    def set_value(self, value: Any) -> None: ...

    @abstractmethod
    def get_value(self) -> Any: ...


@dataclass
class Input(UIElement):
    value: str = ''

    def get_value(self) -> str:
        return self.value

    def set_value(self, value: str) -> None:
        self.value = value
        self.changed()


@dataclass
class Button(UIElement):
    value: bool = False

    def set_value(self, value: bool) -> None:
        self.value = value

    def get_value(self) -> Any:
        return self.value

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
        self.username_input = Input('Username', self)
        self.password_input = Input('Password', self)
        self.submit_button = Button('Submit', self)

    def set_username(self, username: str):
        self.username_input.set_value(username)

    def set_password(self, password: str):
        self.password_input.set_value(password)

    def on_change(self):
        username = self.username_input.get_value()
        password = self.password_input.get_value()
        if username and password:
            self.submit_button.enable()

    def submit(self):
        if self.submit_button.is_enabled():
            return 'Submitted'
        else:
            raise PermissionError('Cannot submit form without Username and Password')