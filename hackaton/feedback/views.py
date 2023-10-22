from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .scripts.auth_script import authfunc
from django.conf import settings
from feedback.scripts.translator import translate_to_english
from feedback.scripts.textblob_script import sentiment, objectivity
from feedback.scripts.generate_integral_feedback import generate_feedback
from feedback.models import Users
from feedback.models import Feedbacks
from feedback.models import Notifications

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

    if request.method == 'POST' and 'feedback-text' in request.POST:
        feedback = request.POST['feedback-text']
        body_english = translate_to_english(feedback)
        Feedbacks.objects.create(
            body=feedback,
            body_english=body_english,
            stars=sentiment(body_english),
            subjectivity=objectivity(body_english),
            user_id=intern_id,
            from_user_id=current_user.id
        )
        print(Feedbacks.objects.last())

    if request.method == 'POST' and 'comment-text' in request.POST:
        comment = request.POST['comment-text']
        Notifications.objects.create(
            comment=comment,
            lead=intern,
            user=current_user
        )
        return HttpResponseRedirect('/all_workers')

    if request.method == 'POST' and 'create-integral' in request.POST:
        integral = generate_feedback(intern, None)
        context['integral'] = integral

    return render(request, 'worker_user.html', context)

def feedbacks_user(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')

    fb_id = request.GET.get('id')
    users = Users.objects.all()
    current_user = settings.CURRENT_USER
    feedback = Feedbacks.objects.all()
    lead = feedback.get(id=fb_id).from_user
    user_feedback = feedback.get(id=fb_id)
    context = {
        'users': users,
        'current_user': current_user,
        'feedback': feedback,
        'lead': lead,
        'user_feedback': user_feedback,
    }
    if request.method == 'POST' and 'create-integral' in request.POST:
        integral = generate_feedback(settings.CURRENT_USER, None)
        context['integral'] = integral

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

    if request.method == 'POST' and 'create-integral' in request.POST:
        integral = generate_feedback(settings.CURRENT_USER, None)
        context['integral'] = integral

    return render(request, 'feedbacks.html', context)

def notifications(request):
    if isinstance(settings.CURRENT_USER, str):
        return HttpResponseRedirect('/')
    nots = settings.CURRENT_USER.received_notifications.all()
    print(settings.CURRENT_USER)
    print(settings.CURRENT_USER.received_notifications.filter(is_read=False))
    print(nots)
    context = {
        'notifications': nots,
        'current_user': settings.CURRENT_USER
    }
    
    return render(request, 'notifications.html', context)
