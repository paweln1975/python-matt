
class Point:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
