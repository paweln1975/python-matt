
result = DATA.splitlines()
result = filter(valid_line, result)
result = map(transform, result)
