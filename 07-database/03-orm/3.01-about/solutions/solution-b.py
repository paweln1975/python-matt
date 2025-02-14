@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0


@dataclass
class HasPosition:
    _position: Point = Point()

    def set_position(self, x, y):
        self._position = Point(x, y)

    def get_position(self):
        return self._position

    def change_position(self, right=0, left=0, up=0, down=0):
        current = self.get_position()
        new_x = current.x + right - left
        new_y = current.y + down - up
        self.set_position(new_x, new_y)