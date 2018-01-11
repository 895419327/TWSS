# -*- coding: utf-8 -*-

from django.db import models


class GlobalValue(models.Model):
    # 键
    key = models.CharField(max_length=32, primary_key=True)
    # 值
    value = models.CharField(max_length=32, null=True)
    # 注释
    comment = models.CharField(max_length=32, null=True)

    class Meta:
        # 数据表名
        db_table = 'TWSS_GlobalValue'


# 系部表
class Department(models.Model):
    # 系部编号
    id = models.CharField(max_length=3, default=000, primary_key=True)
    # 系部名称
    name = models.CharField(max_length=8)
    # 系主任
    head_of_department = models.CharField(max_length=16, default=0)

    class Meta:
        # 数据表名
        db_table = 'TWSS_Department'

    def __unicode__(self):
        return self.name


# 用户表
class User(models.Model):
    # 用户名  即教工卡卡号
    id = models.CharField(max_length=16, primary_key=True)
    # 姓名
    name = models.CharField(max_length=16)
    # 性别 (未记录/男/女)
    gender = models.IntegerField(2, default=0, null=True)
    # 出生日期 (yyyy-mm-dd)
    birth_date = models.CharField(max_length=16, null=True)
    # 毕业院校
    graduate = models.CharField(max_length=16, null=True)
    # 专业
    major = models.CharField(max_length=16, null=True)
    # 职称
    title = models.CharField(max_length=16, null=True)
    # 所属系
    department = models.ForeignKey(Department)
    # 权限 (教师/系主任/教务员/系统管理员)
    auth_teacher = models.BooleanField(default=True)
    auth_head_of_department = models.BooleanField(default=False)
    auth_dean = models.BooleanField(default=False)
    auth_admin = models.BooleanField(default=False)
    # 密码 md5加密后的字符串
    password = models.CharField(max_length=128)
    # 手机号
    phone_number = models.CharField(max_length=16, null=True)
    # 邮箱
    email = models.CharField(max_length=32, null=True)
    # identify_code
    identify_code = models.CharField(max_length=64, null=True)

    class Meta:
        # 数据表名
        db_table = 'TWSS_User'

    def __unicode__(self):
        return self.id + ' ' + self.name

    def is_teacher(self):
        return self.auth_teacher

    def is_head_of_department(self):
        return self.auth_head_of_department

    def is_dean(self):
        return self.auth_dean

    def is_admin(self):
        return self.auth_admin


# 班级表
class Class(models.Model):
    # 班级编号
    id = models.CharField(max_length=16, primary_key=True)
    # 班级名称
    name = models.CharField(max_length=16)
    # 所属系
    department = models.ForeignKey(Department, default=0)
    # 所属年级
    grade = models.IntegerField(2048, default=0000)
    # 班级人数
    sum = models.IntegerField(128, default=0)
    # 班主任
    teacher = models.ForeignKey(User, null=True)

    class Meta:
        # 数据表名
        db_table = 'TWSS_Class'

    def __unicode__(self):
        return self.id + ' ' + self.name


class Notice(models.Model):
    # 公告内容
    content = models.TextField(max_length=512, null=True)
    # 发布时间
    post_time = models.DateField()
    # 发布者
    post_by = models.ForeignKey(User)

    class Meta:
        # 数据表名
        db_table = 'TWSS_Notice'

    def __unicode__(self):
        return self.post_by.name + ' ' + str(self.time) + ' ' + self.content


# 课程表 父类
class Course(models.Model):
    # unique id
    id = models.CharField(max_length=32, primary_key=True)
    # 课程编号
    course_id = models.CharField(max_length=16, default='')
    # 课程名称
    name = models.CharField(max_length=32)
    # 学年
    year = models.IntegerField(default=0000)
    # 学期
    semester = models.IntegerField(2, default=0)
    # 授课老师
    teacher = models.ForeignKey(User)
    # 所属系
    department = models.ForeignKey(Department)
    # 上课班级
    classes = models.CharField(max_length=128)
    # 上课人数
    student_sum = models.IntegerField(1024, default=0)
    # 计划课时数
    plan_period = models.IntegerField(128, default=0)
    # 实际课时数
    final_period = models.IntegerField(128, default=0)
    # 属性
    # 理论课 (必修/选修/限选)
    # 实验课 (专业课实验/计算机上机实验/开放实验)
    # 实习/实训课 (市区内认识实习 / 外地认识实习、市区内生产实习 / 外地生产实习、毕业实习、毕业设计(论文))
    attribute = models.IntegerField(4, default=0)
    # 审核状态 (未提交/审核未通过/未审核//已审核) (0/1/2/3)
    audit_status = models.IntegerField(3, default=0)
    # 审核未通过原因
    reject_reason = models.CharField(max_length=64, null=True)
    # 工作量
    workload = models.FloatField(default=0)

    class Meta:
        # 虚类
        abstract = True

    def __unicode__(self):
        return self.course_id + ' ' + self.name + ' ' + self.teacher.name


# 项目表 父类
class Project(models.Model):
    id = models.CharField(max_length=32, primary_key=True, auto_created=True)
    # 项目名称
    name = models.CharField(max_length=128)
    # 学年
    year = models.IntegerField(default=0000)
    # 类型
    # 教学成果 (教研论文/教改项目结项/教学成果/教材)
    # 教学项目 (专业、团队及实验中心类/课程类/工程实践教育中心/教学名师/大学生创新创业训练)
    # 竞赛指导 (全国性大学生学科竞赛/省部级大学生竞赛)
    # 论文指导 (指导本科生发表学术论文)
    type = models.CharField(max_length=16)
    # 老师
    teacher = models.ForeignKey(User)
    # 所属系
    department = models.ForeignKey(Department)
    # 分类
    ############# 教学成果
    # 教研论文    (核心期刊/一般期刊)
    # 教改项目结项 (国家级/省部级/校级)
    # 教学成果*   (国家级/省部级/校级)
    # 教材        (全国统编教材、国家级规划教材、全国教学专业指导委员会指定教材、全国优秀教材 / 其他正式出版教材)
    ############# 教学项目
    # 专业、团队及实验中心类 (国家级/省部级/校级)
    # 课程类      (国家级/省部级/校级)
    # 工程实践教育中心 (国家级)
    # 教学名师    (国家级/省部级/校级)
    # 大学生创新创业训练 (国家级/省部级/校级)
    ############# 竞赛指导
    # 全国性大学生学科竞赛 (特等/一等/二等)
    # 省部级大学生竞赛    (特等/一等/二等)
    ############# 论文指导
    # 指导本科学术论文 (SCI/核心期刊/一般期刊)
    level = models.CharField(max_length=64, null=True)
    # 审核状态 (未提交/审核未通过/未审核/已审核) (0/1/2/3)
    audit_status = models.IntegerField(3, default=0)
    # 审核未通过原因
    reject_reason = models.CharField(max_length=64, null=True)
    # 工作量
    workload = models.FloatField(default=0)

    class Meta:
        # 虚类
        abstract = True

    def __unicode__(self):
        return self.name + ' ' + self.teacher.name


# 理论课
class TheoryCourse(Course):
    class Meta:
        # 数据表名
        db_table = 'TWSS_TheoryCourse'


# 实验课
class ExperimentCourse(Course):
    class Meta:
        # 数据表名
        db_table = 'TWSS_ExperimentCourse'


# 实习实训课
class PraticeCourse(Course):
    class Meta:
        # 数据表名
        db_table = 'TWSS_PraticeCourse'


# 教学成果
class TeachingAchievement(Project):
    # 级别
    # 教学成果      (特等/一等/二等)
    rank = models.CharField(max_length=4, null=True)
    # 发表期刊
    periodical = models.CharField(max_length=64, null=True)
    # 年鉴期
    periodical_issue = models.CharField(max_length=32, null=True)

    class Meta:
        # 数据表名
        db_table = 'TWSS_TeachingAchievement'


# 教学项目
class TeachingProject(Project):
    class Meta:
        # 数据表名
        db_table = 'TWSS_TeachingProject'


# 指导竞赛
class CompetitionGuide(Project):
    # 参赛学生
    students = models.CharField(max_length=32, null=True)

    class Meta:
        # 数据表名
        db_table = 'TWSS_CompetitionGuide'


# 指导论文
class PaperGuide(models.Model):
    id = models.CharField(max_length=32, primary_key=True, auto_created=True)
    # 作者
    student = models.CharField(max_length=16)
    # 学年
    year = models.IntegerField(default=0000)
    # 老师
    teacher = models.ForeignKey(User)
    # 所属系
    department = models.ForeignKey(Department)
    # 审核状态 (未提交/审核未通过/未审核//已审核) (0/1/2/3)
    audit_status = models.IntegerField(3, default=0)
    # 审核未通过原因
    reject_reason = models.CharField(max_length=32, null=True)
    # 工作量
    workload = models.FloatField(default=0)

    class Meta:
        # 数据表名
        db_table = 'TWSS_PaperGuide'
