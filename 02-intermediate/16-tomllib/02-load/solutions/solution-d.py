
with open(FILE, mode='rb') as file:
    config = tomllib.load(file)

authors = config['metadata']['authors']
result = [author['email'] for author in authors]
