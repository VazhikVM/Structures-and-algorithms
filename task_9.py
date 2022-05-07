"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""
import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 100
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)],
         [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)],
         [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]]
print(*array, sep='\n')
print('*' * 30)
my_array = []
for i in array:
    a = array[array.index(i)][0]
    for _ in i:
        if _ < a:
            a = _
    my_array.append(a)
print(my_array)
a = my_array[0]
for _ in my_array:
    if _ > a:
        a = _
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {a}')
