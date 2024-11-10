
data = [vars(obj) for obj in DATA]
fieldnames = sorted(data[0].keys())

with open(FILE, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    writer.writerows(data)
