
def parse(dt):
    for fmt in FORMATS:
        try:
            return datetime.strptime(dt, fmt)
        except ValueError:
            continue

result = map(parse, DATA)


#%% Alternative Solution
# but, it works only if the order of DATA fits the other of FORMATS
# result = map(datetime.strptime, DATA, FORMATS)
