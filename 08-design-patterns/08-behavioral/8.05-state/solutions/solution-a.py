from abc import ABC, abstractmethod


class Language(ABC):
    @abstractmethod
    def hello(self) -> str: ...

    @abstractmethod
    def goodbye(self) -> str: ...


class Polish(Language):
    def goodbye(self) -> str:
        return 'Do widzenia'

    def hello(self) -> str:
        return 'Cześć'


class English(Language):
    def goodbye(self) -> str:
        return 'Goodbye'

    def hello(self) -> str:
        return 'Hello'


class Spanish(Language):
    def goodbye(self) -> str:
        return 'Buenos Días'

    def hello(self) -> str:
        return 'Adiós'


class Chinese(Language):
    def goodbye(self) -> str:
        return '再见'

    def hello(self) -> str:
        return '你好'


class Translation:
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def goodbye(self):
        return self.language.goodbye()

    def hello(self):
        return self.language.hello()


# %% Alternatively
# from abc import ABC, abstractproperty
# from dataclasses import dataclass
#
# class Language(ABC):
#     @abstractproperty
#     def hello(self) -> str: ...
#
#     @abstractproperty
#     def goodbye(self) -> str: ...
#
#
# @dataclass
# class Polish(Language):
#     hello: str = 'Cześć'
#     goodbye: str = 'Do widzenia'
#
# @dataclass
# class English(Language):
#     hello: str = 'Hello'
#     goodbye: str = 'Goodbye'
#
#
# class Translation(Language):
#     language: Language
#
#     def __init__(self, language: Language):
#         self.language = language
#
#     def hello(self):
#         return self.language.hello
#
#     def goodbye(self):
#         return self.language.goodbye