from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('worker', views.worker, name='worker'),
    path('chief', views.chief, name='chief'),
    path('high_worker', views.high_worker, name='high_worker'),
]