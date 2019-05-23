from django.contrib import admin
from .models import Student, Teacher, Admin
# Register your models here.


@admin.register(Student)
class MenuStudent(admin.ModelAdmin):
    list_display = ('phone', 'gender', 'birthday', 'grade', 'school', 'major', 'cclass')


@admin.register(Teacher)
class MenuStudent(admin.ModelAdmin):
    list_display = ('phone', 'role', 'title', 'diploma', 'rate_times', 'rate')


@admin.register(Admin)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('phone', 'role')