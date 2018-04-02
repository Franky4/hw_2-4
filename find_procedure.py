# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os


def find_in_file(file, f_str):
    result = False
    with open(file) as f:
        for line in f:
            if f_str in line.lower():
                return True
    return result


def print_list_files(list_files):
    for item in list_files:
        print(item)


def main():

    list_files = []
    my_dir = "Migrations"
    my_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), my_dir)

    my_format_file = '.sql'
    for d, dirs, files in os.walk(my_dir):
        for f in files:
            if my_format_file in f:
                list_files.append(os.path.join(my_dir, f))
    print('Всего {} sql файлов'.format(len(list_files)))

    while True:
        new_list = list_files[:]
        list_files = []
        my_str = str(input('Введите строку для поиска: ')).lower()
        for f in new_list:
            if find_in_file(f, my_str):
                list_files.append(f)
        if len(list_files) < 5:
            print_list_files(list_files)

        print('Всего: {}'.format(len(list_files)))


if __name__ == '__main__':
    main()
