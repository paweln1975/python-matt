
header, *rows = DATA

data = []
for row in rows:
    tmp = {}
    for i in range(len(header)):
        h = header[i]
        r = row[i]
        tmp[h] = r
    data.append(tmp)

with open(FILE, mode='wt') as file:
    json.dump(data, file)
