from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EnArriendo, EstArrendado
from .forms import ArreindoForm

# Create your views here.


def index(request):
    estacionamientos = EnArriendo.objects.all()
    return render(request, 'mi_est_app/index.html', {'estacionamientos': estacionamientos})


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
def ver_estacionamiento(request, id):
    esta = EnArriendo.objects.get(id=id)
    context = {'esta': esta}
    return render(request, 'mi_est_app/ver_estacionamiento.html', context)


@login_required
def estacionamiento_arrendado(reqeust, id):
    en_arriendo = EnArriendo.objects.get(id=id)
    esta_arrendado, created = EstArrendado.objects.get_or_create(
        user=reqeust.user,
        source_model=en_arriendo
    )
    return redirect('mi_est_app:arriendos')


@login_required
def arriendos(request):
    arriendo = EstArrendado.objects.filter(user=request.user)
    context = {'arriendo': arriendo}
    return render(request, 'mi_est_app/arriendos.html', context)


@login_required
def arriendo(request, id):
    arriendo = EstArrendado.objects.filter(user=request.user).get(id=id)
    context = {'arriendo': arriendo}
    return render(request, 'mi_est_app/arriendo.html', context)


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
