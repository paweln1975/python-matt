

#%% Interfaces
from abc import ABC, abstractmethod


class UIElement(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError

@dataclass
class Button(UIElement):
    name: str

@dataclass
class Textbox(UIElement):
    name: str

class OS(ABC):
    @abstractmethod
    def create_button(self, name: str) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_textbox(self, name: str) -> Textbox:
        raise NotImplementedError


#%% Android
class AndroidButton(Button):
    def render(self) -> None:
        print(f'Android Button {self.name}')

class AndroidTextbox(Textbox):
    def render(self) -> None:
        print(f'Android Textbox {self.name}')

class Android(OS):
    def create_button(self, name: str) -> Button:
        return AndroidButton(name)

    def create_textbox(self, name: str) -> Textbox:
        return AndroidTextbox(name)


#%% iOS
class iOSButton(Button):
    def render(self) -> None:
        print(f'iOS Button {self.name}')

class iOSTextbox(Textbox):
    def render(self) -> None:
        print(f'iOS Textbox {self.name}')

class iOS(OS):
    def create_button(self, name: str) -> Button:
        return iOSButton(name)

    def create_textbox(self, name: str) -> Textbox:
        return iOSTextbox(name)


#%% Main
class Platform(Enum):
    iOS = iOS()
    Android = Android()


def main(platform: Platform):
    os = platform.value
    os.create_textbox('username').render()
    os.create_textbox('password').render()
    os.create_button('submit').render()
