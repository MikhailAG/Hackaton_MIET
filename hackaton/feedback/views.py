from django.http import HttpResponseRedirect
from django.shortcuts import render
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
            if settings.CURRENT_USER.role.name == 'Intern':
                return HttpResponseRedirect('feedbacks')
            else:
                return HttpResponseRedirect('all_workers')
    return render(request, 'auth.html')

def all_workers(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')

    users = Users.objects.all()
    current_user = settings.CURRENT_USER
    feedback = Feedbacks.objects.all()
    context = {
        'users': users,
        'current_user': current_user,
        'feedback': feedback,
    }

    return render(request, 'all_workers.html', context)

def worker_user(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')

    intern_id = request.GET.get('id')
    users = Users.objects.all()
    current_user = settings.CURRENT_USER
    feedback = Feedbacks.objects.filter(user_id=intern_id)
    intern = users.get(id=intern_id)
    lead_interns = users.filter(lead_user=intern)
    context = {
        'users': users,
        'current_user': current_user,
        'intern': intern,
        'feedback': feedback,
        'lead_interns': lead_interns
    }

    return render(request, 'worker_user.html', context)

def feedbacks_user(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')

    fb_id = request.GET.get('id')
    users = Users.objects.all()
    current_user = settings.CURRENT_USER
    feedback = Feedbacks.objects.all()
    lead = feedback.get(id=fb_id).from_user
    user_feedbacks = feedback.filter(user_id=current_user.id)
    context = {
        'users': users,
        'current_user': current_user,
        'feedback': feedback,
        'lead': lead,
        'user_feedbacks': user_feedbacks,
    }

    return render(request, 'feedbacks_user.html', context)

def feedbacks(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')

    users = Users.objects.all()
    current_user = settings.CURRENT_USER
    feedback = Feedbacks.objects.all()
    context = {
        'users': users,
        'current_user': current_user,
        'feedback': feedback,
    }

    return render(request, 'feedbacks.html', context)
