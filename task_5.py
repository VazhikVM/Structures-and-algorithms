"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array_2 = []
for i in array:
    if i < 0:
        array_2.append(i)
a = array_2[0]
for i in array_2:
    if i > a:
        a = i
print(f'Максимальный отрицательный - "{a}" и его индекс {array.index(a)}')

