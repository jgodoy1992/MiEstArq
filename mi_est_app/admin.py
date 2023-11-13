from django.contrib import admin
from .models import EnArriendo, Detalle


@admin.register(EnArriendo)
class EnArriendoAadmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'owner']


@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'tipo', 'desc',
                    'ancho', 'largo', 'esta']
