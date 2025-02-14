def parse(row):
    *values, species = row.values()
    clsname = species.capitalize()
    cls = globals()[clsname]
    return cls(*values)

result = map(parse, json.loads(DATA))


# %% Alternatively
from functools import reduce
from operator import or_


def subclasses(cls):
    subclasses = cls.__subclasses__()
    asdict = lambda cls: {cls.__name__: cls}
    classes = map(asdict, subclasses)
    return reduce(or_, classes)

def iris(row):
    *values, species = row.values()
    clsname = species.capitalize()
    cls = subclasses(Iris).get(clsname)
    return cls(*values)

result = map(iris, json.loads(DATA))