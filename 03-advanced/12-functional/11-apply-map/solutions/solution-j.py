
def convert(contact: dict):
    addresses = [','.join(map(str, x.values()))
                 for x in contact.pop('addresses')]
    return contact | {'addresses': ';'.join(addresses)}

result = map(convert, DATA)
