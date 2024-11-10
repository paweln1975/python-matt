
result = []

for line in DATA.splitlines():
    d, t, lvl, msg = line.strip().split(', ', maxsplit=3)
    d = date.fromisoformat(d)
    t = time.fromisoformat(t)
    dt = datetime.combine(d, t)
    result.append({'datetime': dt, 'level': lvl, 'message': msg})
