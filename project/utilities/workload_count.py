import math
from project.models import *

# 新增课程时
# 各数据是从request里得到的
# 因此类型都为str
# 需要进行转换

def theory_course_workload_count(course):
    K = 0

    # if course.student_sum <= 40:
    #     K = 1.0
    # elif course.student_sum <= 85:
    #     K = 1.6
    # elif course.student_sum <= 125:
    #     K = 2.3
    # elif course.student_sum <= 200:
    #     K = 3.0
    # elif course.student_sum > 200:
    #     K = 3.6
    #
    # workload = 6 + int(course.final_period) * K

    # 新标准
    if course.student_sum <= 60:
        K = 1.0
    else:
        K = 1 + 0.6 * math.log(course.student_sum / 60)

    workload = int(course.final_period) * K
    workload = round(workload, 2)
    return workload


def experiment_course_workload_count(course):
    L = 0
    if course.attribute == 1:
        L = 0.027
    elif course.attribute == 2:
        L = 0.020
    elif course.attribute == 3:
        L = 0.065

    workload = int(course.final_period) * int(course.student_sum) * L
    return workload


def pratice_course_workload_count(course):
    S = 0
    if course.attribute == 1:
        S = 0.05
    if course.attribute == 2:
        S = 0.07
    if course.attribute == 3:
        S = 0.09

    teacher_num = len(PraticeCourse.objects.filter(course_id=course.course_id))
    # 一门实习实训课有多个老师 第一次录入时 此时该记录仍未存入数据库 teacher_num为0
    if teacher_num == 0:
        teacher_num = 1
    workload = int(course.final_period) * course.student_sum * S / teacher_num
    return workload


def teaching_achievement_workload_count(project):
    if project.type == '教研论文':
        if project.level == '核心期刊':
            return 100
        if project.level == '一般期刊':
            return 30

    if project.type == '教改项目结项':
        if project.level == '国家级':
            return 2000
        if project.level == '省部级':
            return 800
        if project.level == '校级':
            return 50

    if project.type == '教学成果':
        if project.level == '国家级':
            if project.rank == '特等':
                return 20000
            if project.rank == '一等':
                return 10000
            if project.rank == '二等':
                return 5000

        if project.level == '省部级':
            if project.rank == '特等':
                return 3000
            if project.rank == '一等':
                return 2000
            if project.rank == '二等':
                return 1000

        if project.level == '校级':
            if project.rank == '特等':
                return 300
            if project.rank == '一等':
                return 150
            if project.rank == '二等':
                return 50

    if project.type == '教材':
        if project.level == '全国统编教材、国家级规划教材、全国教学专业指导委员会指定教材、全国优秀教材':
            return 1500
        if project.level == '其他正式出版教材':
            return 500


def teaching_project_workload_count(project):
    if project.type == '专业、团队及实验中心类':
        if project.level == '国家级':
            return 10000
        if project.level == '省部级':
            return 5000
        if project.level == '校级':
            return 1000

    if project.type == '课程类':
        if project.level == '国家级':
            return 10000
        if project.level == '省部级':
            return 2000
        if project.level == '校级':
            return 400

    if project.type == '工程实践教育中心':
        if project.level == '国家级':
            return 10000

    if project.type == '教学名师':
        if project.level == '国家级':
            return 5000
        if project.level == '省部级':
            return 1000
        if project.level == '校级':
            return 200

    if project.type == '大学生创新创业训练':
        if project.level == '国家级':
            return 300
        if project.level == '省部级':
            return 160
        if project.level == '校级':
            return 50


def competition_guide_workload_count(project):
    if project.type == '全国性大学生学科竞赛':
        if project.level == '特等':
            return 1000
        if project.level == '一等':
            return 600
        if project.level == '二等':
            return 400

    if project.type == '省部级大学生竞赛':
        if project.level == '特等':
            return 300
        if project.level == '一等':
            return 200
        if project.level == '二等':
            return 100


def papar_guide_workload_count(project):
    return 15


def workload_count(teacher, year=2017, is_audit=True, course=True, project=True):
    theory_course_W = 0
    experiment_course_W = 0
    pratice_course_W = 0

    teaching_achievement_W = 0
    teaching_project_W = 0
    competition_guide_W = 0
    paper_guide_W = 0

    if course:
        # Theory Course
        theory_course_list = TheoryCourse.objects.filter(teacher=teacher, year=year)
        if is_audit:
            theory_course_list = theory_course_list.filter(audit_status=3)
        for course in theory_course_list:
            theory_course_W += course.workload

        # Experiment Course
        experiment_course_list = ExperimentCourse.objects.filter(teacher=teacher, year=year)
        if is_audit:
            experiment_course_list = experiment_course_list.filter(audit_status=3)
        for course in experiment_course_list:
            experiment_course_W += course.workload

        # Pratice Course
        pratice_course_list = PraticeCourse.objects.filter(teacher=teacher, year=year)
        if is_audit:
            pratice_course_list = pratice_course_list.filter(audit_status=3)
        for course in pratice_course_list:
            course.workload = pratice_course_workload_count(course)
            course.save()
            pratice_course_W += course.workload

        # 保留两位小数
        theory_course_W = round(theory_course_W, 2)
        experiment_course_W = round(experiment_course_W, 2)
        pratice_course_W = round(pratice_course_W, 2)

    if project:
        # Teaching Achievement
        teaching_achievement_list = TeachingAchievement.objects.filter(teacher=teacher, year=year)
        if is_audit:
            teaching_achievement_list = teaching_achievement_list.filter(audit_status=3)
        for project in teaching_achievement_list:
            teaching_achievement_W += project.workload

        # Teaching Project
        teaching_project_list = TeachingProject.objects.filter(teacher=teacher, year=year)
        if is_audit:
            teaching_project_list = teaching_project_list.filter(audit_status=3)
        for project in teaching_project_list:
            teaching_project_W += project.workload

        # Competition Guide
        competition_guide_list = CompetitionGuide.objects.filter(teacher=teacher, year=year)
        if is_audit:
            competition_guide_list = competition_guide_list.filter(audit_status=3)
        for project in competition_guide_list:
            competition_guide_W += project.workload

        # Paper Guide
        paper_guide_list = PaperGuide.objects.filter(teacher=teacher, year=year)
        if is_audit:
            paper_guide_list = paper_guide_list.filter(audit_status=3)
        for project in paper_guide_list:
            paper_guide_W += project.workload

    if course and project:
        return theory_course_W, experiment_course_W, pratice_course_W, teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W
    elif course:
        return theory_course_W, experiment_course_W, pratice_course_W
    elif project:
        return teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W
