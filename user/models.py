from django.db import models
# Create your models here.


class Student(models.Model):
    """
    学生
    """
    phone = models.CharField(max_length=32, blank=False, null=False)
    gender = models.CharField(max_length=5, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    grade = models.DateField(blank=False, null=False)
    school = models.CharField(max_length=32, blank=False, null=False)
    major = models.CharField(max_length=32, blank=False, null=False)
    cclass = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return "Student " + str(self.id)


class Teacher(models.Model):
    """
    教师
    """
    phone = models.CharField(max_length=32, blank=False, null=False)
    gender = models.CharField(max_length=5, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    role = models.CharField(max_length=32, blank=False, null=False)
    title = models.CharField(max_length=32, blank=False, null=False)
    diploma = models.CharField(max_length=32, blank=False, null=False)
    school = models.CharField(max_length=32, blank=False, null=False)
    rate_times = models.IntegerField(blank=False, null=False, default=1)
    rate = models.FloatField(default=10.0)

    def __str__(self):
        return "Teacher " + str(self.id)


class Admin(models.Model):
    """
    管理员
    """
    phone = models.CharField(max_length=32, blank=False, null=False)
    role = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return "Admin " + str(self.id)
