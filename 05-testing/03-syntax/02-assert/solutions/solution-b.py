
def add_numbers(a, b):
    assert type(a) in (int, float), 'Parameter `a` must be int or float'
    assert type(b) in (int, float), 'Parameter `b` must be int or float'
    return a + b
