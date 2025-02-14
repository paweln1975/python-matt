def flat(i, groupobj):
    group = vars(groupobj)
    gid = group.get('gid')
    name = group.get('name')
    return {f'group{i}_gid': gid, f'group{i}_name': name}

def flatten(groups):
    dicts = starmap(flat, enumerate(groups, start=1))
    return reduce(or_, dicts, {})

def convert(userobj):
    user = vars(userobj)
    firstname = user.get('firstname')
    lastname = user.get('lastname')
    groups = flatten(user.get('groups'))
    return {'firstname': firstname, 'lastname': lastname} | groups


result = map(convert, DATA)