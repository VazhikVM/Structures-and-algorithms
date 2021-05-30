import collections
from statistics import mean

org = collections.Counter()
count = 1
a = int(input('Введите количество предприятий: '))
while True:
    b = input(f'Введите наименование преприятия № {count}: ')
    c = input(f'Введите прибыль преприятия № {count} за с 1 по 4 квартал в формате "10 20 30 40": ')
    org[b] = c.split()
    count += 1
    if count > a:
        break
print(org)
for i in org:
    org[i] = mean(list(map(int, org[i])))
print(f'Наибольшую прибыль имеет преприятие {org.most_common(1)[0][0]} {org.most_common(1)[0][1]}')
print(f'Наименьшая прибыль имеет у преприятие {list(org.keys())[-1]} {list(org.values())[-1]}')
