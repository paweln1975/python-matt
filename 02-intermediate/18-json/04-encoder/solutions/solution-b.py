
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date | datetime):
            return obj.isoformat()


result = json.dumps(DATA, cls=Encoder)
