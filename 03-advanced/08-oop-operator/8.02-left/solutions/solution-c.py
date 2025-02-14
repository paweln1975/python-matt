@dataclass
class Vector:
    x: int
    y: int

    def __matmul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return Vector(new_x, new_y)