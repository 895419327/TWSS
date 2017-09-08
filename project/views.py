# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from project.models import *


def index(request):
    return render(request, 'index/index.html')


def login(request):
    request.encoding = 'utf-8'

    # 如果表单为POST提交
    if request.POST:
        # 接收表单数据
        username_post = request.POST['username']
        password_post = request.POST['password']
        status_post = request.POST['status']

        # 检查是否存在此用户
        # from models import User
        from project.models import User

        user_list = User.objects.filter(id=username_post)
        '''
        用filter而不是get的原因：
        当此用户不存在的时候get会报错"DoesNotExist"
        而filer只会返回一个空对象列表
        '''
        # 用户存在
        if user_list:
            # 遍历列表 虽然列表里只有一个对象
            for user in user_list:
                # 密码正确
                if password_post == user.password:
                    # 验证身份
                    check_status = user.status.find(status_post)
                    # 身份正确
                    if check_status != -1:
                        # 生成unique_code
                        from hashlib import md5
                        unique_code_src = username_post + password_post + status_post
                        generater = md5(unique_code_src.encode("utf8"))
                        unique_code = generater.hexdigest()
                        # 返回相应页面
                        if status_post == u'教师':
                            return render(request, 'main/teacher/teacher.html', locals())
                        if status_post == u'系主任':
                            return render(request, 'main/head_of_department/head_of_department.html', locals())
                        if status_post == u'教务员':
                            return render(request, 'main/dean/dean.html', locals())
                        if status_post == u'系统管理员':
                            return render(request, 'main/admin/admin.html', locals())
                    # 身份错误
                    else:
                        return render(request, 'index/loginfailed.html')

                # 防止意外: user_list里有多个user
                # TODO: 打log报错
                return render(request, 'index/loginfailed.html')

    # 不是为POST提交时(如直接输入URL=/main试图直接进入系统时)
    return render(request, 'index/loginfailed.html')


def getpage(request):
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


#####  教师  #####
def user_info_user_info(request, user):
    status_post = request.POST['status']
    return render(request, 'main/teacher/user_info/user_info.html', locals())


def user_info_change_password(request, user):
    return render(request, 'main/teacher/user_info/change_password.html', locals())


# Theory Course

def workload_input_theory_course(request, user):
    # 获取账号课程信息
    course_list = TheoryCourse.objects.filter(teacher_id=user.id)
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/theory_course/theory_course.html', locals())


def workload_input_theory_course_add(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/theory_course/theory_course_add.html', locals())


def workload_input_theory_course_modify(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    # modify
    modified_course = TheoryCourse.objects.get(id=request.POST['request_data'])
    classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/theory_course/theory_course_modify.html', locals())


def workload_input_experiment_course(request, user):
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course.html', locals())


def workload_input_pratice_course(request, user):
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course.html', locals())


def workload_input_teaching_achievement(request, user):
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement.html', locals())


def workload_input_teaching_project(request, user):
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project.html', locals())


def workload_input_competition_guide(request, user):
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide.html', locals())


def workload_input_paper_guide(request, user):
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide.html', locals())


def workload_count(request, user):
    theory_course_list = TheoryCourse.objects.filter(teacher=user)
    pratice_course_list = PraticeCourse.objects.filter(teacher=user)

    theory_course_W = 0
    for course in theory_course_list:
        K = 0
        if course.student_sum <= 40:
            K = 1.0
        elif course.student_sum <= 85:
            K = 1.6
        elif course.student_sum <= 125:
            K = 2.3
        elif course.student_sum <= 200:
            K = 3.0
        elif course.student_sum > 200:
            K = 3.6
        theory_course_W += 6 + course.period * K

    pratice_course_W = 0
    experiment_course_W = 0
    course_total_W = theory_course_W + pratice_course_W + experiment_course_W
    return render(request, 'main/teacher/workload_count/workload_count.html', locals())


# ##### 系主任 #####

# Teacher Management
def teacher_management(request, user):
    department = Department.objects.get(head_of_department=user.id)
    teacher_list = User.objects.filter(department=department)
    return render(request, 'main/head_of_department/teacher_management/teacher_management.html', locals())


# 理论课
def workload_audit_theory_course(request, user):
    department = Department.objects.get(head_of_department=user.id)
    course_list = TheoryCourse.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_audit/theory_course/theory_course_audit.html', locals())


def workload_audit_theory_course_pass(request, user):
    course = TheoryCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_theory_course(request, user)


def workload_audit_theory_course_reject(request, user):
    course = TheoryCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 1
    course.save()
    return workload_audit_theory_course(request, user)


# 实验课
def workload_audit_experiment_course(request, user):
    return render(request, 'main/head_of_department/workload_audit/experiment_course/experiment_course_audit.html', locals())

# 实习实训课
def workload_audit_pratice_course(request, user):
    return render(request, 'main/head_of_department/workload_audit/pratice_course/pratice_course_audit.html', locals())


# 教学成果
def workload_audit_teaching_achievement(request, user):
    return render(request,
                  'main/head_of_department/workload_audit/teaching_achievement/teaching_achievement_audit.html',
                  locals())


# 教学项目
def workload_audit_teaching_project(request, user):
    return render(request, 'main/head_of_department/workload_audit/teaching_project/teaching_project_audit.html',
                  locals())


# 竞赛指导
def workload_audit_competition_guide(request, user):
    return render(request, 'main/head_of_department/workload_audit/competition_guide/competition_guide_audit.html',
                  locals())


# 论文指导
def workload_audit_paper_guide(request, user):
    return render(request, 'main/head_of_department/workload_audit/paper_guide/paper_guide_audit.html', locals())
