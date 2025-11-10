from abc import ABC, abstractmethod
from typing import Any


class Document(ABC):
    @property
    @abstractmethod
    def extension(self) -> Any:
        pass

    @abstractmethod
    def render(self):
        pass

    def __init__(self, *args, **kwargs):
        self.filename = args[0]

    def __new__(cls, *args, **kwargs):
        # check if at least one args is given otherwise throw exception
        if len(args) < 1:
            raise ValueError('At least one argument is required')

        name, extension = args[0].split('.')
        plugins = cls.__subclasses__()
        for plugin in plugins:
            if plugin.extension == extension:
                instance = object.__new__(plugin)
                instance.__init__(*args, **kwargs)
                return instance
        else:
            raise NotImplementedError(f'Class for extension {extension} is not implemented')

class Txt(Document):
    extension = 'txt'

    def render(self):
        return f'Rendering {self.extension} document {self.filename}'

class Pdf(Document):
    extension = 'pdf'

    def render(self):
        return f'Rendering {self.extension} document {self.filename}'

class Html(Document):
    extension = 'html'

    def render(self):
        return f'Rendering {self.extension} document {self.filename}'

if __name__ == '__main__':
    documents = ['txt', 'pdf', 'html']
    for doc in documents:
       file = Document('filename.' + doc) # type: ignore
       print(file.render())

