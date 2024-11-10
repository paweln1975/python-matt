
def convert(x):
    try:
        return float(x)
    except ValueError:
        return x


with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    result = []
    for row in reader:
        row = {k:convert(v) for k,v in row.items()}
        result.append(row)
