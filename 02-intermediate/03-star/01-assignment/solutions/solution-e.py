
header, *rows = DATA

result = []
for *values, species in rows:
    if species.endswith(SUFFIXES):
        result.append(species)
