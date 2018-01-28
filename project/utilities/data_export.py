import sys
import time

import xlrd
import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from xlutils.copy import copy

from TWSS.settings import BASE_DIR
from project.utilities.identify import check_identity
from project.utilities.log import log
from project.utilities.workload_count import *


# TODO: 按类别导出


def export(request):
    request.encoding = 'utf-8'

    user = check_identity(request)
    if not user:
        return render(request, "main/utilities/unsafe.html")

    requestfor = request.POST['requestfor']
    log('INFO', 'DataExport', user.name, user.id, requestfor, request.POST)
    return getattr(sys.modules[__name__], requestfor)(request, user)


def download_help_pdf(request, user):
    filename = BASE_DIR + '/media/help/' + 'help.pdf'
    file = open(filename, 'rb')
    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment;filename="help.pdf"'
    return response


def teacher_management_export(request, user):
    department_id = request.POST['department_id']
    if department_id == 'all':
        teacher_list = User.objects.filter(department_id__gt='470')
        title = u'生命科学学院教师队伍信息'
    else:
        department = Department.objects.get(id=department_id)
        teacher_list = User.objects.filter(department=department)
        title = department.name + u'系教师队伍信息'

    workbook_template = xlrd.open_workbook(BASE_DIR + '/media/excel/templates/user_info.xls',
                                           formatting_info=True)

    workbook = copy(workbook_template)
    worksheet = workbook.get_sheet(0)

    worksheet.write(0, 0, title, xlwt.easyxf(
        'font: height 480, name 黑体, bold on;'
        ' align: vert centre, horiz centre;'))

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'宋体'
    style.font = font

    row = 3
    for teacher in teacher_list:
        gender = ''
        if teacher.gender == 1:
            gender = u'男'
        elif teacher.gender == 2:
            gender = u'女'

        worksheet.write(row, 0, teacher.id, style)
        worksheet.write(row, 1, teacher.department.name, style)
        worksheet.write(row, 2, teacher.name, style)
        worksheet.write(row, 3, gender, style)
        worksheet.write(row, 4, teacher.birth_date, style)
        worksheet.write(row, 5, teacher.title, style)
        worksheet.write(row, 6, teacher.graduate, style)
        worksheet.write(row, 7, teacher.major, style)
        worksheet.write(row, 8, teacher.email, style)
        worksheet.write(row, 9, teacher.phone_number, style)
        row += 1

    # 时间戳
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    worksheet.write(1, 8, u'导出时间：' + current_time, style)

    # 保存
    filename = BASE_DIR + '/media/excel/user_info/' + current_time + '.xls'
    workbook.save(filename)

    file = open(filename, 'rb')
    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename="user_info.xls"'
    return response


def workload_statistics_export(request, user):
    year = request.POST['year']

    department_id = request.POST['department_id']
    if department_id == 'all':
        teacher_list = User.objects.filter(department_id__gt='470')
        title = year + '-' + str(int(year) + 1) + u'学年' + u'生命科学学院' + u'工作量统计'
    else:
        department = Department.objects.get(id=department_id)
        teacher_list = User.objects.filter(department=department)
        title = year + '-' + str(int(year) + 1) + u'学年' + department.name + u'系工作量统计'

    workbook_template = xlrd.open_workbook(BASE_DIR + '/media/excel/templates/workload_statisitic.xls',
                                           formatting_info=True)
    workbook = copy(workbook_template)
    worksheet = workbook.get_sheet(0)

    worksheet.write(0, 0, title, xlwt.easyxf(
        'font: height 560, name 黑体, bold on;'
        ' align: vert centre, horiz centre;'))

    style = xlwt.easyxf('font: height 200, name 宋体, bold off;')

    style_center = xlwt.easyxf(
        'font: height 300, name 宋体, bold off;'
        ' align: vert centre, horiz centre;')

    start_row = 4
    for teacher in teacher_list:

        row_span = 1

        row = start_row
        theory_course_list = TheoryCourse.objects.filter(teacher=teacher, year=year)
        theory_course_num = theory_course_list.count()
        if theory_course_num >= row_span:
            row_span = theory_course_num
        theory_course_period = 0
        theory_course_W = 0
        for course in theory_course_list:
            worksheet.write(row, 5, course.name, style)
            worksheet.write(row, 6, course.final_period, style)
            worksheet.write(row, 7, round(course.workload, 2), style)

            theory_course_period += course.final_period
            theory_course_W += course.workload
            row += 1

        worksheet.write(row, 5, theory_course_num, style)
        worksheet.write(row, 6, theory_course_period, style)
        worksheet.write(row, 7, round(theory_course_W, 2), style)

        row = start_row
        experiment_course_list = ExperimentCourse.objects.filter(teacher=teacher, year=year)
        experiment_course_num = experiment_course_list.count()
        if experiment_course_num >= row_span:
            row_span = experiment_course_num
        experiment_course_period = 0
        experiment_course_W = 0
        for course in experiment_course_list:
            worksheet.write(row, 5, course.name, style)
            worksheet.write(row, 6, course.final_period, style)
            worksheet.write(row, 7, round(course.workload, 2), style)

            experiment_course_period += course.final_period
            experiment_course_W += course.workload
            row += 1

        worksheet.write(row, 9, experiment_course_num, style)
        worksheet.write(row, 10, experiment_course_period, style)
        worksheet.write(row, 11, round(experiment_course_W, 2), style)

        row = start_row
        pratice_course_list = PraticeCourse.objects.filter(teacher=teacher, year=year)
        pratice_course_num = pratice_course_list.count()
        if pratice_course_num >= row_span:
            row_span = pratice_course_num
        pratice_course_period = 0
        pratice_course_W = 0
        for course in pratice_course_list:
            worksheet.write(row, 13, course.name, style)
            worksheet.write(row, 14, course.final_period, style)
            worksheet.write(row, 15, round(course.workload, 2), style)

            pratice_course_period += course.final_period
            pratice_course_W += pratice_course_workload_count(course)
            row += 1

        worksheet.write(row, 13, pratice_course_num, style)
        worksheet.write(row, 14, pratice_course_period, style)
        worksheet.write(row, 15, round(pratice_course_W, 2), style)

        row = start_row
        teaching_achievement_list = TeachingAchievement.objects.filter(teacher=teacher, year=year)
        teaching_achievement_sum = teaching_achievement_list.count()
        if teaching_achievement_sum >= row_span:
            row_span = teaching_achievement_sum
        teaching_achievement_W = 0
        for project in teaching_achievement_list:
            worksheet.write(row, 19, project.name, style)
            worksheet.write(row, 20, round(project.workload, 2), style)

            teaching_achievement_W += project.workload
            row += 1

        worksheet.write(row, 19, teaching_achievement_sum, style)
        worksheet.write(row, 20, round(teaching_achievement_W, 2), style)

        row = start_row
        teaching_project_list = TeachingProject.objects.filter(teacher=teacher, year=year)
        teaching_project_sum = teaching_project_list.count()
        if teaching_project_sum >= row_span:
            row_span = teaching_project_sum
        teaching_project_W = 0
        for project in teaching_project_list:
            worksheet.write(row, 22, project.name, style)
            worksheet.write(row, 23, round(project.workload, 2), style)

            teaching_project_W += project.workload
            row += 1

        worksheet.write(row, 22, teaching_project_sum, style)
        worksheet.write(row, 23, round(teaching_project_W, 2), style)

        row = start_row
        competition_guide_list = CompetitionGuide.objects.filter(teacher=teacher, year=year)
        competition_guide_sum = competition_guide_list.count()
        competition_guide_W = 0
        for project in competition_guide_list:
            worksheet.write(row, 25, project.name, style)
            worksheet.write(row, 26, round(project.workload, 2), style)

            competition_guide_W += project.workload
            row += 1

        worksheet.write(row, 25, competition_guide_sum, style)
        worksheet.write(row, 26, round(competition_guide_W, 2), style)

        row = start_row
        paper_guide_list = PaperGuide.objects.filter(teacher=teacher, year=year)
        paper_guide_sum = paper_guide_list.count()
        paper_guide_W = 0
        for project in paper_guide_list:
            paper_guide_W += project.workload

        worksheet.write(row, 28, paper_guide_sum, style)
        worksheet.write(row, 29, round(paper_guide_W, 2), style)

        row = start_row
        course_total_W = theory_course_W + experiment_course_W + pratice_course_W
        worksheet.write_merge(row, row + row_span, 17, 17, round(course_total_W, 2), style_center)

        project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
        worksheet.write_merge(row, row + row_span, 31, 31, round(project_total_W, 2), style_center)

        total_W = project_total_W + course_total_W
        worksheet.write_merge(row, row + row_span, 33, 33, round(total_W, 2), style_center)

        row = start_row
        worksheet.write_merge(row, row + row_span, 0, 0, teacher.id, style_center)
        worksheet.write_merge(row, row + row_span, 1, 1, teacher.name, style_center)
        worksheet.write_merge(row, row + row_span, 2, 2, teacher.department.name, style_center)
        worksheet.write_merge(row, row + row_span, 3, 3, teacher.title, style_center)

        start_row += row_span + 1

    # 时间戳
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    worksheet.write(0, 32, u'导出时间：' + current_time, style)

    worksheet.panes_frozen = True
    worksheet.horz_split_pos = 4
    worksheet.vert_split_pos = 4

    # 保存
    filename = BASE_DIR + '/media/excel/workload_statisitic/' + current_time + '.xls'
    workbook.save(filename)

    file = open(filename, 'rb')
    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename="%s.xls"' % year
    return response
