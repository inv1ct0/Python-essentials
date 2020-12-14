import os
import shutil
import sys

# EASY
# Задача-1:
if __name__ == '__main__':
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'dir_{i}')
        try:
            os.mkdir(new_path)
        except FileExistsError:
            print('Directory already is exist')

    for j in range(1, 10):
        path_to_remove = os.path.join(os.getcwd(), f'dir_{j}')
        try:
            os.rmdir(path_to_remove)
        except FileNotFoundError:
            print('Directory is not exist')
# Задача-3:
    new_path = "".join(sys.argv)
    shutil.copyfile(new_path, 'copy_les5.py')


# Задача-2:
def list_dir():
    print(os.listdir())


# for dirpath, dirnames, filenames in os.walk('.'):
#     for dirname in dirnames:
#         print('Folder: ', os.path.join(dirpath, dirname))
#     for filename in filenames:
#         print('File: ', os.path.join(dirpath, filename))


