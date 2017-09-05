# -*- coding: utf-8 -*-

from django.db import models

import unittest

undefine = u'未记录'


# 用户表
class User(models.Model):
    # 用户名  即教工卡卡号
    id = models.CharField(max_length=16, primary_key=True)
    # 姓名
    name = models.CharField(max_length=16, default=undefine)
    # 职称
    title = models.CharField(max_length=16, default=undefine)
    # 所属系
    department = models.CharField(max_length=8, default=undefine)
    # 身份 (教师/系负责人/教务员)
    status = models.CharField(max_length=16, default=undefine)
    # 密码 md5加密后的字符串
    password = models.CharField(max_length=32, default=undefine)
    # 手机号
    phone_number = models.CharField(max_length=11, default=undefine)
    # 邮箱
    email = models.CharField(max_length=32, default=undefine)

    class Meta:
        # 数据表名
        db_table = 'TWSS_User'

    def __unicode__(self):
        return self.id + ' ' + self.name


# 班级表
class Class(models.Model):
    # 班级编号
    id = models.CharField(max_length=8, primary_key=True)
    # 班级名称
    name = models.CharField(max_length=16, default=undefine)
    # 所属年级
    grade = models.IntegerField(2048, default=0000)
    # 班级人数
    sum = models.IntegerField(128, default=0)
    # 班主任
    teacher = models.ForeignKey(User)

    class Meta:
        # 数据表名
        db_table = 'TWSS_Class'

    def __unicode__(self):
        return self.id + ' ' + self.name


# 课程表 父类
class Course(models.Model):
    # 课程编号
    id = models.CharField(max_length=16, primary_key=True)
    # 课程名称
    name = models.CharField(max_length=32, default=undefine)
    # 学年
    year = models.IntegerField(max_length=12, default=0000)
    # 学期
    semester = models.IntegerField(2, default=0)
    # 授课老师
    teacher = models.ForeignKey(User)
    # 上课班级
    classes = models.CharField(max_length=128, default=undefine)
    # 上课人数
    student_sum = models.IntegerField(1024, default=0)
    # 课时数
    period = models.IntegerField(128, default=0)
    # 学分
    credit = models.IntegerField(8, default=0)
    # 属性 (必修/选修/限选) (1/2/3)
    attribute = models.IntegerField(max_length=4, default=0)
    # 审核状态 (已审核/未审核) (False/True)
    audit_status = models.BooleanField(max_length=4, default=False)

    class Meta:
        # 虚类
        abstract = True

    def __unicode__(self):
        return self.id + ' ' + self.name + self.teacher.name


# 项目表 父类
class Project(models.Model):
    # 项目名称
    name = models.CharField(max_length=128, default=undefine)
    # 类型
    type = models.CharField(max_length=16, default=undefine)
    # 老师
    teacher = models.ForeignKey(User)
    # 作者
    author = models.CharField(max_length=16, default=undefine)
    # 发表期刊
    publish = models.CharField(max_length=128, default=undefine)
    # 所获奖项
    award = models.CharField(max_length=256, default=undefine)
    # 审核状态
    audit_status = models.CharField(max_length=4, default=undefine)

    class Meta:
        # 虚类
        abstract = True

    def __unicode__(self):
        return self.name + self.teacher.name


# 理论课
class TheoryCourse(Course):
    class Meta:
        # 数据表名
        db_table = 'TWSS_TheoryCourse'


# 实习实训课
class PraticeCourse(Course):
    class Meta:
        # 数据表名
        db_table = 'TWSS_PraticeCourse'


# 教学项目
class TeachingProject(Project):
    class Meta:
        # 数据表名
        db_table = 'TWSS_TeachingProject'


# 教学成果
class TeachingAchievement(Project):
    class Meta:
        # 数据表名
        db_table = 'TWSS_TeachingAchievement'


# 指导竞赛
class CompetitionGuide:
    class Meta:
        # 数据表名
        db_table = 'TWSS_CompetitionGuide'


# 指导论文
class PaperGuide:
    class Meta:
        # 数据表名
        db_table = 'TWSS_PaperGuide'
