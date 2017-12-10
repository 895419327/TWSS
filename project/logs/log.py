from time import localtime, strftime
from TWSS.settings import BASE_DIR

from django.http.request import QueryDict

def log(*args):
    date = strftime('%Y-%m-%d', localtime())
    filename = BASE_DIR + '/project/logs/' + date + '.txt'
    file = open(filename, 'a+', encoding='utf-8')

    time = strftime("%H:%M:%S", localtime())

    info = time
    for arg in args:
        # 如果是QueryDict 删掉不必要的内容
        if type(arg) == QueryDict:
            querydict = arg.copy()
            querydict.pop('csrfmiddlewaretoken')
            try:
                querydict.pop('identify_code')
            except KeyError:
                pass
            try:
                querydict.pop('password')
            except KeyError:
                pass
            info += '\n' + str(querydict)
        else:
            info += '   ' + str(arg)

    info += '\n\n'

    file.write(info)
    file.close()
