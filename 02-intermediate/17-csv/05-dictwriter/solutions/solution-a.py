
fieldnames = DATA[0].keys()

with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(DATA)


