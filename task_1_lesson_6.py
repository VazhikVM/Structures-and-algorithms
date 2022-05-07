import random
import sys

# task_5 из 3 урока  Windows 10 64-разрядная операционная система, процессор x64, python 64 bit


def max_neg(size, min_item, max_item):
    my_array = [random.randint(min_item, max_item) for _ in range(size)]
    array_max_neg = []
    for x in my_array:
        if x < 0:
            array_max_neg.append(x)
    y = array_max_neg[0]
    for x in array_max_neg:
        if x > y:
            y = x
    return f'{my_array}\nМаксимальный отрицательный - "{y}" и его индекс {my_array.index(y)}'


print(max_neg(100, -100, 100))
print(f'Затрачено памяти: {sys.getsizeof(max_neg(100, -100, 100))}')
# Затрачено памяти: 1058 ----------------------------------------------------------------------------------------------


def max_neg_2(size, min_item, max_item):
    my_array = [random.randint(min_item, max_item) for _ in range(size)]
    array_max_neg = []
    for x in my_array:
        if x < 0:
            array_max_neg.append(x)
    y = max(array_max_neg)

    return f'{my_array}\nМаксимальный отрицательный - "{y}" и его индекс {my_array.index(y)}'


print(max_neg_2(100, -100, 100))
print(f'Затрачено памяти: {sys.getsizeof(max_neg_2(100, -100, 100))}')
# Затрачено памяти: 1060 ----------------------------------------------------------------------------------------------


def max_neg_3(size, min_item, max_item):
    my_array = [random.randint(min_item, max_item) for _ in range(size)]
    array_max_neg = []
    m = 0
    while m < len(my_array):
        if my_array[m] < 0:
            array_max_neg.append(my_array[m])
        m += 1
    y = max(array_max_neg)
    return f'{my_array}\nМаксимальный отрицательный - "{y}" и его индекс {my_array.index(y)}'


print(max_neg_3(100, -100, 100))
print(f'Затрачено памяти: {sys.getsizeof(max_neg_3(10, -10, 10))}')
# Затрачено памяти: Затрачено памяти: 246 -----------------------------------------------------------------
