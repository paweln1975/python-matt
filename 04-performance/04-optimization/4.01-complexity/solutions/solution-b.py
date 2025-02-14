result = set()

for row in DATA:
    result.update(row.keys())


"""
# 1.86 µs ± 290 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = set()
for row in DATA:
    for key in row.keys():
        result.add(key)


# 1.37 µs ± 208 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = set()
for row in DATA:
    result.update(row.keys())


# 1.91 µs ± 334 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    for key in row.keys():
        if key not in result:
            result.append(key)


# 2.15 µs ± 277 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    for key in row.keys():
        if key not in result:
            result.append(key)
result = set(result)


# 2.19 µs ± 306 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    for key in row.keys():
        result.append(key)
result = set(result)


# 1.52 µs ± 192 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    result.extend(row.keys())
result = set(result)
"""