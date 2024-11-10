
def loads(data):
    header, *lines = data.splitlines()
    nrows, nvalues, *labels = header.split(',')
    encoder = dict(enumerate(labels))
    rows = []
    for line in lines:
        *values, species = line.split(',')
        species = encoder[int(species)]
        row = tuple(values) + (species,)
        rows.append(row)
    return rows

result = loads(DATA)
