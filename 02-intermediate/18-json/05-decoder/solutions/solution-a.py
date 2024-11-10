
def decoder(obj):
    if 'destination_landing' in obj:
        obj['destination_landing'] = datetime.fromisoformat(obj['destination_landing'])

    if 'launch_date' in obj:
        obj['launch_date'] = datetime.fromisoformat(obj['launch_date'])

    if 'birthdate' in obj:
        obj['birthdate'] = date.fromisoformat(obj['birthdate'])

    return obj


result = json.loads(DATA, object_hook=decoder)
