
def valid(line):
    if len(line) == 0:
        return False
    if line.startswith('#'):
        return False
    return True


result = filter(valid, DATA.splitlines())
