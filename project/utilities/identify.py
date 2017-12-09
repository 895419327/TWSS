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
    identify_code = request.POST['identify_code']

    # 校验身份
    try:
        user = User.objects.get(id=username_post)
    except Exception:
        log('WARNING', 'Check Identify Exception: username not found', username_post)
        return False

    if user.identify_code == identify_code:
        return user
    else:
        log('WARNING', 'Check Identify Exception: identify code uncorrect', username_post)
        return False

