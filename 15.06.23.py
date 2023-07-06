a = input('Введите слова для проверки (с маленькой буквы): ')
if a == a[::-1]:
    print('True')
else:
    print('False')