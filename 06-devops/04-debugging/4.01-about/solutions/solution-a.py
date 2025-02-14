def doctest(docstring):
    if not docstring:
        return None

    docstring.replace('\\', '').split('\n')

    i = 0

    for line in docstring:
        line = line.strip()

        if line.startswith('>>> '):
            expected = docstring[i+1].strip()
            code = line.split('>>> ')[1]
            result = eval(code)

            if isinstance(result, str):
                result = f"'{result}'"

            if result == expected:
                print('ok')
            else:
                print(f'\nExpected: {expected}\nGot: {result}')

        i += 1


jose = Astronaut(name='José Jiménez')


for method in dir(jose):
    docstring = eval(f'jose.{method}.__doc__')
    doctest(docstring)