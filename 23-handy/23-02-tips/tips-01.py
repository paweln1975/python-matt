import sys
from collections import Counter

# iterate with enumerate instead of range(len())
data = [5, 4, 5, 6, -2, -3, 1, 2, 3]
for idx, val in enumerate(data):
    if val < 0:
        data[idx] = 0

print(data)

# use python comprehension instead of for loop
squared = [x**2 for x in range(10)]
print(squared)

# use sorted with key instead of sort
data = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Doe', 'age': 30}]

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

# remove duplicates from list using set
data = [1, 2, 2, 3, 4, 4, 5]
data = list(set(data))
print(data)

# to save memory use generator expressions instead of list comprehensions
my_list = [x for x in range(100000)]  # list comprehension
print(sum(my_list))
print("Size of list:", sys.getsizeof(my_list), "bytes")

my_gen = (x for x in range(100000))  # generator expression
print(sum(my_gen))
print("Size of generator:", sys.getsizeof(my_gen), "bytes")

# use default for get() to avoid KeyError and setdefault() to initialize dict keys
data = {'a': 1, 'b': 2}
#value = data['c'] # KeyError

value = data.get('c', 0)  # returns 0 if 'c' not found
print(value)

value = data.get('c') # returns None if 'c' not found
print(value)

data.setdefault('c', 3)  # sets 'c' to 3 if not present
value = data['c']
print(value)

# count elements, hashable objects with collections.Counter
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)
print(counter.most_common(2))  # two most common elements
print(counter['banana'])  # count of 'banana'
print(counter['grape'])  # count of 'grape' (not present, returns 0)

# use f-strings for formatting
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# concatenate strings with join() instead of +
words = ['Hello', 'world', 'this', 'is', 'Python']
sentence = ' '.join(words)
print(sentence)

# merge dictionaries with {**d1, **d2} or d1 | d2 (Python 3.9+)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged = {**d1, **d2}  # d2 values overwrite d1
print(merged)
merged2 = d1 | d2  # Python 3.9+
print(merged2)

# simplify if statements with f in instead of checking each element
data = ['apple', 'banana', 'orange']
if 'banana' in data:
    print("Banana is in the list")

if all(fruit in data for fruit in ['apple', 'banana']):
    print("Both apple and banana are in the list")
if any(fruit in data for fruit in ['grape', 'banana']):
    print("At least one of grape or banana is in the list")
