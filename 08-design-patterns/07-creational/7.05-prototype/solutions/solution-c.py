@dataclass
class Dragon:
    name: str
    position: tuple[int,int] = (0,0)
    health: int = field(default_factory=lambda: randint(50, 100))
    gold: int = field(default_factory=lambda: randint(1, 100))

    def clone(self):
        return Dragon(**vars(self))