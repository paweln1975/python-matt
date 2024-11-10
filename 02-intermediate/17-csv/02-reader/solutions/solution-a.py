
result = []

with open(FILE, mode='rt', encoding='utf-8') as file:
    reader = csv.reader(file, lineterminator='\n')
    result = [tuple(row) for row in reader]
