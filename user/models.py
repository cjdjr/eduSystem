from django.db import models
# Create your models here.


class Student(models.Model):
    """
    学生
    """
    phone = models.CharField('手机号', max_length=32, blank=False, null=False)
    gender = models.CharField('性别', max_length=5, blank=False, null=False)
    birthday = models.DateField('出生日期', blank=False, null=False)
    grade = models.DateField('入学时间', blank=False, null=False)
    school = models.CharField('院系', max_length=32, blank=False, null=False)
    major = models.CharField('专业', max_length=32, blank=False, null=False)
    cclass = models.CharField('班级', max_length=32, blank=False, null=False)

    class Meta:
        verbose_name = '学生资料管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "Student " + str(self.id)


class Teacher(models.Model):
    """
    教师
    """
    phone = models.CharField('手机号', max_length=32, blank=False, null=False)
    gender = models.CharField('性别', max_length=5, blank=False, null=False)
    birthday = models.DateField('出生日期', blank=False, null=False)
    role = models.CharField('角色', max_length=32, blank=False, null=False)
    title = models.CharField('职称', max_length=32, blank=False, null=False)
    diploma = models.CharField('学位', max_length=32, blank=False, null=False)
    school = models.CharField('院系', max_length=32, blank=False, null=False)
    rate_times = models.IntegerField('评分次数', blank=False, null=False, default=1)
    rate = models.FloatField('评分', default=10.0)

    class Meta:
        verbose_name = '教师资料管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "Teacher " + str(self.id)


class Admin(models.Model):
    """
    管理员
    """
    phone = models.CharField('手机号', max_length=32, blank=False, null=False)
    role = models.CharField('角色', max_length=32, blank=False, null=False)

    class Meta:
        verbose_name = '管理员资料管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "Admin " + str(self.id)
