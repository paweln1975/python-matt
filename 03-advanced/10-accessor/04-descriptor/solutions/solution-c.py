
class Validator:
    name: str
    min: int
    max: int

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        instance.__dict__[self.name] = None

    def __set__(self, instance, value):
        if not self.min <= value <= self.max:
            raise ValueError('Out of bounds')
        instance.__dict__[self.name] = value


class Latitude(Validator):
    min = -90.0
    max = 90.0


class Longitude(Validator):
    min = -180.0
    max = 180.0


class Elevation(Validator):
    min = -10994.0
    max = 8848.0


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
