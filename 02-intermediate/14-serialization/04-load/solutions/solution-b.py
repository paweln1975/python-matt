
def loads(data):
    header, *lines = data.splitlines()
    header = tuple(header.split(','))
    rows = []
    for line in lines:
        *values, species = line.split(',')
        values = [float(x) for x in values]
        row = tuple(values) + (species,)
        rows.append(row)
    return [header] + rows

result = loads(DATA)
