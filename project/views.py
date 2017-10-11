# -*- coding: utf-8 -*-

from django.shortcuts import render

from project.models import *


def index(request):
    return render(request, 'index/index.html')


# TODO: 教务员身份

# FIXME: 修改/删除/审核后会跳回默认查询的界面而不是审核时的界面

# TODO: 数据库备份
# TODO: 测试覆盖
# TODO: 日志系统

# TODO: 如果有空的话...把MyAjax和MyAjax_Get优化掉...

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

        try:
            user = User.objects.get(id=username_post)
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

        except:
            return render(request, 'index/loginfailed.html')

    # 任何意外
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


from project.utilities.search import *


# TODO: 所有新增界面改为fixed

# Theory Course

def workload_input_theory_course(request, user):
    # 获取账号课程信息
    course_list = TheoryCourse.objects.filter(teacher_id=user.id)
    course_list, year, semester = search(request, course_list)
    return render(request, 'main/teacher/workload_input/theory_course/theory_course.html', locals())


def workload_input_theory_course_add(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    modified_course = ''
    if (request.POST['request_data']):
        modified_course = TheoryCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/theory_course/theory_course_add.html', locals())


# Experiment Course

def workload_input_experiment_course(request, user):
    # 获取账号课程信息
    course_list = ExperimentCourse.objects.filter(teacher_id=user.id)
    course_list, year, semester = search(request, course_list)
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course.html', locals())


def workload_input_experiment_course_add(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    modified_course = ''
    if (request.POST['request_data']):
        modified_course = ExperimentCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/experiment_course/experiment_course_add.html', locals())


# Pratice Course

def workload_input_pratice_course(request, user):
    # 获取账号课程信息
    course_list = PraticeCourse.objects.filter(teacher_id=user.id)
    course_list, year, semester = search(request, course_list)
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course.html', locals())


def workload_input_pratice_course_add(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    modified_course = ''
    if (request.POST['request_data']):
        modified_course = PraticeCourse.objects.get(id=request.POST['request_data'])
        classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course_add.html', locals())


# TODO: search bar 精简 可考虑用{% include %}
# TODO: 新增自动识别type和相应level
# TODO: 教研工作量精简html for type in type_list

# TODO: 教学成果:教学成果 细分级别未实现

# Teaching Achievement

def workload_input_teaching_achievement(request, user):
    project_list = TeachingAchievement.objects.filter(teacher_id=user.id)
    project_list, year, semester = search(request, project_list)
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement.html', locals())


def workload_input_teaching_achievement_add(request, user):
    modified_project = ''
    if (request.POST['request_data']):
        modified_project = TeachingAchievement.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement_add.html', locals())


# Teaching Project
def workload_input_teaching_project(request, user):
    project_list = TeachingProject.objects.filter(teacher_id=user.id)
    project_list, year, semester = search(request, project_list)
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project.html', locals())


def workload_input_teaching_project_add(request, user):
    modified_project = ''
    if (request.POST['request_data']):
        modified_project = TeachingProject.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project_add.html', locals())


# Competition Guide

def workload_input_competition_guide(request, user):
    project_list = CompetitionGuide.objects.filter(teacher_id=user.id)
    project_list, year, semester = search(request, project_list)
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide.html', locals())


def workload_input_competition_guide_add(request, user):
    modified_project = ''
    if (request.POST['request_data']):
        modified_project = CompetitionGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide_add.html', locals())


# Paper Guide

def workload_input_paper_guide(request, user):
    project_list = PaperGuide.objects.filter(teacher_id=user.id)
    project_list, year, semester = search(request, project_list)
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide.html', locals())


def workload_input_paper_guide_add(request, user):
    modified_project = ''
    if (request.POST['request_data']):
        modified_project = PaperGuide.objects.get(id=request.POST['request_data'])
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide_add.html', locals())


# Workload Count

def workload_count(request, user):
    # TODO: 导出功能
    from project.utilities.workload_count import workload_count_func

    theory_course_W, experiment_course_W, pratice_course_W, teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W = workload_count_func(
        user)

    course_total_W = theory_course_W + pratice_course_W + experiment_course_W
    project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
    return render(request, 'main/teacher/workload_count/workload_count.html', locals())


# ##### 系主任 #####
# TODO: 驳回时可填写理由
# TODO: pass和reject可整合

# Teacher Management
def teacher_management(request, user):
    department = Department.objects.get(head_of_department=user.id)
    teacher_list = User.objects.filter(department=department)
    return render(request, 'main/head_of_department/teacher_management/teacher_management.html', locals())


def teacher_management_add(request, user):
    modified_teacher = ''
    if (request.POST['request_data']):
        modified_teacher = User.objects.get(id=request.POST['request_data'])
    return render(request, 'main/head_of_department/teacher_management/teacher_management_add.html', locals())

# Class Management
def class_management(request, user):
    department = Department.objects.get(head_of_department=user.id)
    class_list = Class.objects.filter(department=department)
    return render(request, 'main/head_of_department/class_management/class_management.html', locals())


def class_management_add(request, user):
    department = Department.objects.get(head_of_department=user.id)
    teacher_list = User.objects.filter(department=department)
    modified_class = ''
    if (request.POST['request_data']):
        modified_class = Class.objects.get(id=request.POST['request_data'])
    return render(request, 'main/head_of_department/class_management/class_management_add.html', locals())

# 理论课
def workload_audit_theory_course(request, user):
    department = Department.objects.get(head_of_department=user.id)
    course_list = TheoryCourse.objects.filter(department=department)
    course_list, year, semester, audit_status = audit_search(request, course_list)
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
    course_list, year, semester, audit_status = audit_search(request, course_list)
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
    course_list, year, semester, audit_status = audit_search(request, course_list)
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
    project_list, year, semester, audit_status = audit_search(request, project_list)
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
    project_list, year, semester, audit_status = audit_search(request, project_list)
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
    project_list, year, semester, audit_status = audit_search(request, project_list)
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
    project_list, year, semester, audit_status = audit_search(request, project_list)
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


def workload_statistics(request, user):
    department = Department.objects.get(head_of_department=user.id)
    teacher_list = User.objects.filter(department=department)
    return render(request, 'main/head_of_department/workload_statistics/workload_statistics.html', locals())
