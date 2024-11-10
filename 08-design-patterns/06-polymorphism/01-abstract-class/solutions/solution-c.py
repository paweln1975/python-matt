
class Account(ABC):
    username: str
    password: str

    @abstractmethod
    def __init__(self, username: str, password: str) -> None:
        ...

    @abstractmethod
    def login(self) -> None:
        ...

    @abstractmethod
    def logout(self) -> None:
        ...
