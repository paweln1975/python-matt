class ValueRange:
    name: str
    min: float
    max: float

    def __init__(self, min, max):
        self.max = max
        self.min = min

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not self.min <= value <= self.max:
            raise ValueError(f'{self.name} is not between {self.min} and {self.max}')
        instance.__dict__[self.name] = value


@dataclass
class User:
    firstname: str
    lastname: str
    age: int = ValueRange(min=18, max=65)
    height: float = ValueRange(min=150, max=200)
    weight: float = ValueRange(min=50, max=150)