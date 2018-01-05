# -*- coding: utf-8 -*-

import os
import time

from django.http import HttpResponse
from django.shortcuts import render

from TWSS.settings import BASE_DIR, DATABASES, DATABASE_BACKUPS_DIR
from project.views import database_management
from project.utilities.identify import check_identity
from project.utilities.log import log


def database(request):
    request.encoding = 'utf-8'

    user = check_identity(request)
    if not user:
        return render(request, "main/utilities/unsafe.html")

    requestfor = request.POST['requestfor']
    log('INFO', 'DataUpload', user.name, user.id, requestfor, request.POST)
    if requestfor == 'database_backup':
        return database_backup(request)
    if requestfor == 'backup_download':
        return buckup_download(request)
    if requestfor == 'buckup_delete':
        return buckup_delete(request, user)


def database_backup(request):
    if request.POST['filename']:
        filename = request.POST['filename']
    else:
        filename = time.strftime('%Y%m%d-%H%M%S', time.localtime())

    full_filename = DATABASE_BACKUPS_DIR + filename + '.sql'

    database_password = DATABASES['default']['PASSWORD']
    os.system('mysqldump -uroot -p' + database_password + ' twss > ' + full_filename)

    os.system('chmod 444 ' + full_filename)

    file = open(full_filename, encoding='utf-8')
    # response = StreamingHttpResponse(file.read())
    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}.sql"'.format(filename)
    return response


def buckup_download(request):
    filename = request.POST['buckup_id']
    file = open(DATABASE_BACKUPS_DIR + filename, encoding='utf-8')

    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response


def buckup_delete(request, user):
    filename = request.POST['request_data']
    full_filename = DATABASE_BACKUPS_DIR + filename

    os.remove(full_filename)

    return database_management(request, user)
