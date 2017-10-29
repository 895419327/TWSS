from project.models import *


def workload_count_func(user, course=True, project=True, year=GlobalValue.objects.get(key='current_year').value):
    theory_course_W = 0
    experiment_course_W = 0
    pratice_course_W = 0

    teaching_achievement_W = 0
    teaching_project_W = 0
    competition_guide_W = 0
    paper_guide_W = 0

    if course:
        theory_course_list = TheoryCourse.objects.filter(teacher=user, year=year)
        for course in theory_course_list:
            K = 0
            if course.student_sum <= 40:
                K = 1.0
            elif course.student_sum <= 85:
                K = 1.6
            elif course.student_sum <= 125:
                K = 2.3
            elif course.student_sum <= 200:
                K = 3.0
            elif course.student_sum > 200:
                K = 3.6
            theory_course_W += 6 + course.period * K
        theory_course_W = round(theory_course_W, 2)

        experiment_course_list = ExperimentCourse.objects.filter(teacher=user, year=year)
        for course in experiment_course_list:
            L = 0
            if course.attribute == 1:
                L = 0.045
            elif course.attribute == 2:
                L = 0.020
            elif course.attribute == 3:
                L = 0.065
            experiment_course_W += course.period * course.student_sum * L
        experiment_course_W = round(experiment_course_W, 2)

        pratice_course_list = PraticeCourse.objects.filter(teacher=user, year=year)
        for course in pratice_course_list:
            S = 0
            if course.attribute == 1:
                S = 0.05
            if course.attribute == 2:
                S = 0.07
            if course.attribute == 3:
                S = 0.09
            teacher_num = len(PraticeCourse.objects.filter(id=course.id))
            pratice_course_W += course.period * course.student_sum * S / teacher_num
        pratice_course_W = round(pratice_course_W, 2)

    if project:
        teaching_achievement_list = TeachingAchievement.objects.filter(teacher=user, year=year)
        for project in teaching_achievement_list:
            if project.type == '教研论文':
                if project.level == '核心期刊':
                    teaching_achievement_W += 100
                if project.level == '一般期刊':
                    teaching_achievement_W += 30

            if project.type == '教改项目结项':
                if project.level == '国家级':
                    teaching_achievement_W += 2000
                if project.level == '省部级':
                    teaching_achievement_W += 800
                if project.level == '校级':
                    teaching_achievement_W += 50

            if project.type == '教学成果':
                if project.level == '国家级':
                    if project.rank == '特等':
                        teaching_achievement_W += 20000
                    if project.rank == '一等':
                        teaching_achievement_W += 10000
                    if project.rank == '二等':
                        teaching_achievement_W += 5000

                if project.level == '省部级':
                    if project.rank == '特等':
                        teaching_achievement_W += 3000
                    if project.rank == '一等':
                        teaching_achievement_W += 2000
                    if project.rank == '二等':
                        teaching_achievement_W += 1000

                if project.level == '校级':
                    if project.rank == '特等':
                        teaching_achievement_W += 300
                    if project.rank == '一等':
                        teaching_achievement_W += 150
                    if project.rank == '二等':
                        teaching_achievement_W += 50

            if project.type == '教材':
                if project.level == '全国统编教材、国家级规划教材、全国教学专业指导委员会指定教材、全国优秀教材':
                    teaching_achievement_W += 1500
                if project.level == '其他正式出版教材':
                    teaching_achievement_W += 500

        teaching_project_list = TeachingProject.objects.filter(teacher=user, year=year)
        for project in teaching_project_list:
            if project.type == '专业、团队及实验中心类':
                if project.level == '国家级':
                    teaching_project_W += 10000
                if project.level == '省部级':
                    teaching_project_W += 5000
                if project.level == '校级':
                    teaching_project_W += 1000

            if project.type == '课程类':
                if project.level == '国家级':
                    teaching_project_W += 10000
                if project.level == '省部级':
                    teaching_project_W += 2000
                if project.level == '校级':
                    teaching_project_W += 400

            if project.type == '工程实践教育中心':
                if project.level == '国家级':
                    teaching_project_W += 10000

            if project.type == '教学名师':
                if project.level == '国家级':
                    teaching_project_W += 5000
                if project.level == '省部级':
                    teaching_project_W += 1000
                if project.level == '校级':
                    teaching_project_W += 200

            if project.type == '大学生创新创业训练':
                if project.level == '国家级':
                    teaching_project_W += 300
                if project.level == '省部级':
                    teaching_project_W += 160
                if project.level == '校级':
                    teaching_project_W += 50

        competition_guide_list = CompetitionGuide.objects.filter(teacher=user, year=year)
        for project in competition_guide_list:
            if project.type == '全国性大学生学科竞赛':
                if project.level == '特等':
                    competition_guide_W += 1000
                if project.level == '一等':
                    competition_guide_W += 600
                if project.level == '二等':
                    competition_guide_W += 400

            if project.type == '省部级大学生竞赛':
                if project.level == '特等':
                    competition_guide_W += 300
                if project.level == '一等':
                    competition_guide_W += 200
                if project.level == '二等':
                    competition_guide_W += 100

        paper_guide_list = PaperGuide.objects.filter(teacher=user, year=year)
        for project in paper_guide_list:
            # TODO:按科研论文奖励除外是什么意思？
            if project.level == 'SCI':
                paper_guide_W += 100
            if project.level == '核心期刊':
                paper_guide_W += 30
            if project.level == '一般期刊':
                paper_guide_W += 10

    if course and project:
        return theory_course_W, experiment_course_W, pratice_course_W, teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W
    elif course:
        return theory_course_W, experiment_course_W, pratice_course_W
    elif project:
        return teaching_achievement_W, teaching_project_W, competition_guide_W, paper_guide_W
