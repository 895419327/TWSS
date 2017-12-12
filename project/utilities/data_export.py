import time

from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

import xlwt
import xlrd
from xlutils.copy import copy

from TWSS.settings import BASE_DIR

from project.models import *
from project.logs.log import log
from project.utilities.workload_count import *
from project.utilities.identify import check_identity


def export(request):
    request.encoding = 'utf-8'

    user = check_identity(request)
    if not user:
        return render(request, "main/utilities/unsafe.html")

    requestfor = request.POST['requestfor']
    log('INFO', 'DataExport', user.name, user.id, requestfor, request.POST)
    return eval(requestfor)(request, user)


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
        worksheet.write(row, 4, str(teacher.birth_date), style)
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

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'宋体'
    style.font = font

    row = 4
    for teacher in teacher_list:

        worksheet.write(row, 0, teacher.id, style)
        worksheet.write(row, 1, teacher.name, style)
        worksheet.write(row, 2, teacher.department.name, style)
        worksheet.write(row, 3, teacher.title, style)

        theory_course_list = TheoryCourse.objects.filter(teacher=teacher, year=year)
        theory_course_num = theory_course_list.count()
        theory_course_period = 0
        theory_course_W = 0
        for course in theory_course_list:
            theory_course_period += course.final_period
            theory_course_W += course.workload

        worksheet.write(row, 5, theory_course_num, style)
        worksheet.write(row, 6, theory_course_period, style)
        worksheet.write(row, 7, round(theory_course_W, 2), style)

        experiment_course_list = ExperimentCourse.objects.filter(teacher=teacher, year=year)
        experiment_course_num = experiment_course_list.count()
        experiment_course_period = 0
        experiment_course_W = 0
        for course in experiment_course_list:
            experiment_course_period += course.final_period
            experiment_course_W += course.workload

        worksheet.write(row, 9, experiment_course_num, style)
        worksheet.write(row, 10, experiment_course_period, style)
        worksheet.write(row, 11, round(experiment_course_W, 2), style)

        pratice_course_list = PraticeCourse.objects.filter(teacher=teacher, year=year)
        pratice_course_num = pratice_course_list.count()
        pratice_course_period = 0
        pratice_course_W = 0
        for course in pratice_course_list:
            pratice_course_period += course.final_period
            pratice_course_W += pratice_course_workload_count(course)

        worksheet.write(row, 13, pratice_course_num, style)
        worksheet.write(row, 14, pratice_course_period, style)
        worksheet.write(row, 15, round(pratice_course_W, 2), style)

        course_total_W = theory_course_W + experiment_course_W + pratice_course_W
        worksheet.write(row, 17, round(course_total_W, 2), style)

        teaching_achievement_list = TeachingAchievement.objects.filter(teacher=teacher, year=year)
        teaching_achievement_sum = teaching_achievement_list.count()
        teaching_achievement_W = 0
        for project in teaching_achievement_list:
            teaching_achievement_W += project.workload

        worksheet.write(row, 19, teaching_achievement_sum, style)
        worksheet.write(row, 20, round(teaching_achievement_W, 2), style)

        teaching_project_list = TeachingProject.objects.filter(teacher=teacher, year=year)
        teaching_project_sum = teaching_project_list.count()
        teaching_project_W = 0
        for project in teaching_project_list:
            teaching_project_W += project.workload

        worksheet.write(row, 22, teaching_project_sum, style)
        worksheet.write(row, 23, round(teaching_project_W, 2), style)

        competition_guide_list = CompetitionGuide.objects.filter(teacher=teacher, year=year)
        competition_guide_sum = competition_guide_list.count()
        competition_guide_W = 0
        for project in competition_guide_list:
            competition_guide_W += project.workload

        worksheet.write(row, 25, competition_guide_sum, style)
        worksheet.write(row, 26, round(competition_guide_W, 2), style)

        paper_guide_list = PaperGuide.objects.filter(teacher=teacher, year=year)
        paper_guide_sum = paper_guide_list.count()
        paper_guide_W = 0
        for project in paper_guide_list:
            paper_guide_W += project.workload

        worksheet.write(row, 28, paper_guide_sum, style)
        worksheet.write(row, 29, round(paper_guide_W, 2), style)

        project_total_W = teaching_achievement_W + teaching_project_W + competition_guide_W + paper_guide_W
        worksheet.write(row, 31, round(project_total_W, 2), style)

        total_W = project_total_W + course_total_W
        worksheet.write(row, 33, round(total_W, 2), style)

        row += 1

    # 时间戳
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    worksheet.write(0, 32, u'导出时间：' + current_time, style)

    # 保存
    filename = BASE_DIR + '/media/excel/workload_statisitic/' + current_time + '.xls'
    workbook.save(filename)

    file = open(filename, 'rb')
    response = HttpResponse(file.read())
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename="%s.xls"' % year
    return response
