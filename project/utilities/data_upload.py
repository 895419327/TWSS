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

    if requestfor == 'experiment_course_add':
        return upload_experiment_course(request, user)
    if requestfor == 'experiment_course_delete':
        return upload_experiment_course_delete(request, user)

    if requestfor == 'pratice_course_add':
        return upload_pratice_course(request, user)
    if requestfor == 'pratice_course_delete':
        return upload_pratice_course_delete(request, user)

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


# Theory Course

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
            classes += clas.id + ','
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
                       department=user.department,
                       classes=classes,
                       student_sum=student_sum,
                       period=request.POST['period'],
                       credit=request.POST['credit'],
                       attribute=attribute,
                       )
    new.save()
    return workload_input_theory_course(request, user)


def upload_theory_course_delete(request, user):
    course_id = request.POST['request_data']
    course = TheoryCourse.objects.get(id=course_id)
    if course.audit_status == 1:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        course.delete()
    return workload_input_theory_course(request, user)


# Experiment Course

def upload_experiment_course(request, user):
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
            classes += clas.id + ','
            student_sum += clas.sum

    attribute = 0
    if request.POST['course_attribute'] == u'专业课实验':
        attribute = 1
    elif request.POST['course_attribute'] == u'计算机上机实验':
        attribute = 2
    elif request.POST['course_attribute'] == u'开放实验':
        attribute = 3
    new = ExperimentCourse(name=request.POST['course_name'],
                           id=request.POST['course_id'],
                           year=request.POST['year'][:4],
                           semester=semester,
                           teacher=user,
                           department=user.department,
                           classes=classes,
                           student_sum=student_sum,
                           period=request.POST['period'],
                           credit=request.POST['credit'],
                           attribute=attribute,
                           )
    new.save()
    return workload_input_experiment_course(request, user)


def upload_experiment_course_delete(request, user):
    course_id = request.POST['request_data']
    course = ExperimentCourse.objects.get(id=course_id)
    if course.audit_status == 1:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        course.delete()
    return workload_input_experiment_course(request, user)


# Pratice Course

def upload_pratice_course(request, user):
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
            classes += clas.id + ','
            student_sum += clas.sum

    attribute = 0
    if request.POST['course_attribute'] == u'市区内认识实习':
        attribute = 1
    elif request.POST['course_attribute'] == u'外地认识实习/市区内生产实习':
        attribute = 2
    elif request.POST['course_attribute'] == u'外地生产实习/毕业实习/毕业设计(论文)':
        attribute = 3
    new = PraticeCourse(name=request.POST['course_name'],
                           id=request.POST['course_id'],
                           year=request.POST['year'][:4],
                           semester=semester,
                           teacher=user,
                           department=user.department,
                           classes=classes,
                           student_sum=student_sum,
                           period=request.POST['period'],
                           credit=request.POST['credit'],
                           attribute=attribute,
                           )
    new.save()
    return workload_input_pratice_course(request, user)


def upload_pratice_course_delete(request, user):
    course_id = request.POST['request_data']
    course = PraticeCourse.objects.get(id=course_id)
    if course.audit_status == 1:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        course.delete()
    return workload_input_pratice_course(request, user)