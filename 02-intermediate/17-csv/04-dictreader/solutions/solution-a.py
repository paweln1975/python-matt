
result = []

with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    result = list(reader)
