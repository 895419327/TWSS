# -*- coding: utf-8 -*-

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

from django.shortcuts import render


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

    if requestfor == 'page':
        return page(request, user)


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


from project.models import TheoryCourse


def upload_theory_course(request, user):
    # 获取json字符串
    data_jsonstr = request.POST['request_data']
    # 解析为对象
    data_json = json.loads(data_jsonstr, encoding='utf-8')
    # 获取数据

    semester = 0
    if data_json['semester'] == u'第一学期':
        semester = 1
    elif data_json['semester'] == u'第二学期':
        semester = 2
    else:
        return render(request, 'main/utilities/upload_fail.html')

    new = TheoryCourse(name=data_json['course_name'],
                       year=data_json['year'],
                       semester=semester,
                       teacher=user,
                       classes=data_json['class'],
                       student_sum=0,
                       period=data_json['period'],
                       credit=data_json['credit'],
                       attribute=data_json['course_attribute'],
                       )
    new.save()
    return render(request, 'main/utilities/upload_success.html')


def upload_theory_course_delete(request, user):
    course_id = request.POST['request_data']
    TheoryCourse.objects.filter(id=course_id).delete()
    return render(request, 'main/utilities/upload_success.html')


def page(request, user):
    return render(request, 'main/teacher/workload_input/theory_course/theory_course.html')
