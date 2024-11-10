
class Animal:
    def __init__(self, english_name, latin_name):
        self.english_name = english_name
        self.latin_name = latin_name

    @classmethod
    def from_dict(cls, data: dict):
        english_name = data.get('english_name')
        latin_name = data.get('latin_name')
        return cls(english_name, latin_name)


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Platypus(Animal):
    pass
