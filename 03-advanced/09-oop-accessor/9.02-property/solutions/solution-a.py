class Point:
    x: int
    y: int
    z: int
    position = property()

    @position.deleter
    def position(self):
        self.x = 0
        self.y = 0
        self.z = 0