
def get_stats(character_name):
    with open(FILE, mode='rb') as file:
        characters = tomllib.load(file)
    return characters[character_name]
