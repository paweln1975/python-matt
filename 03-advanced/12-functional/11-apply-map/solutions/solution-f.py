
def parse(record: dict) -> Setosa | Virginica | Versicolor:
    clsname = record.pop('species').capitalize()
    cls = globals()[clsname]
    return cls(**record)


result = map(parse, json.loads(DATA))
