from django.forms import ModelForm
from .models import Student, Teacher, Admin


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'phone': '电话',
            'gender': '性别',
            'birthday': '生日',
            'grade': '年级',
            'school': '学院',
            'major': '专业',
            'cclass': '班级',
        }


class TeacherModelForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'phone': '电话',
            'gender': '性别',
            'birthday': '生日',
            'role': '角色',
            'title': '职称',
            'diploma': '学历',
            'school': '学院',
            'rate_times': '评分次数',
            'rate': '评分',
        }


class AdminModelForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        labels = {
            'phone': '电话',
            'role': '角色',
        }