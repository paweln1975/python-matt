
def parse(line):
    *values, species = line.split(',')
    values = map(float, values)
    species = label_encoder[int(species)]
    return tuple(values) + (species,)


result = map(parse, lines)
