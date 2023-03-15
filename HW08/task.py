# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных


def show_data():
    '''Эта функция показывает содержимое справочника'''
    with open('data.txt', 'r', encoding='utf-8') as data:
        return data.read().split('\n')


def new_data():
    '''Добавляет новую информацию в справочник'''
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write('\n' + input('Введите данные: '))


def find_data():
    '''Эта функция ищет информацию в справочнике'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input()
        for i in book:
            if temp in i:
                print(i)


def replace_data():
    '''Эта функция изменяет информацию в справочнике'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        a = False
        while a == False:
            temp = input('Что меняем: ')
            for i in range(len(book)):
                if temp in book[i]:
                    print(f'Что вы хотите сделать с записью ({book[i]})?\
                          \n 1. Изменить\
                          \n 2. Удалить\
                          \n 3. Пропустить')
                    user_ans = 3
                    user_ans = int(input())
                    if user_ans == 1:
                        book[i] = book[i].replace(book[i], input('На что меняем: '))
                    if user_ans == 2:
                        book[i] = book[i].replace((book[i]), '')
                    a = True
            if a == False:
                print('Запись не найдена')
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(filter(lambda x: x != '', book)))


while True:
    mode = input('Выберите режим работы справочника:\
                \n 1. Показать содержимое справочника\
                \n 2. Добавить новую информацию в справочник\
                \n 3. Поиск информации в справочнике\
                \n 4. Изменить информацию в справочнике\
                \n ')

    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        replace_data()
    elif mode == '0':
        break
    else:
        print('No mode')


# def replace_data():
#     '''Эта функция изменяет информацию в справочнике'''
#     with open('data.txt', 'r', encoding='utf-8') as file:
#         book = file.read()
#         temp = str()
#         while (temp not in book or temp == ''):
#             temp = input('Что меняем: ')
#             if temp in book:
#                 new_data = book.replace(temp, input('На что меняем: '))
#             else:
#                 print('Запись не найдена')
#     print(new_data)
#     with open('data.txt', 'w', encoding='utf-8') as file:
#         file.write(new_data)
