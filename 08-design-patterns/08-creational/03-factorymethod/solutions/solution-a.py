
def iris(row: tuple[float,float,float,float,str]) -> Iris:
    *values, species = row
    match species:
        case 'setosa':     return Setosa(*values)
        case 'virginica':  return Virginica(*values)
        case 'versicolor': return Versicolor(*values)


