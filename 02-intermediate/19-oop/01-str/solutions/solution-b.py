
class Iris:
    values: list
    species: str

    def __init__(self, values, species):
        self.values = values
        self.species = species

    def __str__(self):
        species = self.species
        total = sum(self.values)
        return f'{species=}, {total=:.1f}'
