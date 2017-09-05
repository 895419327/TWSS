# -*- coding: utf-8 -*-

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

from django.shortcuts import render
from project.views import *
from project.models import *


def upload(request):
    request.encoding = 'utf-8'
    # 校验身份
    from project.utilities.check_indentity import check_identity
    check_return = check_identity(request)
    if check_return:
        user = check_return
    else:
        return False

    # 获取需求
    requestfor = request.POST['requestfor']

    if requestfor == 'user_info':
        return upload_user_info(request, user)
    if requestfor == 'theory_course_add':
        return upload_theory_course(request, user)
    if requestfor == 'theory_course_delete':
        return upload_theory_course_delete(request, user)

    return False


def upload_user_info(request, user):
    # 获取json字符串
    data_jsonstr = request.POST[u'request_data']
    # 解析为对象
    data_json = json.loads(data_jsonstr, encoding='utf-8')
    # 获取数据
    user.phone_number = data_json[u'手机号']
    # 保存
    user.save()
    # 返回成功状态
    return render(request, 'main/utilities/upload_success.html')


def upload_theory_course(request, user):
    semester = 0
    if request.POST['semester'] == u'第一学期':
        semester = 1
    elif request.POST['semester'] == u'第二学期':
        semester = 2
    else:
        return render(request, 'main/utilities/upload_fail.html')

    class_list = Class.objects.all()
    classes = ''
    student_sum = 0
    for clas in class_list:
        if clas.id in request.POST:
            classes += clas.id+','
            student_sum += clas.sum

    attribute = 0
    if request.POST['course_attribute'] == u'必修':
        attribute = 1
    elif request.POST['course_attribute'] == u'选修':
        attribute = 2
    elif request.POST['course_attribute'] == u'限选':
        attribute = 3
    new = TheoryCourse(name=request.POST['course_name'],
                       id=request.POST['course_id'],
                       year=request.POST['year'][:4],
                       semester=semester,
                       teacher=user,
                       classes=classes,
                       student_sum=student_sum,
                       period=request.POST['period'],
                       credit=request.POST['credit'],
                       attribute=attribute,
                       )
    new.save()
    return theory_course_page(request, user)


def upload_theory_course_delete(request, user):
    course_id = request.POST['request_data']
    TheoryCourse.objects.filter(id=course_id).delete()
    return theory_course_page(request, user)
