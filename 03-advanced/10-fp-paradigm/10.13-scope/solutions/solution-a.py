def sumselected(values, species):
    if species in SELECT:
        return sum(values)
    else:
        return 0