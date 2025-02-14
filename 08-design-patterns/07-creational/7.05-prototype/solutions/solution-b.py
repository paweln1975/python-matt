@dataclass
class Time:
    hour: int = 0
    minute: int = 0
    second: int = 0
    microsecond: int = 0

    def clone(self):
        return Time(**vars(self))