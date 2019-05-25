from django.forms import ModelForm
from .models import Course, SC


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'name': '课程名称',
            'score': '课程学分',
            'teacher_id':'授课老师的id',
            'time': '上课时间',
            'place': '上课地点',
            'school': '开课院系',
            'code': '课程代码',
        }


class SCForm(ModelForm):
    class Meta:
        model = SC
        fields = '__all__'
        labels = {
            'student_id': '学生的id',
            'course_id': '课程的id',
            'type': '该选课类型',
            'score': '成绩',
        }