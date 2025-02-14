@dataclass
class Vector:
    x: int
    y: int

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return x + y