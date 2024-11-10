
with open(FILE, mode='rb') as file:
    config = tomllib.load(file)

metadata = config['metadata']
result = metadata['release_date']
