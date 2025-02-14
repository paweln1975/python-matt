@dataclass
class Point:
    x: int
    y: int
    z: int

    def __setattr__(self, name, value):
        if name not in ('x', 'y', 'z'):
            raise PermissionError('Cannot set other attributes than x, y, z')
        if hasattr(self, name):
            raise PermissionError('Cannot modify existing attributes')
        return super().__setattr__(name, value)