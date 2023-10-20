from django.shortcuts import render

# Create your views here.
def auth(request):
    return render(request, 'auth.html')
def worker(request):
    return render(request, 'worker.html')
def chief(request):
    return render(request, 'chief.html')
def high_worker(request):
    return render(request, 'high_worker.html')