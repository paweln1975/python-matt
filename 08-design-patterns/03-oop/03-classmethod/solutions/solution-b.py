
class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    @classmethod
    def from_csv(cls, data):
        *values, species = data.split(',')
        values = map(float, values)
        data = tuple(values) + (species,)
        return cls(*data)


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass
