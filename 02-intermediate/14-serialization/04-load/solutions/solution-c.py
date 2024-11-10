
def loads(data):
    header, *lines = DATA.splitlines()
    header = tuple(header.split(','))
    rows = []
    for line in lines:
        *values, species = line.split(',')
        species = ENCODER[species]
        row = tuple(values) + (species,)
        rows.append(row)
    return [header] + rows


result = loads(DATA)
