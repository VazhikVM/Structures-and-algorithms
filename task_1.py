"""
https://drive.google.com/file/d/1qn2Yhy2lSxRgGST_Oqvro2uPVHJSapW5/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
"""
num = int(input('Введите 3-х значное число: '))
a = int(num * 0.01)
b = int(((int(num * 0.1) * 0.1) - a) * 10)
c = int(((num * 0.1)-int(num * 0.1))*10)
print(f'Сумма цифр {num} = {a + b + c}\nПроизведение цифр {num} = {a * b * c}')
