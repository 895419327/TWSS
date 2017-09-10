# -*- coding: utf-8 -*-

import os
import json
import time

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
    return globals().get(requestfor)(request, user)


# TODO: 更改前要检查数据合法性
# 比如系主任审核通过时 教师正好更改了数据 微小的时间差导致审核通过的不是系主任看到的数据

def user_info(request, user):
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

def theory_course_add(request, user):
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
                       attribute=attribute)
    new.save()
    return workload_input_theory_course(request, user)


def theory_course_delete(request, user):
    course_id = request.POST['request_data']
    course = TheoryCourse.objects.get(id=course_id)
    if course.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        course.delete()
    return workload_input_theory_course(request, user)


# Experiment Course

def experiment_course_add(request, user):
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
                           attribute=attribute)
    new.save()
    return workload_input_experiment_course(request, user)


def experiment_course_delete(request, user):
    course_id = request.POST['request_data']
    course = ExperimentCourse.objects.get(id=course_id)
    if course.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        course.delete()
    return workload_input_experiment_course(request, user)


# Pratice Course

def pratice_course_add(request, user):
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
                        attribute=attribute)
    new.save()
    return workload_input_pratice_course(request, user)


def pratice_course_delete_add(request, user):
    course_id = request.POST['request_data']
    course = PraticeCourse.objects.get(id=course_id, teacher=user)
    if course.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        course.delete()
    return workload_input_pratice_course(request, user)


def teaching_achievement_add(request, user):
    id = ''
    if 'project_id' in request.POST:
        id = request.POST['project_id']
    else:
        id = int(time.time())
    new = TeachingAchievement(id=id,
                              name=request.POST['project_name'],
                              type=request.POST['type'],
                              level=request.POST['level'],
                              teacher=user,
                              department=user.department, )
    new.save()
    return workload_input_teaching_achievement(request, user)


def teaching_achievement_delete(request, user):
    project_id = request.POST['request_data']
    project = TeachingAchievement.objects.get(id=project_id)
    if project.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        project.delete()
    return workload_input_teaching_achievement(request, user)


def teaching_project_add(request, user):
    id = ''
    if 'project_id' in request.POST:
        id = request.POST['project_id']
    else:
        id = int(time.time())
    new = TeachingProject(id=id,
                          name=request.POST['project_name'],
                          type=request.POST['type'],
                          level=request.POST['level'],
                          teacher=user,
                          department=user.department, )
    new.save()
    return workload_input_teaching_project(request, user)


def teaching_project_delete(request, user):
    project_id = request.POST['request_data']
    project = TeachingProject.objects.get(id=project_id)
    if project.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        project.delete()
    return workload_input_teaching_project(request, user)


def competition_guide_add(request, user):
    id = ''
    if 'project_id' in request.POST:
        id = request.POST['project_id']
    else:
        id = int(time.time())
    new = CompetitionGuide(id=id,
                           name=request.POST['project_name'],
                           type=request.POST['type'],
                           level=request.POST['level'],
                           students=request.POST['project_students'],
                           teacher=user,
                           department=user.department, )
    new.save()
    return workload_input_competition_guide(request, user)


def competition_guide_delete(request, user):
    project_id = request.POST['request_data']
    project = CompetitionGuide.objects.get(id=project_id)
    if project.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        project.delete()
    return workload_input_competition_guide(request, user)


def paper_guide_add(request, user):
    id = ''
    if 'project_id' in request.POST:
        id = request.POST['project_id']
    else:
        id = int(time.time())
    new = PaperGuide(id=id,
                     name=request.POST['project_name'],
                     level=request.POST['level'],
                     author=request.POST['author'],
                     teacher=user,
                     department=user.department, )
    new.save()
    return workload_input_paper_guide(request, user)


def paper_guide_delete(request, user):
    project_id = request.POST['request_data']
    project = PaperGuide.objects.get(id=project_id)
    if project.audit_status == 2:
        return render(request, 'main/utilities/upload_fail.html')
    else:
        project.delete()
    return workload_input_paper_guide(request, user)


# Teacher Management

def teacher_management_add(request, user):
    # 先假设使用手机号作为密码
    password = request.POST['phone_number']
    # 如果是在更改界面修改密码则使用该密码
    if 'password' in request.POST:
        if request.POST['password'] and request.POST['password'] != u'不修改则放空':
            password = request.POST['password']

    from hashlib import md5
    generater = md5(password.encode("utf8"))
    password = generater.hexdigest()

    new = User(id=request.POST['teacher_id'],
               name=request.POST['name'],
               title=request.POST['title'],
               department=user.department,
               status=u'教师',
               password=password,
               phone_number=request.POST['phone_number'],
               email=request.POST['email'], )
    new.save()

    if 'original_teacher_id' in request.POST:
        if request.POST['original_teacher_id'] != request.POST['teacher_id']:
            old = User.objects.get(id=request.POST['original_teacher_id'])
            old.delete()

    return teacher_management(request, user)


def teacher_management_delete(request, user):
    teacher_id = request.POST['request_data']
    teacher = User.objects.get(id=teacher_id)
    teacher.delete()
    return teacher_management(request, user)


# Class Management

def class_management_add(request, user):
    # TODO:根据实际id长度修改
    teacher = User.objects.get(id=request.POST['teacher'][-11:])
    new = Class(id=request.POST['class_id'],
                name=request.POST['name'],
                department=user.department,
                grade=request.POST['grade'][:-1],
                sum=request.POST['student_sum'],
                teacher=teacher)
    new.save()

    if 'original_class_id' in request.POST:
        if request.POST['original_class_id'] != request.POST['class_id']:
            old = Class.objects.get(id=request.POST['original_class_id'])
            old.delete()
    return class_management(request, user)


def class_management_delete(request, user):
    class_id = request.POST['request_data']
    clas = Class.objects.get(id=class_id)
    clas.delete()
    return class_management(request, user)
