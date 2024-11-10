
def dumps(data):
    header = tuple(data[0].keys())
    rows = [tuple(row.values()) for row in data]
    data = [header] + rows
    values = [','.join(f'"{x}"' for x in row) for row in data]
    result = '\n'.join(values) + '\n'
    return result

result = dumps(DATA)
