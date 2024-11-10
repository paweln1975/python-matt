
from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass
