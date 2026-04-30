import random
from typing import ClassVar


class Dragon:
    DAMAGE_MIN: ClassVar[int] = 5
    DAMAGE_MAX: ClassVar[int] = 20
    INITIAL_HEALTH_MIN: ClassVar[int] = 50
    INITIAL_HEALTH_MAX: ClassVar[int] = 100
    name: str
    health: int
    _pos_x: int
    _pos_y: int

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = value

    def __init__(self, name: str, /, *, pos_x: int = 0, pos_y: int = 0) -> None:
        self.name: str = name
        self._health: int = random.randint(self.INITIAL_HEALTH_MIN, self.INITIAL_HEALTH_MAX)
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y

    def take_damage(self, damage: int, /) -> None:
        self._health = max(0, self._health - damage)

    def is_dead(self) -> bool:
        return self._health == 0

    def get_position(self) -> tuple[int, int]:
        return self._pos_x, self._pos_y

    def set_position(self, *, pos_x: int = 0, pos_y: int = 0) -> None:
        self._pos_x = pos_x
        self._pos_y = pos_y

    def move(self, *, up: int = 0, down: int = 0, left: int = 0, right: int = 0) -> None:
        if self.is_dead():
            raise ValueError("Cannot move a dead dragon")
        self._pos_x += right - left
        self._pos_y += down - up

    def make_damage(self) -> int:
        return random.randint(self.DAMAGE_MIN, self.DAMAGE_MAX)

