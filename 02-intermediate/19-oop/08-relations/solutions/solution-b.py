
class Position:
    def __init__(self):
        self.position = Point()

    def get_position(self) -> Point:
        return self.position

    def set_position(self, x: int, y: int) -> None:
        self.position = Point(x, y)

    def change_position(self, left: int = 0, right: int = 0, up: int = 0, down: int = 0) -> None:
        current = self.get_position()
        new_x = current.x + right - left
        new_y = current.y + down - up
        self.set_position(new_x, new_y)
