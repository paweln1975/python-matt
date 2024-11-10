
def parse(line):
    *values, species = line.strip().split(',')
    values = map(float, values)
    return tuple(values) + (species,)


result = map(parse, DATA.splitlines())
