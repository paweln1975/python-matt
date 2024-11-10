
with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    header, *lines = reader
    nrows, nvalues, *labels = header

    encoder = {}
    i = 0
    for label in labels:
        encoder[i] = label
        i += 1

    result = []
    for *values, species in lines:
        species = encoder[int(species)]
        row = tuple(values) + (species,)
        result.append(row)

