
class Hero:
    def __init__(self, name, health=None):
        self.name = name
        self.health = randint(50, 100) if health is None else health
