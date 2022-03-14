import os


def read_list(filename):
    if not os.path.exists(filename):
        print(f'{filename} not exists')
    with open(filename, 'r') as f:
        content = f.read()
        return content.split()
