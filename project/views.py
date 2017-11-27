# -*- coding: utf-8 -*-

import os
import time

from django.shortcuts import render
from hashlib import md5

from project.logs.log import log
from project.models import *
from project.utilities.search import *
from project.utilities.indentity import check_identity
from project.utilities.workload_count import workload_count_func

BASE_DIR = os.path.dirname(os.path.abspath(__name__))


def index(request):
    return render(request, 'index/index.html')


# FIXME: VERY-HIGH 工作量统计/审核的搜索bug 搜索后内容正确但搜索栏未更新


# TODO: 教务员工作量系数调整功能

# TODO: 排序

# TODO: 欢迎界面 可以写一些使用帮助

# TODO: 数据库备份
# TODO: 测试覆盖
# TODO: 日志系统


# TODO: 删除班级、教师信息时检查是否有相关引用

# TODO: 防爆破 输入多次密码错误后封ip


# TODO: 移动端可做成微信小程序

def login(request):
    request.encoding = 'utf-8'

    login_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 如果表单为POST提交
    if request.POST:
        # 接收表单数据
        username_post = request.POST['username']
        password_post = request.POST['password']
        status_post = request.POST['status']

        # 检查是否存在此用户
        try:
            user = User.objects.get(id=username_post)
            if password_post == user.password:
                # 验证身份
                if user.status.find(status_post) != -1:
                    # 生成unique_code
                    unique_code_src = username_post + password_post + status_post
                    generater = md5(unique_code_src.encode("utf8"))
                    unique_code = generater.hexdigest()
                    # 记录
                    log('INFO', login_time, 'Login', user.name, user.id, status_post)
                    # 返回相应页面
                    if status_post == u'教师':
                        return render(request, 'main/teacher/teacher.html', locals())
                    if status_post == u'系主任':
                        return render(request, 'main/head_of_department/head_of_department.html', locals())
                    if status_post == u'教务员':
                        return render(request, 'main/dean/dean.html', locals())
                    if status_post == u'系统管理员':
                        return render(request, 'main/admin/admin.html', locals())

        except Exception:
            log('WARNING', login_time, 'Login Fail', username_post, status_post)
            return render(request, 'index/loginfailed.html')

    # 任何意外
    log('ERROR', login_time, 'Login Fail', request.POST)
    return render(request, 'index/loginfailed.html')


def getpage(request):
    request.encoding = 'utf-8'
    # 校验身份
    check_return = check_identity(request)
    if check_return:
        user = check_return
    else:
        return False

    # 获取需求
    requestfor = request.POST['requestfor']
    # try:
    return eval(requestfor)(request, user)
    # except:
    #     print('views.py getpage() exception')
    #     return False


#####  教师  #####
def user_info_user_info(request, user):
    status_post = request.POST['status']
    return render(request, 'main/teacher/user_info/user_info.html', locals())


def user_info_change_password(request, user):
    return render(request, 'main/teacher/user_info/change_password.html', locals())


# FIXME: URGENT 自动检测课程年级

# TODO: 选择班级后更新人数

def get_classes(grade=2017):
    class_list = Class.objects.filter(grade=grade)
    return class_list


def get_classes_module(request, user):
    data = request.POST['request_data'].split(',')
    grade = data[0]
    course_type = data[1]
    id = data[2]


    class_list = Class.objects.filter(grade=grade)
    classes_checked = ''
    if id:
        if course_type == 'TheoryCourse':
            classes_checked = TheoryCourse.objects.get(id=id).classes.split(',')
        elif course_type == 'ExperimentCourse':
            classes_checked = ExperimentCourse.objects.get(id=id).classes.split(',')
        elif course_type == 'PraticeCourse':
            classes_checked = PraticeCourse.objects.get(id=id).classes.split(',')

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
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    location = ''
    if 'extra_data' in request.POST and request.POST['extra_data'] != '':
        location = request.POST['extra_data'].split(',')
        year = location[0]
        semester = location[1]
    # 获取班级信息
    class_list = get_classes(2016)
    modified_course = ''
    if request.POST['request_data']:
        modified_course = TheoryCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
        grade = classes_checked[0][0:4]
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
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    location = ''
    if 'extra_data' in request.POST and request.POST['extra_data'] != '':
        location = request.POST['extra_data'].split(',')
        year = location[0]
        semester = location[1]
    # 获取班级信息
    class_list = get_classes(2016)
    modified_course = ''
    if request.POST['request_data']:
        modified_course = ExperimentCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
        grade = classes_checked[0][0:4]
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
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    location = ''
    if 'extra_data' in request.POST and request.POST['extra_data'] != '':
        location = request.POST['extra_data'].split(',')
        year = location[0]
        semester = location[1]
    # 获取班级信息
    class_list = get_classes(2016)
    modified_course = ''
    if request.POST['request_data']:
        modified_course = PraticeCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
        grade = classes_checked[0][0:4]
        class_list = get_classes(grade)
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course_add.html', locals())


# TODO: search bar 精简 可考虑用{% include %}
# TODO: 新增自动识别type和相应level
# TODO: 教研工作量精简html for type in type_list

# FIXME: 教学成果:教学成果 细分级别未实现

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
        semester = location[1]
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
        semester = location[1]
    if request.POST['request_data']:
        modified_project = TeachingProject.objects.get(id=request.POST['request_data'])
    type_list = [u'专业、团队及实验中心类', u'课程类', u'工程实践教育类', u'教学名师', u'大学生创新创业训练']
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
        semester = location[1]
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
        semester = location[1]

    modified_project = ''
    if request.POST['request_data']:
        modified_project = PaperGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide_add.html', locals())


# Workload Count

def workload_count(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    year = GlobalValue.objects.get(key='current_year').value
    if request.POST['request_data']:
        year = request.POST['request_data'][:4]

    # TODO: 导出功能


    theory_course_W, \
    experiment_course_W, \
    pratice_course_W, \
    teaching_achievement_W, \
    teaching_project_W, \
    competition_guide_W, \
    paper_guide_W \
        = workload_count_func(user, year=year)

    course_total_W = theory_course_W + pratice_course_W + experiment_course_W
    project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
    return render(request, 'main/teacher/workload_count/workload_count.html', locals())


# ##### 系主任 #####
# TODO: 驳回时可填写理由
# TODO: pass和reject可整合
# TODO: 班级管理搜索功能  默认只显示当前四届
# TODO: 考虑在教师表里缓存工作量统计
# TODO: 考虑在系主任查看工作量统计时只统计已审核工作量


def workload_audit_reject_page(request, user):
    data = request.POST['request_data'].split(',')
    project_type = data[0]
    project_id = data[1]
    return render(request, 'main/head_of_department/workload_audit/workload_audit_reject.html', locals())


def workload_audit_reject(request, user):
    project_type = request.POST['project_type']
    if project_type == 'TheoryCourse':
        course = TheoryCourse.objects.get(id=request.POST['project_id'])
        course.audit_status = 1
        course.reject_reason = request.POST['reject_reason']
        course.save()
        course_list = TheoryCourse.objects.all()
        course_list, year, semester, audit_status = search_course_audit(request, course_list)
        return render(request, 'main/head_of_department/workload_audit/theory_course/theory_course_audit.html',
                      locals())
    elif project_type == 'ExperimentCourse':
        course = ExperimentCourse.objects.get(id=request.POST['project_id'])
        course.audit_status = 1
        course.reject_reason = request.POST['reject_reason']
        course.save()
        course_list = ExperimentCourse.objects.all()
        course_list, year, semester, audit_status = search_course_audit(request, course_list)
        return render(request, 'main/head_of_department/workload_audit/experiment_course/experiment_course_audit.html',
                      locals())
    elif project_type == 'PraticeCourse':
        course = PraticeCourse.objects.get(id=request.POST['project_id'])
        course.audit_status = 1
        course.reject_reason = request.POST['reject_reason']
        course.save()
        course_list = PraticeCourse.objects.all()
        course_list, year, semester, audit_status = search_course_audit(request, course_list)
        return render(request, 'main/head_of_department/workload_audit/pratice_course/pratice_course_audit.html',
                      locals())

    # FIXME: URGENT 考虑一个project多个教师 使用同一project_id的情况
    elif project_type == 'TeachingAchievement':
        project = TeachingAchievement.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        project_list = TeachingAchievement.objects.all()
        project_list, year, audit_status = search_project_audit(request, project_list)
        return render(request,
                      'main/head_of_department/workload_audit/teaching_achievement/teaching_achievement_audit.html',
                      locals())
    elif project_type == 'TeachingProject':
        project = TeachingProject.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        project_list = TeachingProject.objects.all()
        project_list, year, audit_status = search_project_audit(request, project_list)
        return render(request,
                      'main/head_of_department/workload_audit/teaching_project/teaching_project_audit.html',
                      locals())
    elif project_type == 'CompetitionGuide':
        project = CompetitionGuide.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        project_list = CompetitionGuide.objects.all()
        project_list, year, audit_status = search_project_audit(request, project_list)
        return render(request,
                      'main/head_of_department/workload_audit/competition_guide/competition_guide_audit.html',
                      locals())
    elif project_type == 'PaperGuide':
        project = PaperGuide.objects.get(id=request.POST['project_id'])
        project.audit_status = 1
        project.reject_reason = request.POST['reject_reason']
        project.save()
        project_list = PaperGuide.objects.all()
        project_list, year, audit_status = search_project_audit(request, project_list)
        return render(request,
                      'main/head_of_department/workload_audit/paper_guide/paper_guide_audit.html',
                      locals())


# 理论课
def workload_audit_theory_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    course_list = TheoryCourse.objects.filter(department=department)
    course_list, year, semester, audit_status = search_course_audit(request, course_list)
    return render(request, 'main/head_of_department/workload_audit/theory_course/theory_course_audit.html', locals())


def workload_audit_theory_course_pass(request, user):
    course = TheoryCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_theory_course(request, user)


# 实验课
def workload_audit_experiment_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    course_list = ExperimentCourse.objects.filter(department=department)
    course_list, year, semester, audit_status = search_course_audit(request, course_list)
    return render(request, 'main/head_of_department/workload_audit/experiment_course/experiment_course_audit.html',
                  locals())


def workload_audit_experiment_course_pass(request, user):
    course = ExperimentCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_experiment_course(request, user)


# 实习实训课
def workload_audit_pratice_course(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    course_list = PraticeCourse.objects.filter(department=department)
    course_list, year, semester, audit_status = search_course_audit(request, course_list)
    return render(request, 'main/head_of_department/workload_audit/pratice_course/pratice_course_audit.html', locals())


def workload_audit_pratice_course_pass(request, user):
    course = PraticeCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_pratice_course(request, user)


# 教学成果
def workload_audit_teaching_achievement(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    project_list = TeachingAchievement.objects.filter(department=department)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request,
                  'main/head_of_department/workload_audit/teaching_achievement/teaching_achievement_audit.html',
                  locals())


def workload_audit_teaching_achievement_pass(request, user):
    course = TeachingAchievement.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_teaching_achievement(request, user)


# 教学项目
def workload_audit_teaching_project(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    project_list = TeachingProject.objects.filter(department=department)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/head_of_department/workload_audit/teaching_project/teaching_project_audit.html',
                  locals())


def workload_audit_teaching_project_pass(request, user):
    course = TeachingProject.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_teaching_project(request, user)


# 竞赛指导
def workload_audit_competition_guide(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    project_list = CompetitionGuide.objects.filter(department=department)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/head_of_department/workload_audit/competition_guide/competition_guide_audit.html',
                  locals())


def workload_audit_competition_guide_pass(request, user):
    course = CompetitionGuide.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_competition_guide(request, user)


# 论文指导
def workload_audit_paper_guide(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    semesters = [u'所有', u'第一学期', u'第二学期']
    audit_status_s = [u'所有', u'未审核', u'审核未通过', u'已审核']

    department = Department.objects.get(head_of_department=user.id)
    project_list = PaperGuide.objects.filter(department=department)
    project_list, year, audit_status = search_project_audit(request, project_list)
    return render(request, 'main/head_of_department/workload_audit/paper_guide/paper_guide_audit.html', locals())


def workload_audit_paper_guide_pass(request, user):
    course = PaperGuide.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_paper_guide(request, user)


###### 教务员 #####

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
    status = user.status.split(',')[1]

    department_list = []
    teacher_list = []
    # 若为教务员
    if status == u'教务员':
        department_list = Department.objects.all()
        teacher_list = User.objects.all()
    # 若为系主任
    elif status == u'系主任':
        department_list = Department.objects.filter(head_of_department=user.id)
        teacher_list = User.objects.filter(department=user.department)
    return render(request, 'main/head_of_department/teacher_management/teacher_management.html', locals())


def teacher_management_add(request, user):
    modified_teacher = ''
    if request.POST['request_data']:
        modified_teacher = User.objects.get(id=request.POST['request_data'])
    return render(request, 'main/head_of_department/teacher_management/teacher_management_add.html', locals())


# 班级管理

def class_management(request, user):
    department_ist = Department.objects.all()
    class_list = Class.objects.all()
    return render(request, 'main/dean/class_management/class_management.html',
                  locals())


def class_management_add(request, user):
    teacher_list = User.objects.all()
    modified_class = ''
    if request.POST['request_data']:
        modified_class = Class.objects.get(id=request.POST['request_data'])
    return render(request, 'main/dean/class_management/class_management_add.html',
                  locals())


# 工作量统计
# 系主任有权调用
def workload_statistics(request, user):
    years = range(2016, int(GlobalValue.objects.get(key='current_year').value) + 1)
    status = user.status.split(',')[1]

    year = GlobalValue.objects.get(key='current_year').value
    if request.POST['request_data']:
        year = request.POST['request_data'][:4]

    department_list = []
    teacher_list = []
    # 若为教务员
    if status == u'教务员':
        department_list = Department.objects.all()
        teacher_list = User.objects.all()
    # 若为系主任
    elif status == u'系主任':
        department_list = Department.objects.filter(head_of_department=user.id)
        teacher_list = User.objects.filter(department=user.department)

    workload_list = []
    for teacher in teacher_list:
        theory_course_W, \
        experiment_course_W, \
        pratice_course_W, \
        teaching_achievement_W, \
        teaching_project_W, \
        competition_guide_W, \
        paper_guide_W \
            = workload_count_func(teacher, year=year)

        course_total_W = theory_course_W + pratice_course_W + experiment_course_W
        project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W

        workload = [teacher.department.id, teacher.name + ' ' + teacher.id, teacher.title, course_total_W,
                    project_total_W]
        workload_list.append(workload)
    return render(request, 'main/head_of_department/workload_statistics/workload_statistics.html', locals())


def workload_K_value(request, user):
    return render(request, "main/dean/workload_K_value/workload_K_value.html", locals())


# # # ADMIN # # #

def database_management(request, user):
    buckups_dir = BASE_DIR + '/project/database_backups'
    backup_infos = []
    for root, dirs, files in os.walk(buckups_dir):
        for file in files:
            create_time = os.path.getctime(buckups_dir + '/' + file)
            create_time_r = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(create_time))

            size = os.path.getsize(buckups_dir + '/' + file)
            size = size / 1000

            info = (create_time, file, create_time_r, size)
            backup_infos.append(info)
    backup_infos.sort()
    backup_infos.reverse()
    return render(request, "main/admin/database_management/database_management.html", locals())


def data_import(request, user):
    return render(request, "main/admin/data_import/data_import.html", locals())


def data_import_a(request, user):
    import xlrd
    workbook = xlrd.open_workbook('/users/vicchen/downloads/data.xlsx')

    # # 导入教师信息
    # worksheet = workbook.sheet_by_name('User')
    # nrows = worksheet.nrows
    #
    # for r in range(0, nrows):
    #     value = worksheet.row_values(r,start_colx=0,end_colx=2)
    #     name = value[0]
    #     teacher_id = str(value[1])
    #
    #     generater = md5(teacher_id.encode("utf8"))
    #     password = generater.hexdigest()
    #
    #     new = User(id=teacher_id,name=name,password=password,department_id='471',status=u'教师')
    #     new.save()

    # 导入TheoryCourse
    worksheet = workbook.sheet_by_name('TheoryCourse')
    nrows = worksheet.nrows

    for r in range(0, nrows):
        value = worksheet.row_values(r, start_colx=0, end_colx=5)
        print(value)

    return render(request, "main/admin/data_import/data_import.html", locals())
