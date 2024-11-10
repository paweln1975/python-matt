
keys = set()
for row in DATA:
    keys.update(row.keys())
fieldnames = sorted(keys)

with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(DATA)

