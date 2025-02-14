def flat(address):
    values = map(str, address.values())
    return str.join(',', values)

def flatten(row):
    fname = row.get('firstname')
    lname = row.get('lastname')
    addresses = map(flat, row.get('addresses'))
    addr = str.join(';', addresses)
    return {'firstname': fname, 'lastname': lname, 'addresses': addr}

result = map(flatten, DATA)