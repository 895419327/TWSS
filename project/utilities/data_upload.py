# -*- coding: utf-8 -*-

import os
import time
import datetime

from TWSS.settings import BASE_DIR

from django.contrib.auth.hashers import make_password

from project.views import *
from project.models import *


def upload(request):
    request.encoding = 'utf-8'

    # 校验身份
    from project.utilities.indentity import check_identity
    check_return = check_identity(request)
    if check_return:
        user = check_return
    else:
        return False

    # 获取需求
    requestfor = request.POST['requestfor']
    # try:
    return eval(requestfor)(request, user)
    # except Exception:
    #     log('WARNING', 'Login Fail', request.POST, repr(Exception))
    #     print('data_upload.py upload() exception')
    #     return False


# TODO: 考虑在User表增加location 防假单
# TODO: 更改前要检查数据合法性
# 比如系主任审核通过时 教师正好更改了数据 微小的时间差导致审核通过的不是系主任看到的数据

def user_info(request, user):
    department = request.POST['department']
    department = Department.objects.get(name=department)

    gender = 0
    if request.POST['gender'] == u'男':
        gender = 1
    elif request.POST['gender'] == u'女':
        gender = 2
    user.gender = gender
    user.department = department
    user.title = request.POST['title']
    user.birth_date = request.POST['birth_date']
    user.graduate = request.POST['graduate']
    user.major = request.POST['major']
    user.phone_number = request.POST['phone_number']
    user.email = request.POST['email']
    user.save()
    return user_info_user_info(request, user)


def change_password(request, user):
    original_password = request.POST['original_password']
    new_password = request.POST['new_password']
    if check_password(original_password, user.password):
        user.password = make_password(new_password)
        user.save()
        return render(request, 'main/utilities/upload_success.html')
    else:
        return False


# Theory Course

def theory_course_add(request, user):
    id = ''
    if request.POST['id']:
        id = request.POST['id']
    else:
        id = str(int(time.time())) + user.id

    semester = 0
    if request.POST['semester'] == u'第一学期':
        semester = 1
    elif request.POST['semester'] == u'第二学期':
        semester = 2
    else:
        return False

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

    new = TheoryCourse(id=id,
                       name=request.POST['course_name'],
                       course_id=request.POST['course_id'],
                       year=request.POST['year'][:4],
                       semester=semester,
                       teacher=user,
                       department=user.department,
                       classes=classes,
                       student_sum=student_sum,
                       plan_period=request.POST['plan_period'],
                       final_period=request.POST['final_period'],
                       attribute=attribute)
    new.workload = theory_course_workload_count(new)
    new.save()

    return workload_input_theory_course(request, user)


def theory_course_delete(request, user):
    id = request.POST['request_data']
    course = TheoryCourse.objects.get(id=id)
    if course.audit_status == 2:
        return False
    else:
        course.delete()
    return workload_input_theory_course(request, user)


# Experiment Course

def experiment_course_add(request, user):
    id = ''
    if request.POST['id']:
        id = request.POST['id']
    else:
        id = str(int(time.time())) + user.id

    semester = 0
    if request.POST['semester'] == u'第一学期':
        semester = 1
    elif request.POST['semester'] == u'第二学期':
        semester = 2
    else:
        return False

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

    new = ExperimentCourse(id=id,
                           name=request.POST['course_name'],
                           course_id=request.POST['course_id'],
                           year=request.POST['year'][:4],
                           semester=semester,
                           teacher=user,
                           department=user.department,
                           classes=classes,
                           student_sum=student_sum,
                           plan_period=request.POST['plan_period'],
                           final_period=request.POST['final_period'],
                           attribute=attribute)
    new.workload = experiment_course_workload_count(new)
    new.save()
    return workload_input_experiment_course(request, user)


def experiment_course_delete(request, user):
    id = request.POST['request_data']
    course = ExperimentCourse.objects.get(id=id)
    if course.audit_status == 2:
        return False
    else:
        course.delete()
    return workload_input_experiment_course(request, user)


# Pratice Course

def pratice_course_add(request, user):
    id = ''
    if request.POST['id']:
        id = request.POST['id']
    else:
        id = str(int(time.time())) + user.id

    semester = 0
    if request.POST['semester'] == u'第一学期':
        semester = 1
    elif request.POST['semester'] == u'第二学期':
        semester = 2
    else:
        return False

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

    new = PraticeCourse(id=id,
                        name=request.POST['course_name'],
                        course_id=request.POST['course_id'],
                        year=request.POST['year'][:4],
                        semester=semester,
                        teacher=user,
                        department=user.department,
                        classes=classes,
                        student_sum=student_sum,
                        plan_period=request.POST['plan_period'],
                        final_period=request.POST['final_period'],
                        attribute=attribute)
    new.save()
    return workload_input_pratice_course(request, user)


def pratice_course_delete(request, user):
    id = request.POST['request_data']
    course = PraticeCourse.objects.get(id=id)
    if course.audit_status == 2:
        return False
    else:
        course.delete()
    return workload_input_pratice_course(request, user)


def teaching_achievement_add(request, user):
    id = ''
    if request.POST['project_id']:
        id = request.POST['project_id']
    else:
        id = str(int(time.time())) + user.id

    rank = ''
    if 'rank' in request.POST:
        rank = request.POST['rank']
    project_type = request.POST['type']
    if project_type != u'教学成果':
        rank = ''

    new = TeachingAchievement(id=id,
                              name=request.POST['project_name'],
                              type=project_type,
                              level=request.POST['level'],
                              rank=rank,
                              year=request.POST['year'][:4],
                              teacher=user,
                              department=user.department)
    new.workload = teaching_achievement_workload_count(new)
    new.save()
    return workload_input_teaching_achievement(request, user)


def teaching_achievement_delete(request, user):
    project_id = request.POST['request_data']
    project = TeachingAchievement.objects.get(id=project_id)
    if project.audit_status == 2:
        return False
    else:
        project.delete()
    return workload_input_teaching_achievement(request, user)


def teaching_project_add(request, user):
    id = ''
    if request.POST['project_id']:
        id = request.POST['project_id']
    else:
        id = str(int(time.time())) + user.id

    new = TeachingProject(id=id,
                          name=request.POST['project_name'],
                          type=request.POST['type'],
                          level=request.POST['level'],
                          year=request.POST['year'][:4],
                          teacher=user,
                          department=user.department)
    new.workload = teaching_project_workload_count(new)
    new.save()
    return workload_input_teaching_project(request, user)


def teaching_project_delete(request, user):
    project_id = request.POST['request_data']
    project = TeachingProject.objects.get(id=project_id)
    if project.audit_status == 2:
        return False
    else:
        project.delete()
    return workload_input_teaching_project(request, user)


def competition_guide_add(request, user):
    id = ''
    if request.POST['project_id']:
        id = request.POST['project_id']
    else:
        id = str(int(time.time())) + user.id

    new = CompetitionGuide(id=id,
                           name=request.POST['project_name'],
                           type=request.POST['type'],
                           level=request.POST['level'],
                           students=request.POST['project_students'],
                           year=request.POST['year'][:4],
                           teacher=user,
                           department=user.department)
    new.workload = competition_guide_workload_count(new)
    new.save()
    return workload_input_competition_guide(request, user)


def competition_guide_delete(request, user):
    project_id = request.POST['request_data']
    project = CompetitionGuide.objects.get(id=project_id)
    if project.audit_status == 2:
        return False
    else:
        project.delete()
    return workload_input_competition_guide(request, user)


def paper_guide_add(request, user):
    id = ''
    if request.POST['project_id']:
        id = request.POST['project_id']
    else:
        id = str(int(time.time())) + user.id

    new = PaperGuide(id=id,
                     student=request.POST['student'],
                     year=request.POST['year'][:4],
                     teacher=user,
                     department=user.department)
    new.workload = papar_guide_workload_count(new)
    new.save()
    return workload_input_paper_guide(request, user)


def paper_guide_delete(request, user):
    project_id = request.POST['request_data']
    project = PaperGuide.objects.get(id=project_id)
    if project.audit_status == 2:
        return False
    else:
        project.delete()
    return workload_input_paper_guide(request, user)


# Notice Setting

def notice_setting(request, user):
    post_time = datetime.date.today()

    notice = Notice.objects.get(id=1)
    notice.content = request.POST['notice_content']
    notice.post_time = post_time
    notice.post_by = user
    notice.save()
    return notice_settings(request, user)


# Teacher Management

# FIXME: MEDIUM 如果系主任修改了自己的id
#               会导致浏览器上还记载着原来的id  于是发送表单时还用原来的 id
#               数据库查无此人  于是无法正确加载页面
#               触发条件过于严苛 暂不修复

# FIXME: URGENT 如果系主任修改了其他教师的id
#               目前逻辑无法迁移密码 会默认将手机号设为密码
#               导致无法正常登陆
#               紧急解决方案：应在修改界面予以提醒
# TODO:         后期应重写逻辑 或 考虑给User表增加一个无法被任何用户修改的id

def teacher_add(request, user):
    id = request.POST['teacher_id']
    # 默认使用教职工号作为密码
    password = id
    from hashlib import md5
    generater = md5(password.encode("utf8"))
    password = generater.hexdigest()
    password = make_password(password)

    # 检测是新增还是修改
    if 'original_teacher_id' in request.POST:
        if request.POST['original_teacher_id'] != request.POST['teacher_id']:
            old = User.objects.get(id=request.POST['original_teacher_id'])
            password = old.password

    department = Department.objects.get(name=request.POST['department'])

    # 教务员修改系主任信息后 系主任status会被重置为'教师' 需手动加上
    status = u'教师'
    departments = Department.objects.all()
    for d in departments:
        if d.head_of_department == request.POST['teacher_id']:
            status = u'教师,系主任'
            break

    gender = request.POST['gender']
    if gender == u'男':
        gender = 1
    elif gender == u'女':
        gender = 2
    else:
        gender = 0

    new = User(id=id,
               name=request.POST['name'],
               gender=gender,
               birth_date=request.POST['birth_date'],
               title=request.POST['title'],
               department=department,
               status=status,
               password=password,
               graduate=request.POST['graduate'],
               major=request.POST['major'],
               phone_number=request.POST['phone_number'],
               email=request.POST['email'], )
    new.save()

    # 将原id账号下的项目转移至新账号
    if 'original_teacher_id' in request.POST:
        if request.POST['original_teacher_id'] != request.POST['teacher_id']:
            old = User.objects.get(id=request.POST['original_teacher_id'])

            theory_course_list = TheoryCourse.objects.filter(teacher=old)
            experiment_course_list = ExperimentCourse.objects.filter(teacher=old)
            pratice_course_list = PraticeCourse.objects.filter(teacher=old)
            teaching_achievement_list = TeachingAchievement.objects.filter(teacher=old)
            teaching_project_list = TeachingProject.objects.filter(teacher=old)
            competition_guide_list = CompetitionGuide.objects.filter(teacher=old)
            paper_guide_list = PaperGuide.objects.filter(teacher=old)

            for theory_course in theory_course_list:
                theory_course.teacher = new
                theory_course.save()
            for experiment_course in experiment_course_list:
                experiment_course.teacher = new
                experiment_course.save()
            for pratice_course in pratice_course_list:
                pratice_course.teacher = new
                pratice_course.save()
            for teaching_achievement in teaching_achievement_list:
                teaching_achievement.teacher = new
                teaching_achievement.save()
            for teaching_project in teaching_project_list:
                teaching_project.teacher = new
                teaching_project.save()
            for competition_guide in competition_guide_list:
                competition_guide.teacher = new
                competition_guide.save()
            for paper_guide in paper_guide_list:
                paper_guide.teacher = new
                paper_guide.save()

            class_list = Class.objects.filter(teacher=old)
            for clas in class_list:
                clas.teacher = new
                clas.save()

            old.delete()

    return teacher_management(request, user)


def teacher_delete(request, user):
    teacher_id = request.POST['request_data']
    teacher = User.objects.get(id=teacher_id)
    teacher.delete()
    return teacher_management(request, user)


# Class Management

# TODO: 大一生物科学类分班

def class_add(request, user):
    teacher = None
    teacher_info = request.POST['teacher']
    if teacher_info != '':
        teacher_id = teacher_info.split(' ')[1]
        teacher = User.objects.get(id=teacher_id)
    department = Department.objects.get(name=request.POST['department'])
    new = Class(id=request.POST['class_id'],
                name=request.POST['name'],
                department=department,
                grade=request.POST['grade'][:-1],
                sum=request.POST['student_sum'],
                teacher=teacher)
    new.save()

    if 'original_class_id' in request.POST:
        if request.POST['original_class_id'] != request.POST['class_id']:
            old = Class.objects.get(id=request.POST['original_class_id'])
            old.delete()
    return class_management(request, user)


def class_delete(request, user):
    class_id = request.POST['request_data']
    clas = Class.objects.get(id=class_id)
    clas.delete()
    return class_management(request, user)


##### 教务员 #####


def global_setting(request, user):
    year_upload = request.POST['year'][:4]
    semester_upload = request.POST['semester']
    if semester_upload == u'第一学期':
        semester_upload = 1
    elif semester_upload == u'第二学期':
        semester_upload = 2
    else:
        return False

    year = GlobalValue.objects.get(key='current_year')
    semester = GlobalValue.objects.get(key='current_semester')

    year.value = year_upload
    semester.value = semester_upload

    year.save()
    semester.save()
    return global_settings(request, user)


def change_head_of_department_upload(request, user):
    department = Department.objects.get(id=request.POST['department_id'])

    # 修改两账户身份
    original_head_id = department.head_of_department
    original_head = User.objects.get(id=original_head_id)
    original_head.status = original_head.status.replace(',系主任', '')
    original_head.save()

    new_head_id = request.POST['teacher'].split(' ')[1]
    new_head = User.objects.get(id=new_head_id)
    if new_head.status.find('系主任') == -1:
        new_head.status += ',系主任'
    new_head.save()

    department.head_of_department = new_head_id
    department.save()
    return department_management(request, user)
