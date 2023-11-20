from django.contrib import admin
from .models import EnArriendo, EstArrendado


@admin.register(EnArriendo)
class EnArriendoAadmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'fecha',
                    'tipo', 'desc', 'ancho', 'largo', 'owner']


@admin.register(EstArrendado)
class EstArrendadoAadmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'source_model']
