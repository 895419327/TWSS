from time import localtime, strftime
from TWSS.settings import BASE_DIR


def log(*args):
    date = strftime('%Y-%m-%d', localtime())
    filename = BASE_DIR + '/project/logs/' + date + '.txt'
    file = open(filename, 'a+', encoding='utf-8')

    time = strftime("%H:%M:%S", localtime())

    info = time
    for arg in args:
        info += '   ' + str(arg)
    info += '\n'

    file.write(info)
    file.close()
