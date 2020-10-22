password = input('Введите пароль: ')
count = len(password)


try:
    result = int(password)
    result1 = 10/count
    print('Ваш пароль состоит только из цифр')    
except ZeroDivisionError:
    print('Вы ввели пустой пароль')    
except ValueError:
    print('Требования к паролю соблюдены')
except:
    print('Неизвестная ошибка')

