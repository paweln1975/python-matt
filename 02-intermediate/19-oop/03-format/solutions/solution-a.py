
class Distance:
    meters: int | float

    def __init__(self, meters):
        self.meters = meters

    def __format__(self, unit):
        distance = self.meters
        match unit:
            case 'km':  distance /= KILOMETER
            case 'm':   distance /= METER
            case 'cm':  distance /= CENTIMETER
        return f'{distance:.1f} {unit}'
