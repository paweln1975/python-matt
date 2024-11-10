
@dataclass
class Point:
    x: int
    y: int
    z: int

    def __delattr__(self, item):
        raise PermissionError('Cannot delete attributes')
