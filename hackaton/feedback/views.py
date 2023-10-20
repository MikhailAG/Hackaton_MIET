from django.shortcuts import render
from .models import *

# Create your views here.
def auth(request):
    data = Users.objects.all()
    return render(request, 'auth.html')

def worker(request):
    data = Users.objects.all()
    return render(request, 'worker.html')
