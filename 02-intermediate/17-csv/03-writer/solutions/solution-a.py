
with open(FILE, mode='wt', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(DATA)
