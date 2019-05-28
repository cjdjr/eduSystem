import xadmin
from .models import Course, SC


class CourseAdmin(object):
    list_display = ['id', 'code', 'name', 'score', 'teacher_id', '', 'school']

xadmin.site.register(Course, CourseAdmin)


class SCAdmin(object):
    list_display = ['student_id', 'course_id', 'type', 'score']

xadmin.site.register(SC, SCAdmin)

