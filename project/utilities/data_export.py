import os
import time

from django.http import HttpResponse, StreamingHttpResponse

import xlwt
import xlrd
from xlutils.copy import copy

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

from project.models import *
from project.utilities.workload_count import *
from project.utilities.indentity import check_identity


def export(request):
    request.encoding = 'utf-8'

    user = check_identity(request)
    if not user:
        return False  # 返回错误信息

    requestfor = request.POST['requestfor']
    return eval(requestfor)(request, user)


def workload_statistics_export(request, user):
    department_id = request.POST['department_id']
    department = Department.objects.get(id=department_id)

    teacher_list = User.objects.filter(department=department)

    workbook_template = xlrd.open_workbook(BASE_DIR + '/media/excel/templates/workload_statisitic.xls',
                                           formatting_info=True)
    workbook = copy(workbook_template)
    worksheet = workbook.get_sheet(0)

    year = GlobalValue.objects.get(key='current_year').value
    title = year + '-' + str(int(year) + 1) + u'学年' + department.name + '系工作量统计'
    worksheet.write(0, 0, title, xlwt.easyxf(
        'font: height 560, name 黑体, bold on;'
        ' align: vert centre, horiz centre;'))

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'宋体'
    style.font = font

    row = 4
    for teacher in teacher_list:
        gender = ''
        if teacher.gender == 1:
            gender = u'男'
        elif teacher.gender == 2:
            gender = u'女'

        worksheet.write(row, 0, teacher.id, style)
        worksheet.write(row, 1, teacher.name, style)
        worksheet.write(row, 2, gender, style)
        worksheet.write(row, 3, teacher.title, style)

        theory_course_list = TheoryCourse.objects.filter(teacher=teacher)
        theory_course_num = theory_course_list.count()
        theory_course_period = 0
        theory_course_W = 0
        for course in theory_course_list:
            theory_course_period += course.final_period
            theory_course_W += course.workload

        worksheet.write(row, 5, theory_course_num, style)
        worksheet.write(row, 6, theory_course_period, style)
        worksheet.write(row, 7, theory_course_W, style)

        experiment_course_list = ExperimentCourse.objects.filter(teacher=teacher)
        experiment_course_num = experiment_course_list.count()
        experiment_course_period = 0
        experiment_course_W = 0
        for course in experiment_course_list:
            experiment_course_period += course.final_period
            experiment_course_W += course.workload

        worksheet.write(row, 9, experiment_course_num, style)
        worksheet.write(row, 10, experiment_course_period, style)
        worksheet.write(row, 11, experiment_course_W, style)

        pratice_course_list = PraticeCourse.objects.filter(teacher=teacher)
        pratice_course_num = pratice_course_list.count()
        pratice_course_period = 0
        pratice_course_W = 0
        for course in pratice_course_list:
            pratice_course_period += course.final_period
            pratice_course_W += pratice_course_workload_count(course)

        worksheet.write(row, 13, pratice_course_num, style)
        worksheet.write(row, 14, pratice_course_period, style)
        worksheet.write(row, 15, pratice_course_W, style)

        course_total_W = theory_course_W + experiment_course_W + pratice_course_W
        worksheet.write(row, 17, course_total_W, style)

        teaching_achievement_list = TeachingAchievement.objects.filter(teacher=teacher)
        teaching_achievement_sum = teaching_achievement_list.count()
        teaching_achievement_W = 0
        for project in teaching_achievement_list:
            teaching_achievement_W += project.workload

        worksheet.write(row, 19, teaching_achievement_sum, style)
        worksheet.write(row, 20, teaching_achievement_W, style)

        teaching_project_list = TeachingProject.objects.filter(teacher=teacher)
        teaching_project_sum = teaching_project_list.count()
        teaching_project_W = 0
        for project in teaching_project_list:
            teaching_project_W += project.workload

        worksheet.write(row, 22, teaching_project_sum, style)
        worksheet.write(row, 23, teaching_project_W, style)

        competition_guide_list = CompetitionGuide.objects.filter(teacher=teacher)
        competition_guide_sum = competition_guide_list.count()
        competition_guide_W = 0
        for project in competition_guide_list:
            competition_guide_W += project.workload

        worksheet.write(row, 25, competition_guide_sum, style)
        worksheet.write(row, 26, competition_guide_W, style)

        paper_guide_list = PaperGuide.objects.filter(teacher=teacher)
        paper_guide_sum = paper_guide_list.count()
        paper_guide_W = 0
        for project in paper_guide_list:
            paper_guide_W += project.workload

        worksheet.write(row, 28, paper_guide_sum, style)
        worksheet.write(row, 29, paper_guide_W, style)

        project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
        worksheet.write(row, 31, project_total_W, style)

        total_W = project_total_W + course_total_W
        worksheet.write(row, 33, total_W, style)

        row += 1

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    filename = BASE_DIR + '/media/excel/workload_statisitic/' + current_time + '.xls'
    workbook.save(filename)

    file = open(filename, 'rb')
    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename="%s.xls"' % (year + department.id)
    return response

# 将user_info写入excel并返回
# def user_info_to_excel(request, user):
#     # 打开模板
#     workbook_template = xlrd.open_workbook(os.path.join(MEDIA_PATH, 'excel', 'templates', 'user_info.xls'),
#                                            formatting_info=True)
#     # 拷贝模板workbook
#     workbook = copy(workbook_template)
#     # 打开worksheet
#     worksheet = workbook.get_sheet(0)
# 
#     # 设置字体格式
#     style = xlwt.XFStyle()
#     font = xlwt.Font()
#     font.name = u'宋体'
#     style.font = font
# 
#     # 写入数据
#     worksheet.write(2, 0, user.id, style)
#     worksheet.write(2, 1, user.name, style)
#     worksheet.write(2, 3, user.status, style)
#     worksheet.write(2, 4, user.phone_number, style)
# 
#     # 保存
#     filename = os.path.join(MEDIA_PATH, 'excel', 'user_info', user.id + '.xls')
#     workbook.save(filename)
#     file = open(filename)
#     # 封装
#     wrapper = FileWrapper(file)
# 
#     # 配置reponse 返回文件
#     response = HttpResponse(wrapper)
#     response['Content-Type'] = 'text/octet-stream'
#     response['Content-Disposition'] = 'attachment; filename="%s.xls"' % user.id
#     return response
