
def encoder(obj):
    if isinstance(obj, date | datetime):
        return obj.isoformat()


result = json.dumps(DATA, default=encoder)
