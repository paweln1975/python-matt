
with open(FILE, mode='rt') as file:
    data = json.load(file)

keys = set()
for row in data:
    keys.update(row.keys())
header = tuple(sorted(keys))

result = []
result.append(header)

for row in data:
    line = tuple(row.get(key) for key in header)
    result.append(line)
