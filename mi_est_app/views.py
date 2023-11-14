from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import EnArriendo

# Create your views here.


def index(request):
    return render(request, 'mi_est_app/index.html')


@login_required
def dashboard(request):
    return render(request, 'mi_est_app/dashboard.html')


@login_required
def estacionamientos(request):
    esta = EnArriendo.objects.filter(owner=request.user)
    context = {'esta': esta}
    return render(request, 'mi_est_app/estacionamientos.html', context)


@login_required
def estacionamiento(request, id):
    esta = EnArriendo.objects.filter(owner=request.user).get(id=id)
    context = {'esta': esta}
    return render(request, 'mi_est_app/estacionamiento.html', context)
