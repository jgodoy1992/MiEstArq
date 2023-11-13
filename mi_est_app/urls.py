from django.urls import path
from . import views

app_name = 'mi_est_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('estacionamientos/', views.estacionamientos, name='estacionamientos'),
    path('estacionamiento/<int:id>',
         views.estacionamiento, name='estacionamiento')
]
