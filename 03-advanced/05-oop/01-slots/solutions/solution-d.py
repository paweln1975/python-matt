
def dump(obj) -> dict:
    return {x:getattr(obj,x) for x in obj.__slots__}
