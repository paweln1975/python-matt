from abc import ABC, abstractmethod

class Localizer(ABC):
    @abstractmethod
    def localize(self, msg):
        pass

class EnglishLocalizer(Localizer):
    def localize(self, msg):
        return msg


class SpanishLocalizer(Localizer):
    def __init__(self):
        self.translations = {
            'car': 'coache',
            'bike': 'bicicleta',
            'cycle': 'ciclo'
        }
    def localize(self, msg):
        return self.translations[msg]

def create_localizer(language = 'english'):
    localizers = {
        'english': EnglishLocalizer,
        'spanish': SpanishLocalizer
    }
    return localizers[language]()

for language in ('english', 'spanish'):
    localizer = create_localizer(language)

    messages = ['car', 'bike', 'cycle']

    for msg in messages:
        print(localizer.localize(msg))
