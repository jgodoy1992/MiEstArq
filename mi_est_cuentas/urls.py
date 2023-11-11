from django.urls import path, include
from . import views

app_name = 'mi_est_cuentas'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name='registro'),
]
