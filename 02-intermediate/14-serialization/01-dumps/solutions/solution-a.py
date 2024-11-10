
def dumps(data):
    values = [','.join(f'{x}' for x in row) for row in data]
    result = '\n'.join(values) + '\n'
    return result

result = dumps(DATA)
