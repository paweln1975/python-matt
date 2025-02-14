def flat(i, group):
    gid = group.get('gid')
    name = group.get('name')
    return {f'group{i}_gid': gid, f'group{i}_name': name}

def flatten(groups):
    dicts = starmap(flat, enumerate(groups, start=1))
    return reduce(or_, dicts, {})

def convert(user):
    firstname = user.get('firstname')
    lastname = user.get('lastname')
    groups = flatten(user.get('groups'))
    return {'firstname': firstname, 'lastname': lastname} | groups


result = map(convert, DATA)

# %% Alternatively
def flatten(group):
    asdict = lambda i,group: {f'group{i}_gid': group['gid'], f'group{i}_name': group['name']}
    dicts = starmap(asdict, enumerate(group, start=1))
    return reduce(or_, dicts, {})

def convert(user):
    fname = user.get('firstname')
    lname = user.get('lastname')
    groups = flatten(user.get('groups'))
    result = dict(firstname=fname, lastname=lname)
    return result | groups


result = map(convert, DATA)