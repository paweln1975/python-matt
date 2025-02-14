def as_user(record):
    firstname = record.get('firstname')
    lastname = record.get('lastname')
    values = map(dict.values, record.get('addresses'))
    addresses = starmap(Address, values)
    return User(firstname, lastname, addresses=tuple(addresses))


result = map(as_user, DATA)