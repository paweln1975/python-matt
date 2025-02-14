def convert(user: dict):
    addresses = [','.join(map(str, x.values()))
                 for x in user.pop('addresses')]
    return user | {'addresses': ';'.join(addresses)}

result = [convert(x) for x in DATA]