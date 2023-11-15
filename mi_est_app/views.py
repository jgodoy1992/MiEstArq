from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EnArriendo
from .forms import ArreindoForm

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


@login_required
def nuevo_arriendo(request):
    if request.method == 'POST':
        form = ArreindoForm(data=request.POST)
        if form.is_valid():
            est_form = form.save(commit=False)
            est_form.owner = request.user
            est_form.save()
            return redirect('mi_est_app:estacionamientos')
    else:
        form = ArreindoForm()

    context = {'form': form}
    return render(request, 'mi_est_app/nuevo_est.html', context)


@login_required
def editar_arriendo(request, id):
    esta = EnArriendo.objects.filter(owner=request.user).get(id=id)
    if request.method != 'POST':
        form = ArreindoForm(instance=esta)
    else:
        form = ArreindoForm(instance=esta, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_est_app:estacionamientos')

    context = {'esta': esta, 'form': form}
    return render(request, 'mi_est_app/editar_arriendo.html', context)


@login_required
def elimiar_arriendo(request, id):
    esta = EnArriendo.objects.filter(owner=request.user).get(id=id)
    esta.delete()
    return redirect('mi_est_app:estacionamientos')
