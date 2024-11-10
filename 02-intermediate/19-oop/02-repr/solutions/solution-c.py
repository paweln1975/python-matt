
class Iris:
    values: list
    species: str

    def __init__(self, data):
        self.values = list(data[:-1])
        self.species = str(data[-1])

    def __repr__(self):
        values = self.values
        species = self.species
        return f'Iris({values=}, {species=})'
