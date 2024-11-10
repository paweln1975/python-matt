
result = []

with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    header, *rows = reader
    result.append(tuple(header))

    for *values, species in rows:
        values = [float(x) for x in values]
        row = tuple(values) + (species,)
        result.append(row)

