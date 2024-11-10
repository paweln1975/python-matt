
def loads(data):
    return [tuple(line.split(',')) for line in data.splitlines()]

result = loads(DATA)
