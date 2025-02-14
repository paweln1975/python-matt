result = DATA.splitlines()
result = filter(is_valid, result)
result = map(transform, result)