class Point:
    x: int
    y: int
    z: int
    position = property()

    @position.setter
    def position(self, new_value):
        if type(new_value) not in (list, tuple, set):
            raise TypeError
        elif len(new_value) != 3:
            raise ValueError
        else:
            self.x, self.y, self.z = new_value