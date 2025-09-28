DATA = [
    ('firstname', 'lastname', 'age'),
    ('Mark', 'Watney', 41),
    ('Melissa', 'Lewis', 40),
    ('Rick', 'Martinez', 39),
    ('Alex', 'Vogel', 40),
    ('Chris', 'Beck', 36),
    ('Beth', 'Johanssen', 29),
]

header, *rows = DATA
result: list[dict[str, str | int]] = [
    dict(zip(header, row)) for row in rows]

print(result)