import collections


def hexadecimal_sum(x, y):
    hexadecimal_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = collections.deque()
    mind = 0

    if len(y) > len(x):
        x, y = collections.deque(y), collections.deque(x)

    else:
        x, y = collections.deque(x), collections.deque(y)

    while x:

        if y:
            res = hexadecimal_dict[x.pop()] + hexadecimal_dict[y.pop()] + mind

        else:
            res = hexadecimal_dict[x.pop()] + mind

        mind = 0

        if res < 16:
            result.appendleft(hexadecimal_dict[res])

        else:
            result.appendleft(hexadecimal_dict[res - 16])
            mind = 1

    if mind:
        result.appendleft('1')

    return list(result)


print(hexadecimal_sum('A1', 'C4F'))
