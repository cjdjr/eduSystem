from django.shortcuts import render, redirect, HttpResponse, reverse
from rbac.service.init_permission import init_permission
from django.conf import settings
from eduSystem.settings import USER_ID, USER_TYPE
import json
from rbac.forms import UserInfoModelForm
from rbac.models import UserInfo


# Create your views here.


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "GET":
        print()
        try:
            test = request.session[settings.SESSION_PERMISSION_URL_KEY]
        except:
            return render(request, "login.html", {'error': json.dumps(False)})
        else:
            return redirect('/index/')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user_obj = UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return render(request, "login.html", {'error': json.dumps(True), 'message': '用户名或密码错误'})
        else:
            init_permission(request, user_obj)
            return redirect('/index/')


def logout(request):
    try:
        del request.session[settings.SESSION_PERMISSION_URL_KEY]
        del request.session[settings.SESSION_MENU_KEY]
    except:
        return redirect(login)
    else:
        return redirect(login)