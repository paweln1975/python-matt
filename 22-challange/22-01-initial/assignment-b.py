"""
>>> result = FibonacciIterator(5)
>>> consume_iterator(result)
0
1
1
2
3

>>> result = FibonacciIterator(2)
>>> consume_iterator(result)
0
1

"""

def consume_iterator(iter):
    for n in iter:
        print(str(n))

class FibonacciIterator:

    def __init__(self, n):
        self.data = []
        self.current = -1

        if n == 1:
            self.data.append(0)

        if n >= 2:
            self.data.append(0)
            self.data.append(1)
            for n in range(2, n):
                self.data.append(self.data[-1]+self.data[-2])

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self.data):
            return self.data[self.current]
        else:
            raise StopIteration


