"""
>>> print(get_top_letters(DATA, num))
Top 5 letters:
e: 41
t: 37
s: 32
o: 26
a: 21

>>> print(get_top_words(DATA, num))
Top 5 words:
the: 8
it: 4
and: 3
classes: 2
got: 2
"""
import re
from typing import OrderedDict

DATA = """
Most of the lists and dicts and stuff were fine for me…but when it got to Classes section (Python Code Challenges: Classes), WOW it got hard. The hints didn’t help - looked at the answers and re-read the prompt…wondering who in the world wrote it because it answered the obvious while skipped the parts that was NOT taught in the Class section before. Also I found actual spelling typos (like so was spelled “se” etc.)
"""
num = 5


def get_top(regexp: str, text: str, num, what = 'letters'):
    result: dict[str, int] = {}
    text = text.strip().lower()
    item_list = re.findall(regexp, text)
    for item in item_list:
        value = result.get(item, 0)
        result[item] = value + 1
    items = [(k, v) for k, v in result.items()]
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    top_items = sorted_items[:num]

    output = f'Top {num} {what}:\n'
    for k, v in top_items:
        output += f'{k}: {v}\n'

    return output.rstrip()

def get_top_letters(text: str, num):
    pattern = r'\w'
    return get_top(pattern, text, num)

def get_top_words(text: str, num):
    pattern = r'\w+'
    return get_top(pattern, text, num, what='words')

def get_top_letters_and_words(text, num):

    letters = get_top_letters(text, num)
    words = get_top_words(text, num)
    return letters, words
