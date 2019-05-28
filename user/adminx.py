import xadmin
from xadmin import views
from .models import Student, Teacher, Admin

# 在xadmin中注册Student
class StudentAdmin(object):
    list_display = ['phone', 'gender', 'birthday', 'grade', 'school', 'major', 'cclass']
    list_filter = ['phone', 'gender', 'birthday', 'grade', 'school', 'major', 'cclass']
    search_fields = ['phone', 'gender', 'birthday', 'grade', 'school', 'major', 'cclass']
    fields = ['phone', 'gender', 'birthday', 'grade', 'school', 'major', 'cclass']

xadmin.site.register(Student, StudentAdmin)

# 在xadmin中注册Teacher
class TeacherAdmin(object):
    list_display = ['phone', 'role', 'title', 'diploma', 'rate_times', 'rate']
    list_filter = ['phone', 'role', 'title', 'diploma', 'rate_times', 'rate']
    search_fields = ['phone', 'role', 'title', 'diploma', 'rate_times', 'rate']
    fields = ['phone', 'role', 'title', 'diploma', 'rate_times', 'rate']

xadmin.site.register(Teacher, TeacherAdmin)

# 在xadmin中注册Admin
class AdminAdmin(object):
    list_display = ['phone', 'role']
    list_filter = ['phone', 'role']
    search_fields = ['phone', 'role']
    fields = ['phone', 'role']

xadmin.site.register(Admin, AdminAdmin)


# 开启功能，修改网页标题和尾部
class BaseSetting:
    enable_themes = True  # 开启主题功能
    use_bootswatch = True

class GlobalSettings:
    site_title = '安徽大学教务系统后台管理'
    site_footer = '软件工程试验：第11小组'

xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(views.BaseAdminView, BaseSetting)