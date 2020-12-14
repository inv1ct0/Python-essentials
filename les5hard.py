import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("copy <dir_name> - создание копии указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросит подтверждение операции)")
    print("ls - отображение полного пути текущей директории")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'. format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'. format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        shutil.copyfile(dir_path, os.path.join(os.getcwd(), f'copy_{dir_name}'))
        print('Файл скопирован')
    except FileNotFoundError:
        print('Файла с данным именем не существует')


def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        path_to_remove = os.path.join(os.getcwd(), dir_name)
        if os.path.isdir(path_to_remove):
            os.rmdir(path_to_remove)
            print('Папка удалена')
        else:
            os.remove(path_to_remove)
            print('Файл удален')
    except FileNotFoundError:
        print('Файла/папки с таким именем не существует')


def full_path():
    print(os.getcwd())


def change_disk():
    if not dir_name:
        print("Необходимо указать путь для перехода вторым параметром")
        return
    try:
        os.chdir(dir_name)
        print("Переход в указанную папку совершен")
        full_path()
    except FileNotFoundError:
        print("Указанный путь недоступен или не существует")


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "copy": copy_file,
    "rm": remove_file,
    "ls": full_path,
    "cd": change_disk
    }
try:
    dir_name = sys. argv[ 2]
except IndexError:
    dir_name = None
try:
    key = sys. argv[ 1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
