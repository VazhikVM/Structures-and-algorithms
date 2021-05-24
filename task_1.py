import random
import timeit
import cProfile


# task_5 из 3 урока

# SIZE = 1000
# MIN_ITEM = -10000
# MAX_ITEM = 10000
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)
# array_2 = []
# for i in array:
#     if i < 0:
#         array_2.append(i)
# a = array_2[0]
# for i in array_2:
#     if i > a:
#         a = i
# print(f'Максимальный отрицательный - "{a}" и его индекс {array.index(a)}')


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
print(timeit.timeit('max_neg(100, -100, 100)', number=1000, globals=globals()))  # 0.1018296
print(timeit.timeit('max_neg(200, -100, 100)', number=1000, globals=globals()))  # 0.1983886
print(timeit.timeit('max_neg(300, -100, 100)', number=1000, globals=globals()))  # 0.3131577
cProfile.run('max_neg(10000, -10000, 10000)')


# 61326 function calls in 0.022 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.022    0.022 <string>:1(<module>)
#   10000    0.005    0.000    0.007    0.000 random.py:238(_randbelow_with_getrandbits)
#   10000    0.006    0.000    0.013    0.000 random.py:291(randrange)
#   10000    0.003    0.000    0.017    0.000 random.py:335(randint)
#       1    0.002    0.002    0.021    0.021 task_1.py:21(max_neg)
#       1    0.003    0.003    0.019    0.019 task_1.py:22(<listcomp>)
#       1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
#    5096    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   16224    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#       1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


def max_neg_2(size, min_item, max_item):
    my_array = [random.randint(min_item, max_item) for _ in range(size)]
    array_max_neg = []
    for x in my_array:
        if x < 0:
            array_max_neg.append(x)
    y = max(array_max_neg)

    return f'{my_array}\nМаксимальный отрицательный - "{y}" и его индекс {my_array.index(y)}'


print(max_neg_2(100, -100, 100))

print(timeit.timeit('max_neg_2(100, -100, 100)', number=1000, globals=globals()))  # 0.09687590000000001
print(timeit.timeit('max_neg_2(200, -100, 100)', number=1000, globals=globals()))  # 0.18682449999999995
print(timeit.timeit('max_neg_2(300, -100, 100)', number=1000, globals=globals()))  # 0.276953
cProfile.run('max_neg_2(10000, -10000, 10000)')


# 61177 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#     10000    0.005    0.000    0.007    0.000 random.py:238(_randbelow_with_getrandbits)
#     10000    0.006    0.000    0.013    0.000 random.py:291(randrange)
#     10000    0.003    0.000    0.017    0.000 random.py:335(randint)
#         1    0.002    0.002    0.021    0.021 task_1.py:41(max_neg_2)
#         1    0.003    0.003    0.019    0.019 task_1.py:42(<listcomp>)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#      4917    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16253    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

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


print(max_neg_3(10, -10, 10))

print(timeit.timeit('max_neg_3(100, -100, 100)', number=1000, globals=globals()))  # 0.12091870000000005
print(timeit.timeit('max_neg_3(200, -100, 100)', number=1000, globals=globals()))  # 0.21332379999999995
print(timeit.timeit('max_neg_3(300, -100, 100)', number=1000, globals=globals()))  # 0.33274310000000007
cProfile.run('max_neg_3(10000, -10000, 10000)')
# 71429 function calls in 0.024 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#    10000    0.005    0.000    0.007    0.000 random.py:238(_randbelow_with_getrandbits)
#    10000    0.006    0.000    0.013    0.000 random.py:291(randrange)
#    10000    0.003    0.000    0.016    0.000 random.py:335(randint)
#        1    0.004    0.004    0.023    0.023 task_1.py:60(max_neg_3)
#        1    0.003    0.003    0.019    0.019 task_1.py:61(<listcomp>)
#        1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#    10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#     4962    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    16459    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# Вариант 2 (max_neg_2) наиболее оптимальный, затраченное время на выполнение функции минимальное
