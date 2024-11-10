

class ValueRange:
    name: str
    min: float
    max: float

    def __init__(self, name, min, max):
        self.name = name
        self.max = max
        self.min = min

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not self.min <= value <= self.max:
            raise ValueError(f'{self.name} is not between {self.min} and {self.max}')
        setattr(instance, self.name, value)


class User:
    age = ValueRange('Age', min=28, max=42)
    height = ValueRange('Height', min=150, max=200)

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
