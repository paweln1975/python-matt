class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 10

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            raise self.IsDead

    class IsDead(Exception):
        pass