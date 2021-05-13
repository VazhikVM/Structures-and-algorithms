"""
https://drive.google.com/file/d/1qn2Yhy2lSxRgGST_Oqvro2uPVHJSapW5/view?usp=sharing
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки
"""
x_1 = float(input("Введите x_1: "))
y_1 = float(input("Введите y_1: "))
x_2 = float(input("Введите x_2: "))
y_2 = float(input("Введите y_2: "))

k = (y_2 - y_1) / (x_2 - x_1)
b = y_2 - k * x_2

print(f'Уравнение прямой выглядит y = {k}x + {b}')
