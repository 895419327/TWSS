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
                        if status_post == u'系负责人':
                            return render(request, 'main/dean/dean.html', locals())
                        if status_post == u'教务员':
                            return render(request, 'main/admin/admin.html', locals())
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

    if requestfor == 'user_info':
        return user_info_page(request, user, )
    if requestfor == 'change_password':
        return change_password_page(request, user)

    if requestfor == 'theory_course':
        return theory_course_page(request, user)
    if requestfor == 'theory_course_add':
        return theory_course_add_page(request, user)
    if requestfor == 'theory_course_modify':
        return theory_course_add_modify(request, user)

    if requestfor == 'pratice_course':
        return pratice_course_page(request, user)
    if requestfor == 'teaching_achievement':
        return teaching_achievement_page(request, user)
    if requestfor == 'teaching_project':
        return teaching_project_page(request, user)
    if requestfor == 'competition_guide':
        return competition_guide_page(request, user)
    if requestfor == 'paper_guide':
        return paper_guide_page(request, user)
    if requestfor == 'workload_count':
        return workload_count_page(request, user)

    return False


def user_info_page(request, user):
    status_post = request.POST['status']
    return render(request, 'main/teacher/user_info/user_info.html', locals())


def change_password_page(request, user):
    return render(request, 'main/teacher/user_info/change_password.html', locals())


# Theory Course

def theory_course_page(request, user):
    # 获取账号课程信息
    theory_course_list = TheoryCourse.objects.filter(teacher_id=user.id)
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/theory_course/theory_course.html', locals())


def theory_course_add_page(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    return render(request, 'main/teacher/workload_input/theory_course/theory_course_add.html', locals())


def theory_course_add_modify(request, user):
    # 获取班级信息
    class_list = Class.objects.filter()
    # modify
    modified_course = TheoryCourse.objects.get(id=request.POST['request_data'])
    classes_checked = modified_course.classes.split(',')
    return render(request, 'main/teacher/workload_input/theory_course/theory_course_modify.html', locals())


# Pratice Course

def pratice_course_page(request, user):
    return render(request, 'main/teacher/workload_input/pratice_course/pratice_course.html', locals())


def teaching_achievement_page(request, user):
    return render(request, 'main/teacher/workload_input/teaching_achievement/teaching_achievement.html', locals())


def teaching_project_page(request, user):
    return render(request, 'main/teacher/workload_input/teaching_project/teaching_project.html', locals())


def competition_guide_page(request, user):
    return render(request, 'main/teacher/workload_input/competition_guide/competition_guide.html', locals())


def paper_guide_page(request, user):
    return render(request, 'main/teacher/workload_input/paper_guide/paper_guide.html', locals())


def workload_count_page(request, user):
    return render(request, 'main/teacher/workload_count/workload_count.html', locals())
