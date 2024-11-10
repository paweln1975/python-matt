
def loads(data):
    header, *lines = data.splitlines()
    header = tuple(header.split(','))
    rows = []
    for line in lines:
        *values, species = line.split(',')
        values = [float(x) for x in values]
        record = tuple(values) + (species,)
        row = {}
        for i in range(len(header)):
            h = header[i]
            v = record[i]
            row[h] = v
        rows.append(row)
    return rows

result = loads(DATA)
