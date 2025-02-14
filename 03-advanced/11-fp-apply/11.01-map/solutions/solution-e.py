def parse(line):
    *values, species = line.strip().split(',')
    numbers = map(float, values)
    return tuple(numbers) + (species,)


result = map(parse, DATA.splitlines())