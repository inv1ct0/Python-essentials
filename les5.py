import os
from les5easy import list_dir


# NORMAL
# Задача-1:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
def make_dir(dirname):
    path_to_make = os.path.join(os.getcwd(), dirname)
    try:
        os.mkdir(path_to_make)
        print('Успешно создано')
    except FileExistsError:
        print('Невозможно создать. Папка с таким именем уже существует')


def change_dir(dirname):
    try:
        os.chdir(dirname)
        print('Перешел')
    except FileNotFoundError:
        print('Невозможно перейти. Данной папки не существует')


def remove_dir(dirname):
    try:
        os.rmdir(dirname)
        print('Удалил')
    except FileNotFoundError:
        print('Невозможно удалить. Папки с данным именем не существует')


def dir_util():
    while True:
        man = {1: 'Перейти в папку',
               2: 'Просмотреть содержимое текущей папки',
               3: 'Удалить папку',
               4: 'Создать папку',
               0: 'Выход'}
        print(man)
        choice = int(input('Выберите нужное действие: '))
        if choice == 1:
            print(man.get(choice))
            dirname = input('Введите имя папки для перехода: ')
            change_dir(dirname)
        if choice == 2:
            print(man.get(choice))
            list_dir()
        if choice == 3:
            print(man.get(choice))
            dirname = input('Введите имя папки для удаления: ')
            remove_dir(dirname)
        if choice == 4:
            print(man.get(choice))
            dirname = input('Введите имя папки для создания: ')
            make_dir(dirname)
        if choice == 0:
            exit()


dir_util()
