
with open(FILE, mode='rb') as file:
    config = tomllib.load(file)
    result = config['version']
