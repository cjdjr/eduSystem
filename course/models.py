from django.db import models
from django.utils import timezone
from rbac.models import UserInfo
# Create your models here.


class Course(models.Model):
    """
    课程
    """
    # Django会自动添加一个id作为主键
    name    = models.CharField(max_length=64, blank=False, null=False)      #课程名称
    score   = models.FloatField(blank=True, null=True, default=0)           #课程学分
    teacher_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='teacher_id')  # 教师id
    time    = models.CharField(max_length=64, blank=False, null=False)      #上课时间
    place   = models.CharField(max_length=64, blank=False, null=False)      #上课地点
    school  = models.CharField(max_length=32, blank=False, null=False)      #开课院系
    code    = models.CharField(max_length=32, blank=False, null=False)      #课程代码

    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.time) + " " + str(self.place)


class SC(models.Model):
    """
    选课表
    """
    ## Django会自动添加一个id作为主键
    student_id      =   models.ForeignKey(UserInfo,on_delete=models.CASCADE, related_name='student_id') #学生id
    course_id       =   models.ForeignKey(Course, on_delete=models.CASCADE)                             #课程id
    type            =   models.CharField(max_length=32, blank=False, null=False)                        #该选课类型
    score           =   models.FloatField(blank=True, null=True, default=0)                             #成绩

    def __str__(self):
        return str(self.id) + " " + str(self.student_id)  + " " + str(self.course_id)

