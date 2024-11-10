
class Iris:
    def __init__(self, sl, sw, pl, pw, species):
        self.sepal_length = sl
        self.sepal_width = sw
        self.petal_length = pl
        self.petal_width = pw
        self.species = species

    @property
    def numeric_values(self):
        return [x for x in vars(self).values() if type(x) is float]

    def sum(self):
        return sum(self.numeric_values)

    def len(self):
        return len(self.numeric_values)

    def mean(self):
        return self.sum() / self.len()
