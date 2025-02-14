@dataclass
class Character:
    character_class: str
    race: str
    alignment: str
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    @property
    def stats(self) -> Stats:
        return Stats(
            strength=self.strength,
            dexterity=self.dexterity,
            constitution=self.constitution,
            intelligence=self.intelligence,
            wisdom=self.wisdom,
            charisma=self.charisma)

    @classmethod
    def from_toml(cls, filename: str, name: str):
        with open(filename, mode='rb') as file:
            characters = tomllib.load(file)
        stats = characters[name]
        return cls(**stats)


class Fighter(Character):
    pass


class WildMage(Character):
    pass


class Ranger(Character):
    pass


class Thief(Character):
    pass