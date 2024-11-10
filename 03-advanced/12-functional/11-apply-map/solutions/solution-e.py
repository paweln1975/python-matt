
def parse(line: str) -> tuple[float,float,float,float,str]:
    *values, species = line.strip().split(',')
    values = map(float, values)
    return tuple(values) + (species,)


result = map(parse, DATA.splitlines())
