from django import forms
from .models import EnArriendo


class ArreindoForm(forms.ModelForm):
    class Meta:
        model = EnArriendo
        fields = ['titulo', 'precio', 'tipo', 'largo', 'ancho', 'desc']
