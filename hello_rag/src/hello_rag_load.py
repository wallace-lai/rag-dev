import os
import mimetypes
import configparser

def load_text(path):
    path = path.rstrip()
    path = path.replace(' \n', '')

    filename = os.path.abspath(path)
    if not os.path.isfile(filename):
        print(f"File {filename} not found")
        return None

    filetype = mimetypes.guess_type(filename)[0]
    if filetype != 'text/plain':
        return None

    with open(filename, 'rb') as f:
        text = f.read().decode('utf-8')

    return text

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return dict(config.items('main'))