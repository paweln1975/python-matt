
def loads(data):
    rows = []
    for line in data.splitlines():
        i = 0
        row = {}
        for value in line.split(','):
            header = HEADER[i]
            row[header] = value
            i += 1
        rows.append(row)
    return rows

result = loads(DATA)

