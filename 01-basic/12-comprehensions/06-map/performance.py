import timeit

print(
    timeit.timeit(stmt="""

result = ''.join(PL.get(letter, letter) for letter in DATA)
""", setup="""
PL = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ż': 'z',
    'ź': 'z',
}
DATA = 'zażółć gęślą jaźń'
""", number=100000))
