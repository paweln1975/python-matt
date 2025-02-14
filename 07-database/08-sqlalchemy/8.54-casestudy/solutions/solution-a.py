def parse(data):
    header, *rows = data.splitlines()
    header = header.split(',')
    return [dict(zip(header,values))
            for row in rows
            if (values := row.split(','))]

users = parse(USERS)
addresses = parse(ADDRESSES)
products = parse(PRODUCTS)
orders = parse(ORDERS)