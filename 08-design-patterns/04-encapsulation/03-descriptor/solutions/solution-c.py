
from dataclasses import dataclass


@dataclass
class Validator:
    min: float = None
    max: float = None
    name: str = None

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not (self.min <= value <= self.max):
            raise ValueError('Out of bounds')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __delete__(self, instance):
        instance.__dict__[self.name] = None

@dataclass
class Latitude(Validator):
    min: float = -90.0
    max: float = 90.0

@dataclass
class Longitude(Validator):
    min: float = -180.0
    max: float = 180.0

@dataclass
class Elevation(Validator):
    min: float = -10994.0
    max: float = 8848.0


class GeographicCoordinate:
    latitude = Latitude()
    longitude = Longitude()
    elevation = Elevation()

    def __init__(self, latitude, longitude, elevation):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation

    def __str__(self):
        return f'Latitude: {self.latitude}, ' + \
               f'Longitude: {self.longitude}, ' + \
               f'Elevation: {self.elevation}'

    def __repr__(self):
        return self.__str__()
