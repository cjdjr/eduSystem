from django.shortcuts import render,redirect, HttpResponse
from eduSystem.settings import USER_TYPE, USER_ID
from rbac.models import UserInfo
from .models import Course,SC
# Create your views here.
def test(request):
    '''
    测试页面
    :param request:
    :return: html
    '''
    return render(request,'test.html')

def select(request):
    '''
    选课页面
    :param request:
    :return: html
    '''
    if request.method=='GET':
        if request.session[USER_TYPE] == 0:        #只有学生才能选课
            course_list = Course.objects.all()
            return render(request, "select.html",
                        {"course_list": course_list, "user_type": request.session[USER_TYPE]})
        else:
            HttpResponse("只有学生才能选课！")
    elif request.method=='POST':
        print("POST")
        print(request.POST.getlist("checkbox_list"))
        list=request.POST.getlist("checkbox_list")
        flag=1
        for each in list:
            each=int(each)
            print(SC.objects.filter(student_id=UserInfo.objects.get(id=request.session[USER_ID]),course_id=Course.objects.get(id=each)))
            if SC.objects.filter(student_id=UserInfo.objects.get(id=request.session[USER_ID]),course_id=Course.objects.get(id=each)) != []:
                print("hah")
                flag=0
            else:
                sc=SC(student_id=UserInfo.objects.get(id=request.session[USER_ID]),course_id=Course.objects.get(id=each),type="专业选修")
                print(sc)
                sc.save()
        print(request.session[USER_ID])
        if flag==0:
            return HttpResponse("您已选过其中一门课程")
        return redirect(select)
    else:
        HttpResponse("错误")
