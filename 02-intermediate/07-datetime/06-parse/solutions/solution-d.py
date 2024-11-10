
def parse(dt):
    for fmt in FORMATS:
        try:
            return datetime.strptime(dt, fmt)
        except ValueError:
            continue

result = map(parse, DATA)


#%% Alternative Solution
result = map(datetime.strptime, DATA, FORMATS)
