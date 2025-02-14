class Validator:
    name: str
    min: int
    max: int

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not self.min <= value <= self.max:
            raise ValueError(f'Out of bounds, must be between {self.min} and {self.max}')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = None


class Latitude(Validator):
    min = -90.0
    max = 90.0


class Longitude(Validator):
    min = -180.0
    max = 180.0


class Elevation(Validator):
    min = -10994.0
    max = 8848.0


@dataclass
class GeographicCoordinate:
    latitude: float = Latitude()
    longitude: float = Longitude()
    elevation: float = Elevation()