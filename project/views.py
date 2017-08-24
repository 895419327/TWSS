# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index/index.html', locals())


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
                        # 获取账号相关数据
                        # 课程信息
                        from project.models import TheoryCourse
                        theory_course_list = TheoryCourse.objects.filter(teacher_id=user.id)

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
