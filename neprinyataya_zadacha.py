import os
import contextlib


class ChangeDir:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.f = os.chdir(self.path)
        # print('enter', os.getcwd())
        return self.f

    def __exit__(self, exc_type, exc_val, traceback):
        # print('exit')
        self.f = '..'
        os.chdir(self.f)


with ChangeDir('dir1'):
    print(os.listdir())

    # print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())
    # os.chdir('..')
    # print("2. Текущая деректория:", os.getcwd())
    # print(os.listdir('dir2'))

# вывод в консоль
# ['log.txt']
# ['file1.py', 'file2.py']