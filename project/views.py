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


# Experiment Course

def workload_input_experiment_course(request, user):
    # 获取账号课程信息
    course_list = ExperimentCourse.objects.filter(teacher_id=user.id)
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course.html', locals())


def workload_input_experiment_course_add(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course_add.html', locals())


def workload_input_experiment_course_modify(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    # modify
    modified_course = ExperimentCourse.objects.get(id=request.POST['request_data'])
    classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course_modify.html', locals())


# Pratice Course

def workload_input_pratice_course(request, user):
    # 获取账号课程信息
    course_list = PraticeCourse.objects.filter(teacher_id=user.id)
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course.html', locals())


def workload_input_pratice_course_add(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course_add.html', locals())


def workload_input_pratice_course_modify(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    # modify
    modified_course = PraticeCourse.objects.get(id=request.POST['request_data'], teacher=user)
    classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course_modify.html', locals())


# Teaching Achievement

def workload_input_teaching_achievement(request, user):
    project_list = TeachingAchievement.objects.filter(teacher_id=user.id)
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement.html', locals())


def workload_input_teaching_achievement_add(request, user):
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement_add.html', locals())


def workload_input_teaching_achievement_modify(request, user):
    modified_project = TeachingAchievement.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement_modify.html',
                  locals())


# Teaching Project

def workload_input_teaching_project(request, user):
    project_list = TeachingProject.objects.filter(teacher_id=user.id)
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project.html', locals())


def workload_input_teaching_project_add(request, user):
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project_add.html', locals())


def workload_input_teaching_project_modify(request, user):
    modified_project = TeachingProject.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project_modify.html',
                  locals())


# Competition Guide

def workload_input_competition_guide(request, user):
    project_list = CompetitionGuide.objects.filter(teacher_id=user.id)
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide.html', locals())


def workload_input_competition_guide_add(request, user):
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide_add.html', locals())


def workload_input_competition_guide_modify(request, user):
    modified_project = CompetitionGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide_modify.html',
                  locals())


# Paper Guide

def workload_input_paper_guide(request, user):
    project_list = PaperGuide.objects.filter(teacher_id=user.id)
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide.html', locals())


def workload_input_paper_guide_add(request, user):
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide_add.html', locals())


def workload_input_paper_guide_modify(request, user):
    modified_project = PaperGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide_modify.html',
                  locals())


# Workload Count

def workload_count(request, user):
    theory_course_W = 0
    theory_course_list = TheoryCourse.objects.filter(teacher=user)
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
    theory_course_W = round(theory_course_W, 2)

    experiment_course_W = 0
    experiment_course_list = ExperimentCourse.objects.filter(teacher=user)
    for course in experiment_course_list:
        L = 0
        if course.attribute == 1:
            L = 0.045
        elif course.attribute == 2:
            L = 0.020
        elif course.attribute == 3:
            L = 0.065
        experiment_course_W += course.period * course.student_sum * L
    experiment_course_W = round(experiment_course_W, 2)

    pratice_course_W = 0
    pratice_course_list = PraticeCourse.objects.filter(teacher=user)
    for course in pratice_course_list:
        S = 0
        if course.attribute == 1:
            S = 0.05
        if course.attribute == 2:
            S = 0.07
        if course.attribute == 3:
            S = 0.09
        teacher_num = len(PraticeCourse.objects.filter(id=course.id))
        pratice_course_W += course.period * course.student_sum * S / teacher_num
    pratice_course_W = round(pratice_course_W, 2)

    teaching_achievement_W = 0
    teaching_achievement_list = TeachingAchievement.objects.filter(teacher=user)
    for project in teaching_achievement_list:
        if project.type == '教研论文':
            if project.level == '核心期刊':
                teaching_achievement_W += 100
            if project.level == '一般期刊':
                teaching_achievement_W += 30

        if project.type == '教改项目结项':
            if project.level == '国家级':
                teaching_achievement_W += 2000
            if project.level == '省部级':
                teaching_achievement_W += 800
            if project.level == '校级':
                teaching_achievement_W += 50

        if project.type == '教学成果':
            if project.level == '国家级':
                if project.rank == '特等':
                    teaching_achievement_W += 20000
                if project.rank == '一等':
                    teaching_achievement_W += 10000
                if project.rank == '二等':
                    teaching_achievement_W += 5000

            if project.level == '省部级':
                if project.rank == '特等':
                    teaching_achievement_W += 3000
                if project.rank == '一等':
                    teaching_achievement_W += 2000
                if project.rank == '二等':
                    teaching_achievement_W += 1000

            if project.level == '校级':
                if project.rank == '特等':
                    teaching_achievement_W += 300
                if project.rank == '一等':
                    teaching_achievement_W += 150
                if project.rank == '二等':
                    teaching_achievement_W += 50

        if project.type == '教材':
            if project.level == '全国统编教材、国家级规划教材、全国教学专业指导委员会指定教材、全国优秀教材':
                teaching_achievement_W += 1500
            if project.level == '其他正式出版教材':
                teaching_achievement_W += 500

    teaching_project_W = 0
    teaching_project_list = TeachingProject.objects.filter(teacher=user)
    for project in teaching_project_list:
        if project.type == '专业、团队及实验中心类':
            if project.level == '国家级':
                teaching_project_W += 10000
            if project.level == '省部级':
                teaching_project_W += 5000
            if project.level == '校级':
                teaching_project_W += 1000

        if project.type == '课程类':
            if project.level == '国家级':
                teaching_project_W += 10000
            if project.level == '省部级':
                teaching_project_W += 2000
            if project.level == '校级':
                teaching_project_W += 400

        if project.type == '工程实践教育中心':
            if project.level == '国家级':
                teaching_project_W += 10000

        if project.type == '教学名师':
            if project.level == '国家级':
                teaching_project_W += 5000
            if project.level == '省部级':
                teaching_project_W += 1000
            if project.level == '校级':
                teaching_project_W += 200

        if project.type == '大学生创新创业训练':
            if project.level == '国家级':
                teaching_project_W += 300
            if project.level == '省部级':
                teaching_project_W += 160
            if project.level == '校级':
                teaching_project_W += 50

    competition_guide_W = 0
    competition_guide_list = CompetitionGuide.objects.filter(teacher=user)
    for project in competition_guide_list:
        if project.type == '全国性大学生学科竞赛':
            if project.level == '特等':
                competition_guide_W += 1000
            if project.level == '一等':
                competition_guide_W += 600
            if project.level == '二等':
                competition_guide_W += 400

        if project.type == '省部级大学生竞赛':
            if project.level == '特等':
                competition_guide_W += 300
            if project.level == '一等':
                competition_guide_W += 200
            if project.level == '二等':
                competition_guide_W += 100

    paper_guide_W = 0
    paper_guide_list = PaperGuide.objects.filter(teacher=user)
    for project in paper_guide_list:
        # TODO:按科研论文奖励外？
        if project.level == 'SCI':
            paper_guide_W += 100
        if project.level == '核心期刊':
            paper_guide_W += 30
        if project.level == '一般期刊':
            paper_guide_W += 10

    course_total_W = theory_course_W + pratice_course_W + experiment_course_W
    project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
    return render(request, 'main/teacher/workload_count/workload_count.html', locals())


# ##### 系主任 #####
# TODO:驳回时可填写理由

# Teacher Management
def teacher_management(request, user):
    department = Department.objects.get(head_of_department=user.id)
    teacher_list = User.objects.filter(department=department)
    return render(request, 'main/head_of_department/teacher_management/teacher_management.html', locals())


# Class Management
def class_management(request, user):
    department = Department.objects.get(head_of_department=user.id)
    class_list = Class.objects.filter(department=department)
    return render(request, 'main/head_of_department/class_management/class_management.html', locals())


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
    department = Department.objects.get(head_of_department=user.id)
    course_list = ExperimentCourse.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_audit/experiment_course/experiment_course_audit.html',
                  locals())


def workload_audit_experiment_course_pass(request, user):
    course = ExperimentCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 2
    course.save()
    return workload_audit_experiment_course(request, user)


def workload_audit_experiment_course_reject(request, user):
    course = ExperimentCourse.objects.get(id=request.POST['request_data'])
    course.audit_status = 1
    course.save()
    return workload_audit_experiment_course(request, user)


# 实习实训课
def workload_audit_pratice_course(request, user):
    department = Department.objects.get(head_of_department=user.id)
    course_list = PraticeCourse.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_audit/pratice_course/pratice_course_audit.html', locals())


def workload_audit_pratice_course_pass(request, user):
    course = PraticeCourse.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 2
    course.save()
    return workload_audit_pratice_course(request, user)


def workload_audit_pratice_course_reject(request, user):
    course = PraticeCourse.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 1
    course.save()
    return workload_audit_pratice_course(request, user)


# 教学成果
def workload_audit_teaching_achievement(request, user):
    department = Department.objects.get(head_of_department=user.id)
    project_list = TeachingAchievement.objects.filter(department=department)
    return render(request,
                  'main/head_of_department/workload_audit/teaching_achievement/teaching_achievement_audit.html',
                  locals())


def workload_audit_teaching_achievement_pass(request, user):
    course = TeachingAchievement.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 2
    course.save()
    return workload_audit_teaching_achievement(request, user)


def workload_audit_teaching_achievement_reject(request, user):
    course = TeachingAchievement.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 1
    course.save()
    return workload_audit_teaching_achievement(request, user)


# 教学项目
def workload_audit_teaching_project(request, user):
    department = Department.objects.get(head_of_department=user.id)
    project_list = TeachingProject.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_audit/teaching_project/teaching_project_audit.html',
                  locals())


def workload_audit_teaching_project_pass(request, user):
    course = TeachingProject.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 2
    course.save()
    return workload_audit_teaching_project(request, user)


def workload_audit_teaching_project_reject(request, user):
    course = TeachingProject.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 1
    course.save()
    return workload_audit_teaching_project(request, user)


# 竞赛指导
def workload_audit_competition_guide(request, user):
    department = Department.objects.get(head_of_department=user.id)
    project_list = CompetitionGuide.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_audit/competition_guide/competition_guide_audit.html',
                  locals())


def workload_audit_competition_guide_pass(request, user):
    course = CompetitionGuide.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 2
    course.save()
    return workload_audit_competition_guide(request, user)


def workload_audit_competition_guide_reject(request, user):
    course = CompetitionGuide.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 1
    course.save()
    return workload_audit_competition_guide(request, user)


# 论文指导
def workload_audit_paper_guide(request, user):
    department = Department.objects.get(head_of_department=user.id)
    project_list = PaperGuide.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_audit/paper_guide/paper_guide_audit.html', locals())


def workload_audit_paper_guide_pass(request, user):
    course = PaperGuide.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 2
    course.save()
    return workload_audit_paper_guide(request, user)


def workload_audit_paper_guide_reject(request, user):
    course = PaperGuide.objects.get(id=request.POST['request_data'], teacher=user)
    course.audit_status = 1
    course.save()
    return workload_audit_paper_guide(request, user)
