from my_package import mylen
import timeit
data = [x for x in range(1000)]




print(
    timeit.timeit(stmt="""
mylen(data)
""",
                  setup="""
from my_package import mylen
data = [x for x in range(1000)]
""", number=100000))
