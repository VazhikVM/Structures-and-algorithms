"""
https://drive.google.com/file/d/1qn2Yhy2lSxRgGST_Oqvro2uPVHJSapW5/view?usp=sharing
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')
print(f'Номер первой букве в алфавите "{ord(first_letter)-96}"\n'
      f'Номер второй буквы в алфавите "{ord(second_letter)-96}"\n'
      f'Между буквами находится {ord(second_letter)-ord(first_letter)-1} букв')
