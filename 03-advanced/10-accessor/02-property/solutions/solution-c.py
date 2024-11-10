
class Point:
    x: int
    y: int
    z: int
    position = property()

    @position.setter
    def position(self, value):
        if min(value) < 0:
            raise ValueError
        self.x, self.y, self.z = value
