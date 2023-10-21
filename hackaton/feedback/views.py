from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.apps import apps
from .scripts.auth_script import authfunc
from django.conf import settings

Users = apps.get_model('feedback', 'Users')
Feedbacks = apps.get_model('feedback', 'Feedbacks')
def auth(request):
    if request.method == 'POST' and 'login-app' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        auth_result = authfunc(username, password)
        print('Статус входа:', auth_result)
        if auth_result == 2 or auth_result == 3 or auth_result == 4:
            print('Роль пользователя:', settings.CURRENT_USER.role_id)
            request.session['role'] = settings.CURRENT_USER.role_id
            request.session['name'] = settings.CURRENT_USER.name
            return HttpResponseRedirect('worker')
    return render(request, 'auth.html')

def worker(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')

    users = Users.objects.all()
    current_user = settings.CURRENT_USER
    feedback = Feedbacks.objects.all()

    return render(request, 'worker.html',{'users': users, 'current_user': current_user, 'feedback': feedback})
