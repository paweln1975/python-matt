result = map(datetime.strptime, DATA, FORMATS)


# %% Alternatively
def convert(string, index=0):
    try:
        fmt = FORMATS[index]
        return datetime.strptime(string, fmt)
    except ValueError:
        return convert(string, index+1)
    except IndexError:
        return None

result = map(convert, DATA)

# %% Alternatively
def convert(string, index=0):
    if index >= len(FORMATS):
        return None
    try:
        return datetime.strptime(string, FORMATS[index])
    except ValueError:
        return convert(string, index+1)

result = map(convert, DATA)