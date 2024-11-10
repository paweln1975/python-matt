
def parse(line):
    d, t, lvl, msg = line.split(', ', maxsplit=3)
    d = date.fromisoformat(d)
    t = time.fromisoformat(t)
    dt = datetime.combine(d,t)
    return {'datetime':dt, 'level':lvl, 'message': msg}


result = map(parse, DATA.splitlines())
