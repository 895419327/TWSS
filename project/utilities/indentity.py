# -*- coding: utf-8 -*-

from project.models import User
from project.logs.log import log

# TODO: 生成unique_code
def generate_unique_code(user, info):
    pass


def check_identity(request):
    request.encoding = 'utf-8'

    # 接收表单数据
    username_post = request.POST['username']
    # unique_code = request.POST['unique_code']

    # 校验身份
    try:
        user = User.objects.get(id=username_post)

        # if user:
            # TODO: 添加身份确认
            # from hashlib import md5
            # check_unique_code_src = username_post + user.password + status_post
            # generater = md5(check_unique_code_src.encode("utf8"))
            # check_unique_code = generater.hexdigest()
            #
            # if unique_code == check_unique_code:
            #     return user
            # return user
        return user

    except Exception:
        log(str(Exception))
        return False
