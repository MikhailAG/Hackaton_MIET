from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('all_workers', views.all_workers, name='all_workers'),
    path('worker_user', views.worker_user, name='worker_user'),
    path('feedbacks_user', views.feedbacks_user, name='feedbacks_user'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    path('notifications', views.notifications, name="notifications")
]