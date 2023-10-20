from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps

Users = apps.get_model('feedback', 'Users')

def auth(request):
    if request.method == 'POST' and 'login-app' in request.POST:
        from auth_script import authfunc
        authfunc(request.username, request.password)
        return HttpResponseRedirect('worker')
    return render(request, 'auth.html')

def worker(request):
    return render(request, 'worker.html')
