"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
b = 0
my_max = ''
for i, item in enumerate(array):
    a = array.count(item)
    if a > b:
        b = a
        my_max = item
print(f'Элемент {my_max} встречается наибольшее число раз')
