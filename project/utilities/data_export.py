# -*- coding: utf-8 -*-

import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

from django.http import HttpResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper

import xlwt
import xlrd
from xlutils.copy import copy  # TODO:


def download(request):
    request.encoding = 'utf-8'

    from project.utilities.indentity import check_identity
    check_return = check_identity(request)
    if check_return == False:
        return False  # 返回错误信息
    else:
        user = check_return

    requestfor = request.POST['requestfor']
    # if requestfor == 'user_info':
    #     return user_info_to_excel(request, user)
    if requestfor == 'database_backup':
        return database_backup(request)


# 将user_info写入excel并返回
# def user_info_to_excel(request, user):
#     # 打开模板
#     workbook_template = xlrd.open_workbook(os.path.join(MEDIA_PATH, 'excel', 'templates', 'user_info.xls'),
#                                            formatting_info=True)
#     # 拷贝模板workbook
#     workbook = copy(workbook_template)
#     # 打开worksheet
#     worksheet = workbook.get_sheet(0)
# 
#     # 设置字体格式
#     style = xlwt.XFStyle()
#     font = xlwt.Font()
#     font.name = u'宋体'
#     style.font = font
# 
#     # 写入数据
#     worksheet.write(2, 0, user.id, style)
#     worksheet.write(2, 1, user.name, style)
#     worksheet.write(2, 3, user.status, style)
#     worksheet.write(2, 4, user.phone_number, style)
# 
#     # 保存
#     filename = os.path.join(MEDIA_PATH, 'excel', 'user_info', user.id + '.xls')
#     workbook.save(filename)
#     file = open(filename)
#     # 封装
#     wrapper = FileWrapper(file)
# 
#     # 配置reponse 返回文件
#     response = HttpResponse(wrapper)
#     response['Content-Type'] = 'text/octet-stream'
#     response['Content-Disposition'] = 'attachment; filename="%s.xls"' % user.id
#     return response


def database_backup(request):
    if request.POST['filename']:
        filename = request.POST['filename']
    else:
        filename = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())

    full_filename = BASE_DIR + '/project/database_backups/' + filename + '.sql'

    os.system('cd ' + BASE_DIR)
    os.system('python3 manage.py dumpdata > ' + full_filename)

    os.system('chmod 444 ' + full_filename)

    file = open(full_filename)
    response = StreamingHttpResponse(file.read())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}.sql"'.format(filename)
    return response
