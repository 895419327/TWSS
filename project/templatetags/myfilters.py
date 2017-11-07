# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter()
def get_class_name(classes):
    class_ids = classes.split(',')
    from project.models import Class
    classes_names = ''
    for clas_id in class_ids:
        if clas_id:
            clas = Class.objects.get(id=clas_id)
            classes_names += clas.name
    return classes_names


@register.filter()
def itoc(integer):
    if integer in [1, '1']:
        return u'一'
    elif integer in [2, '2']:
        return u'二'
    else:
        return 'error'


@register.filter()
def stoi(s):
    if s != u'所有':
        return int(s)
    else:
        return