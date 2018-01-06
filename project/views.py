# -*- coding: utf-8 -*-

import os
import sys
import time

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render

from TWSS.settings import DATABASE_BACKUPS_DIR
from project.utilities.identify import *
from project.utilities.search import *
from project.utilities.workload_count import *


def index(request):
    return render(request, 'index/index.html')


# TODO: memcache

# TODO: 数据库自动备份
# TODO: 测试覆盖


# TODO: 防爆破 输入多次密码错误后封ip


# TODO: 移动端可做成微信小程序


# TODO: 实验课 上课/教辅  6：4

# TODO：理论课 老师分上一节课 工作量怎么算

# TODO: 刷新工作量

def login(request):
    request.encoding = 'utf-8'

    # 如果表单为POST提交
    if request.POST:
        # 接收表单数据
        username_post = request.POST['username']
        password_post = request.POST['password']
        status_post = request.POST['status']
        captcha = request.POST['captcha']

        # 检查是否存在此用户
        user = ''
        try:
            user = User.objects.get(id=username_post)
        except Exception:
            log('WARNING', 'Username Not Found', username_post, status_post, request.POST)
            return render(request, 'index/loginfailed.html')

        # 验证密码
        if not check_password(password_post, user.password):
            log('WARNING', 'Password Uncorrect', username_post, user.name, status_post, request.POST)
            return render(request, 'index/loginfailed.html')

        # 账号密码验证通过
        # 生成identify_code并保存
        identify_code = generate_identify_code(user, username_post, password_post, captcha)
        user.identify_code = identify_code
        user.save()

        # 记录
        log('INFO', 'Login', user.name, user.id, status_post, request.POST)

        # 检查身份 返回相应页面
        notice = Notice.objects.get(id=1)
        if status_post == u'教师' and user.is_teacher():
            return render(request, 'main/teacher/teacher.html', locals())
        elif status_post == u'系主任' and user.is_head_of_department():
            return render(request, 'main/head_of_department/head_of_department.html', locals())
        elif status_post == u'教务员' and user.is_dean():
            return render(request, 'main/dean/dean.html', locals())
        elif status_post == u'系统管理员' and user.is_admin():
            return render(request, 'main/admin/admin.html', locals())
        # 身份验证失败
        else:
            return render(request, 'index/status_incorrect.html', locals())

    # 任何意外
    log('ERROR', 'Login Fail', request)
    return render(request, 'index/loginfailed.html')


def getpage(request):
    request.encoding = 'utf-8'
    # 校验身份
    user = check_identity(request)
    if not user:
        return render(request, "main/utilities/unsafe.html")

    # 获取需求
    requestfor = request.POST['requestfor']
    # 记录
    log('INFO', 'GetPage', user.name, user.id, requestfor, request.POST)
    return getattr(sys.modules[__name__], requestfor)(request, user)


#####  教师  #####

def notice_page(request, user):
    notice = Notice.objects.get(id=1)
    return render(request, 'main/teacher/notice/notice.html', locals())


def user_info_user_info(request, user):
    # 玄学bug
    # 没有这行修改后出生日期不显示 其他项没问题
    birth_date = str(user.birth_date)
    return render(request, 'main/teacher/user_info/user_info.html', locals())


def user_info_change_password(request, user):
    return render(request, 'main/teacher/user_info/change_password.html', locals())


# TODO: 选择班级后更新人数
def get_classes(grade=2017):
    class_list = Class.objects.filter(grade=grade)
    return class_list


def get_classes_module(request, user):
    data = request.POST['request_data'].split(',')
    grade = data[0]
    course_type = data[1]
    course_id = data[2]

    class_list = Class.objects.filter(grade=grade)
    classes_checked = ''
    if course_id:
        if course_type == 'TheoryCourse':
            classes_checked = TheoryCourse.objects.get(id=course_id).classes.split(',')
        elif course_type == 'ExperimentCourse':
            classes_checked = ExperimentCourse.objects.get(id=course_id).classes.split(',')
        elif course_type == 'PraticeCourse':
            classes_checked = PraticeCourse.objects.get(id=course_id).classes.split(',')

    return render(request, "main/utilities/classes.html", locals())


# Theory Course

def workload_input_theory_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    # 获取账号课程信息
    course_list = TheoryCourse.objects.filter(teacher_id=user.id)
    course_list, year, semester = search_course(request, course_list)
    return render(request, 'main/teacher/workload_input/theory_course/theory_course.html', locals())


def workload_input_theory_course_add(request, user):
    current_year = int(GlobalValue.objects.get(key='current_year').value)
    years = range(2016, current_year + 1)
    grades = range(current_year, 2013, -1)

    location = ''
    if 'extra_data' in request.POST and request.POST['extra_data'] != '':
        location = request.POST['extra_data'].split(',')
        year = location[0]
        semester = location[1]
    # 获取班级信息

    class_list = get_classes(current_year)
    modified_course = ''

    course_list = TheoryCourse.objects.order_by('course_id')
    course_info_list = []
    for course in course_list:
        info = course.course_id + ' ' + course.name
        if info not in course_info_list:
            course_info_list.append(info)

    if request.POST['request_data']:
        modified_course = TheoryCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
        grade = int(classes_checked[0][0:4])
        class_list = get_classes(grade)
    return render(request, 'main/teacher/workload_input/theory_course/theory_course_add.html', locals())


# Experiment Course

def workload_input_experiment_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    # 获取账号课程信息
    course_list = ExperimentCourse.objects.filter(teacher_id=user.id)
    course_list, year, semester = search_course(request, course_list)
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course.html', locals())


def workload_input_experiment_course_add(request, user):
    current_year = int(GlobalValue.objects.get(key='current_year').value)
    years = range(2016, current_year + 1)
    grades = range(current_year, 2013, -1)

    location = ''
    if 'extra_data' in request.POST and request.POST['extra_data'] != '':
        location = request.POST['extra_data'].split(',')
        year = location[0]
        semester = location[1]
    # 获取班级信息
    class_list = get_classes(current_year)
    modified_course = ''

    course_list = ExperimentCourse.objects.order_by('course_id')
    course_info_list = []
    for course in course_list:
        info = course.course_id + ' ' + course.name
        if info not in course_info_list:
            course_info_list.append(info)

    if request.POST['request_data']:
        modified_course = ExperimentCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
        grade = int(classes_checked[0][0:4])
        class_list = get_classes(grade)
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course_add.html', locals())


# Pratice Course

def workload_input_pratice_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    # 获取账号课程信息
    course_list = PraticeCourse.objects.filter(teacher_id=user.id)
    course_list, year, semester = search_course(request, course_list)
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course.html', locals())


def workload_input_pratice_course_add(request, user):
    current_year = int(GlobalValue.objects.get(key='current_year').value)
    years = range(2016, current_year + 1)
    grades = range(current_year, 2013, -1)

    location = ''
    if 'extra_data' in request.POST and request.POST['extra_data'] != '':
        location = request.POST['extra_data'].split(',')
        year = location[0]
        semester = location[1]
    # 获取班级信息
    class_list = get_classes(current_year)
    modified_course = ''
    if request.POST['request_data']:
        modified_course = PraticeCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
        grade = int(classes_checked[0][0:4])
        class_list = get_classes(grade)
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course_add.html', locals())


# Teaching Achievement

def workload_input_teaching_achievement(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    project_list = TeachingAchievement.objects.filter(teacher_id=user.id)
    project_list, year = search_project(request, project_list)
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement.html', locals())


def workload_input_teaching_achievement_add(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    modified_project = ''
    project_type = ''
    location = ''
    if request.POST['extra_data']:
        location = request.POST['extra_data'].split(',')
        year = location[0]
    if request.POST['request_data']:
        modified_project = TeachingAchievement.objects.get(id=request.POST['request_data'])

    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement_add.html', locals())


# Teaching Project
def workload_input_teaching_project(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    project_list = TeachingProject.objects.filter(teacher_id=user.id)
    project_list, year = search_project(request, project_list)
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project.html', locals())


def workload_input_teaching_project_add(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    modified_project = ''
    location = ''
    if request.POST['extra_data']:
        location = request.POST['extra_data'].split(',')
        year = location[0]
    if request.POST['request_data']:
        modified_project = TeachingProject.objects.get(id=request.POST['request_data'])
    type_list = [u'专业、团队及实验中心类', u'课程类', u'工程实践教育中心', u'教学名师', u'大学生创新创业训练']
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project_add.html', locals())


# Competition Guide

def workload_input_competition_guide(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    project_list = CompetitionGuide.objects.filter(teacher_id=user.id)
    project_list, year = search_project(request, project_list)
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide.html', locals())


def workload_input_competition_guide_add(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    modified_project = ''
    location = ''
    if request.POST['extra_data']:
        location = request.POST['extra_data'].split(',')
        year = location[0]
    if request.POST['request_data']:
        modified_project = CompetitionGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide_add.html', locals())


# Paper Guide

def workload_input_paper_guide(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    project_list = PaperGuide.objects.filter(teacher_id=user.id)
    project_list, year = search_project(request, project_list)
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide.html', locals())


def workload_input_paper_guide_add(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    location = ''
    if request.POST['extra_data']:
        location = request.POST['extra_data'].split(',')
        year = location[0]

    modified_project = ''
    if request.POST['request_data']:
        modified_project = PaperGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide_add.html', locals())


# Workload Count

def teacher_workload_count(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    year = GlobalValue.objects.get(key='current_year').value
    if request.POST['request_data']:
        year = request.POST['request_data'][:4]

    is_audit = True
    if request.POST['extra_data']:
        audit_status = request.POST['extra_data']
        if audit_status == u'所有':
            is_audit = False

    theory_course_W, \
    experiment_course_W, \
    pratice_course_W, \
    teaching_achievement_W, \
    teaching_project_W, \
    competition_guide_W, \
    paper_guide_W \
        = workload_count(user, year=year, is_audit=is_audit)

    course_total_W = round(theory_course_W + pratice_course_W + experiment_course_W, 2)
    project_total_W = round(teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W, 2)
    return render(request, 'main/teacher/workload_count/workload_count.html', locals())


# ##### 系主任 #####

def workload_audit_reject_page(request, user):
    data = request.POST['request_data'].split(',')
    project_type = data[0]
    project_id = data[1]
    return render(request, 'main/dean/workload_audit/workload_audit_reject.html', locals())


def workload_audit_reject(request, user):
    project_type = request.POST['project_type']
    if project_type == 'TheoryCourse':
        course = TheoryCourse.objects.get(id=request.POST['project_id'])
        course.audit_status = 1
        course.reject_reason = request.POST['reject_reason']
        course.save()
        return workload_audit_theory_course(request, user)
    elif project_type == 'ExperimentCourse':
        course = ExperimentCourse.objects.get(id=request.POST['project_id'])
        course.audit_status = 1
        course.reject_reason = request.POST['reject_reason']
        course.save()
        return workload_audit_experiment_course(request, user)
    elif project_type == 'PraticeCourse':
        course = PraticeCourse.objects.get(id=request.POST['project_id'])
        course.audit_status = 1
        course.reject_reason = request.POST['reject_reason']
        course.save()
        return workload_audit_pratice_course(request, user)

    elif project_type == 'TeachingAchievement':
        project = TeachingAchievement.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        return workload_audit_teaching_achievement(request, user)
    elif project_type == 'TeachingProject':
        project = TeachingProject.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        return workload_audit_teaching_project(request, user)
    elif project_type == 'CompetitionGuide':
        project = CompetitionGuide.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        return workload_audit_competition_guide(request, user)
    elif project_type == 'PaperGuide':
        project = PaperGuide.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        return workload_audit_paper_guide(request, user)


# 理论课
def workload_audit_theory_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    course_list = TheoryCourse.objects.filter(audit_status__gte=1)
    course_list, year, semester, audit_status = search_course_audit(request, course_list)
    return render(request, 'main/dean/workload_audit/theory_course/theory_course_audit.html', locals())


def workload_audit_theory_course_pass(request, user):
    course = TheoryCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_theory_course(request, user)


# 实验课
def workload_audit_experiment_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    course_list = ExperimentCourse.objects.filter(audit_status__gte=1)
    course_list, year, semester, audit_status = search_course_audit(request, course_list)
    return render(request, 'main/dean/workload_audit/experiment_course/experiment_course_audit.html', locals())


def workload_audit_experiment_course_pass(request, user):
    course = ExperimentCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_experiment_course(request, user)


# 实习实训课
def workload_audit_pratice_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    course_list = PraticeCourse.objects.filter(audit_status__gte=1)
    course_list, year, semester, audit_status = search_course_audit(request, course_list)
    return render(request, 'main/dean/workload_audit/pratice_course/pratice_course_audit.html', locals())


def workload_audit_pratice_course_pass(request, user):
    course = PraticeCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_pratice_course(request, user)


# 教学成果
def workload_audit_teaching_achievement(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    project_list = TeachingAchievement.objects.filter(audit_status__gte=1)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/dean/workload_audit/teaching_achievement/teaching_achievement_audit.html', locals())


def workload_audit_teaching_achievement_pass(request, user):
    course = TeachingAchievement.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_teaching_achievement(request, user)


# 教学项目
def workload_audit_teaching_project(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    project_list = TeachingProject.objects.filter(audit_status__gte=1)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/dean/workload_audit/teaching_project/teaching_project_audit.html', locals())


def workload_audit_teaching_project_pass(request, user):
    course = TeachingProject.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_teaching_project(request, user)


# 竞赛指导
def workload_audit_competition_guide(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    project_list = CompetitionGuide.objects.filter(audit_status__gte=1)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/dean/workload_audit/competition_guide/competition_guide_audit.html', locals())


def workload_audit_competition_guide_pass(request, user):
    course = CompetitionGuide.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_competition_guide(request, user)


# 论文指导
def workload_audit_paper_guide(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    project_list = PaperGuide.objects.filter(audit_status__gte=1)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/dean/workload_audit/paper_guide/paper_guide_audit.html', locals())


def workload_audit_paper_guide_pass(request, user):
    course = PaperGuide.objects.get(id=request.POST['request_data'])
    course.audit_status = 3
    course.save()
    return workload_audit_paper_guide(request, user)


###### 教务员 #####


def global_settings(request, user):
    current_year = int(GlobalValue.objects.get(key='current_year').value)
    current_semester = int(GlobalValue.objects.get(key='current_semester').value)
    return render(request, 'main/dean/global_settings/global_settings.html', locals())


# 公告设置
def notice_settings(request, user):
    notice = Notice.objects.get(id=1)
    return render(request, 'main/dean/notice_settings/notice_settings.html', locals())


# 专业管理

def department_management(request, user):
    department_list = Department.objects.all()
    # 因为不能互相引用
    # 因此系表的系主任值记录的是id字符串而不是外键
    # 在此要转为外键
    for department in department_list:
        department.head_of_department = User.objects.get(id=department.head_of_department)
    return render(request, 'main/dean/department_management/department_management.html', locals())


def department_management_modify(request, user):
    department_id = request.POST['request_data']
    department = Department.objects.get(id=department_id)
    original_head = User.objects.get(id=department.head_of_department)
    teacher_list = User.objects.all()
    return render(request, 'main/dean/department_management/department_management_modify.html', locals())


# 教师管理
# 系主任有权调用
def teacher_management(request, user):
    department_list = []
    teacher_list = []
    # 若为系主任
    if user.is_head_of_department():
        department_list = Department.objects.filter(head_of_department=user.id)
        teacher_list = User.objects.filter(department=user.department)
    # 若为教务员
    elif user.is_dean():
        export_all = True
        department_list = Department.objects.all()
        teacher_list = User.objects.all()
    return render(request, 'main/head_of_department/teacher_management/teacher_management.html', locals())


def teacher_management_add(request, user):
    modified_teacher = ''
    if request.POST['request_data']:
        modified_teacher = User.objects.get(id=request.POST['request_data'])
    return render(request, 'main/head_of_department/teacher_management/teacher_management_add.html', locals())


def teacher_management_detail(request, user):
    teacher_id = request.POST['request_data']
    teacher = User.objects.get(id=teacher_id)

    theory_course_list = TheoryCourse.objects.filter(teacher=teacher)
    experiment_course_list = ExperimentCourse.objects.filter(teacher=teacher)
    pratice_course_list = PraticeCourse.objects.filter(teacher=teacher)
    teaching_achievement_list = TeachingAchievement.objects.filter(teacher=teacher)
    teaching_project_list = TeachingProject.objects.filter(teacher=teacher)
    competition_guide_list = CompetitionGuide.objects.filter(teacher=teacher)
    papar_guide_list = PaperGuide.objects.filter(teacher=teacher)

    return render(request, 'main/head_of_department/teacher_management/teacher_management_detail.html', locals())


# 班级管理

def class_management(request, user):
    department_list = Department.objects.all()
    year = int(GlobalValue.objects.get(key='current_year').value)

    grade_list = ['当前四届']
    for g in range(2014, year + 1):
        grade_list.append(str(g) + u'级')

    class_list = []
    grade = ''
    if 'request_data' in request.POST:
        grade = request.POST['request_data']
    if grade == '当前四届' or grade == '':
        class_list = Class.objects.filter(grade__gt=int(year) - 4)
        grade = '当前四届'
    else:
        grade = grade[:4]
        class_list = Class.objects.filter(grade=grade)
        grade = str(grade) + u'级'

    return render(request, 'main/dean/class_management/class_management.html',
                  locals())


def class_management_add(request, user):
    department_list = Department.objects.all()
    teacher_list = User.objects.all()
    year = int(GlobalValue.objects.get(key='current_year').value)

    if request.POST['extra_data']:
        location = request.POST['extra_data'].split(' ')
        department_id = location[0]
        department = department_list.get(id=department_id)
        location_grade = location[1]
        if location_grade == u'当前四届':
            location_grade = year
        else:
            location_grade = int(location_grade[:4])

    modified_class = ''
    if request.POST['request_data']:
        modified_class = Class.objects.get(id=request.POST['request_data'])

    grade_list = []
    for g in range(2014, year + 1):
        grade_list.append(g)

    return render(request, 'main/dean/class_management/class_management_add.html',
                  locals())


# TODO: 检查/刷新工作量
# 工作量统计
# 系主任有权调用
def workload_statistics(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)

    year = GlobalValue.objects.get(key='current_year').value
    if request.POST['request_data']:
        year = request.POST['request_data'][:4]

    is_audit = True
    sortby = ''

    if request.POST['extra_data']:
        extra_data = request.POST['extra_data']
        if extra_data:
            extra_data = extra_data.split(',')
            sortby = extra_data[0]
            audit_status = extra_data[1]
            if audit_status == u'所有':
                is_audit = False

    department_list = []
    teacher_list = []

    # 若为系主任
    if user.is_head_of_department():
        department_list = Department.objects.filter(head_of_department=user.id)
        teacher_list = User.objects.filter(department=user.department)
    # 若为教务员
    elif user.is_dean():
        export_all = True
        department_list = Department.objects.all()
        teacher_list = User.objects.all()

    workload_list = []
    for teacher in teacher_list:
        theory_course_W, \
        experiment_course_W, \
        pratice_course_W, \
        teaching_achievement_W, \
        teaching_project_W, \
        competition_guide_W, \
        paper_guide_W \
            = workload_count(teacher, year=year, is_audit=is_audit)

        course_total_W = round(theory_course_W + pratice_course_W + experiment_course_W, 2)
        project_total_W = round(teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W, 2)

        workload = [teacher.department.id, teacher.name, teacher.id, teacher.title,
                    course_total_W, project_total_W]
        workload_list.append(workload)

    if not sortby:
        sortby = 'teacher'

    if sortby == 'teacher':
        workload_list.sort(key=lambda w: w[2])
        sortby = u'按教职工号'
    elif sortby == 'course':
        workload_list.sort(key=lambda w: w[4])
        workload_list.reverse()
        sortby = u'按教学工作量'
    elif sortby == 'project':
        workload_list.sort(key=lambda w: w[5])
        workload_list.reverse()
        sortby = u'按教研工作量'

    sortby_list = [u'按教职工号', u'按教学工作量', u'按教研工作量']

    return render(request, 'main/head_of_department/workload_statistics/workload_statistics.html', locals())


def workload_K_value(request, user):
    return render(request, 'main/dean/workload_K_value/workload_K_value.html', locals())


# # # ADMIN # # #

def database_management(request, user):
    backup_infos = []
    for root, dirs, files in os.walk(DATABASE_BACKUPS_DIR):
        for file in files:
            create_time = os.path.getctime(DATABASE_BACKUPS_DIR + file)
            create_time_r = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(create_time))

            size = os.path.getsize(DATABASE_BACKUPS_DIR + file)
            size = size / 1000

            info = (create_time, file, create_time_r, size)
            backup_infos.append(info)
    backup_infos.sort()
    backup_infos.reverse()
    return render(request, "main/admin/database_management/database_management.html", locals())


def data_import(request, user):
    return render(request, "main/admin/data_import/data_import.html", locals())


def data_import_a(request, user):
    # import xlrd
    # workbook = xlrd.open_workbook('/users/vicchen/downloads/data.xlsx')

    '''
    # 导入教师信息
    worksheet = workbook.sheet_by_name('User')
    nrows = worksheet.nrows

    for r in range(0, nrows):
        try:
            value = worksheet.row_values(r, start_colx=0, end_colx=2)
            name = value[0]
            teacher_id = str(value[1])

            teacher_list = User.objects.filter(id=teacher_id)
            if teacher_list.count() == 0:
                p = teacher_id + 'zhengzhoudaxueshengmingkexuexueyuanjiaoshigongzuoliangtongjixitong'
                generater = md5(p.encode("utf8"))
                password = generater.hexdigest()
                password = make_password(password)

                new = User(id=teacher_id, name=name, password=password, department_id='471')
                new.save()
                print(teacher_id, name)


        except:
            print(value)

    '''
    '''
    # 导入TheoryCourse
    worksheet = workbook.sheet_by_name('TheoryCourse')
    nrows = worksheet.nrows

    curr_time = int(time.time())

    for r in range(0, nrows):
        curr_time += 1
        try:
            value = worksheet.row_values(r, start_colx=0, end_colx=5)
            name = value[0]
            name = name.strip()
            course_id = value[1]
            teacher_name = value[2]
            teacher_id = value[3]

            teacher = User.objects.get(id=teacher_id)
            if teacher_name != teacher.name:
                raise Exception

            new = TheoryCourse(id=str(curr_time) + str(teacher_id),
                               course_id=course_id,
                               name=name,
                               year=2017,
                               semester=1,
                               teacher=teacher,
                               department_id='471',
                               classes='20160101',
                               student_sum=0,
                               plan_period=0,
                               final_period=0,
                               attribute=1,
                               audit_status=0,
                               workload=0)
            new.save()
        except Exception:
            print(value)
    '''
    '''
    # 导入ExperimentCourse
    worksheet = workbook.sheet_by_name('ExperimentCourse')
    nrows = worksheet.nrows

    curr_time = int(time.time())

    for r in range(0, nrows):
        curr_time += 1
        try:
            value = worksheet.row_values(r, start_colx=0, end_colx=5)
            name = value[0]
            course_id = value[1]
            teacher_name = value[2]
            teacher_id = value[3]

            teacher = User.objects.get(id=teacher_id)
            if teacher_name != teacher.name:
                raise Exception

            new = ExperimentCourse(id=str(curr_time) + str(teacher_id),
                                   course_id=course_id,
                                   name=name,
                                   year=2017,
                                   semester=1,
                                   teacher=teacher,
                                   department_id='471',
                                   classes='20160301',
                                   student_sum=100,
                                   plan_period=0,
                                   final_period=0,
                                   attribute=1,
                                   audit_status=0
                                   )
            new.save()
        except:
            print(value)

    '''
    '''
    teacher_list = User.objects.all()
    i = 0
    for teacher in teacher_list:
        print(i)

        generater = md5(teacher.id.encode("utf8"))
        password = generater.hexdigest()

        teacher.password = make_password(password)
        teacher.save()
        i += 1
        
    '''
    '''
    course_list = TheoryCourse.objects.all()
    for course in course_list:
        course.workload = theory_course_workload_count(course)
        course.save()
    '''
    '''
    user_list = User.objects.all()
    for user in user_list:
        password = user.id
        password += 'zhengzhoudaxueshengmingkexuexueyuanjiaoshigongzuoliangtongjixitong'
        generater = md5(password.encode("utf8"))
        password = generater.hexdigest()
        password = make_password(password)
        user.password = password
        user.save()
    '''
    return render(request, "main/admin/data_import/data_import.html", locals())
