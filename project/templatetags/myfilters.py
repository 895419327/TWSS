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


from project.utilities.workload_count import workload_count_func


@register.filter()
def workload_count_course(id):
    theory_course_W, experiment_course_W, pratice_course_W = workload_count_func(id, course=True, project=False)
    return theory_course_W + experiment_course_W + pratice_course_W


@register.filter()
def workload_count_project(id):
    teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W = workload_count_func(id,
                                                                                                         course=False,
                                                                                                         project=True)
    return teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W


@register.filter()
def workload_count_total(id):
    theory_course_W, experiment_course_W, pratice_course_W, teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W = workload_count_func(
        id)
    return theory_course_W + experiment_course_W + pratice_course_W + teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
