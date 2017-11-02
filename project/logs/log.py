import time
from TWSS.settings import BASE_DIR


def log(*args):
    data = time.strftime('%Y-%m-%d', time.localtime())
    filename = BASE_DIR + '/project/logs/' + data + '.txt'
    file = open(filename, 'a+')

    info = ''
    for arg in args:
        info += str(arg) + '     '
    info += '\n'

    file.write(info)
    file.close()
