from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .scripts.auth_script import authfunc
from django.conf import settings

Users = apps.get_model('feedback', 'Users')

def auth(request):
    if request.method == 'POST' and 'login-app' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        auth_result = authfunc(username, password)
        print('Статус входа:', auth_result)
        if auth_result == 2 or auth_result == 3 or auth_result == 4:
            print('Роль пользователя:', settings.CURRENT_USER.role_id)
            return HttpResponseRedirect('worker')
    return render(request, 'auth.html')

def worker(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')
    return render(request, 'worker.html')
