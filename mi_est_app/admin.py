from django.contrib import admin
from .models import EnArriendo


@admin.register(EnArriendo)
class EnArriendoAadmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'fecha',
                    'tipo', 'desc', 'ancho', 'largo', 'owner']
