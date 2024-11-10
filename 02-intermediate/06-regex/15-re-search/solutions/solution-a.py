
def search(pattern):
    if r := re.search(pattern, DATA):
        return r.span()

result_a = search('Neil Armstrong')
result_b = search('Buzz Aldrin')
result_c = search('Michael Collins')
result_d = search('Mark Watney')
