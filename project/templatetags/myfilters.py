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

