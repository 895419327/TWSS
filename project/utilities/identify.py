# -*- coding: utf-8 -*-

from hashlib import md5
from project.models import User
from project.utilities.log import log


def generate_identify_code(user, username, encrypted_password, captcha):
    identify_code_src = username + encrypted_password + captcha
    generater = md5(identify_code_src.encode("utf8"))
    identify_code = generater.hexdigest()
    return identify_code


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
