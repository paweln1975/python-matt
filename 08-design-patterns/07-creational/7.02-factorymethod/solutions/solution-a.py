def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    match species:
        case 'setosa':     return Setosa(*values)
        case 'virginica':  return Virginica(*values)
        case 'versicolor': return Versicolor(*values)

# %% Alternatively
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    if species == 'setosa':
        return Setosa(*values)
    elif species == 'virginica':
        return Virginica(*values)
    elif species == 'versicolor':
        return Versicolor(*values)

# %% Alternatively
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    classname = species.capitalize()
    cls = globals()[classname]
    return cls(*values)