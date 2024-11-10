
def dump(data, file):
    header = tuple(vars(data[0]).keys())
    rows = [tuple(vars(row).values()) for row in data]
    data = [header] + rows
    values = [','.join(f'"{x}"' for x in row) for row in data]
    result = '\n'.join(values) + '\n'
    with open(file, mode='wt') as file:
        file.write(result)
