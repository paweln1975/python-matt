
result = []

with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.reader(file)
    for *values, species in reader:
        species = LABEL_ENCODER[int(species)]
        row = tuple(values) + (species,)
        result.append(row)

