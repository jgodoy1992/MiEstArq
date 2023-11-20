from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUsuario


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)

        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('mi_est_app:index')
    else:
        form = RegistroUsuario()

    context = {'form': form}
    return render(request, 'registration/registro.html', context)

# Create your views here.
