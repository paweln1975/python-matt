
class Point:
    def __new__(cls, x, y):
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
