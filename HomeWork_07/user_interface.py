# Запрашиваем у пользователя действие

def choice():
    print('Телефонный справочник')
    result = int(input('Меню выбора: \n\
            1 - Добавить абонента\n\
            2 - Показать всех абонентов\n\
            3 - Выход\n\
            Выберите пункт: '))
    return result