from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mi_est_app/index.html')


def dashboard(request):
    return render(request, 'mi_est_app/dashboard.html')
