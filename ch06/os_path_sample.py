import os


def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            search(filepath)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == '.py':
                print(filepath)
