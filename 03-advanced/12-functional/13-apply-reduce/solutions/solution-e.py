
result = DATA.splitlines()
result = map(str.strip, result)
result = filter(valid_line, result)
result = map(transform, result)
