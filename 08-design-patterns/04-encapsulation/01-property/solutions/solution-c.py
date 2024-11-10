
class Point:
    x: int
    y: int
    z: int
    position = property()

    @position.setter
    def position(self, new_value):
        if all(x >= 0 for x in new_value):
            self.x, self.y, self.z = new_value
        else:
            raise ValueError
